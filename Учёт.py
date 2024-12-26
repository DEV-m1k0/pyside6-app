from datetime import datetime, date
import os
import pandas as pd
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,
    QResizeEvent)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QTableWidgetItem, QFileDialog,
    QMessageBox)
from main_ui import Ui_MainWindow
from models import create_db_and_tables, Session
from sqlalchemy.sql import select
from pathlib import Path, PosixPath
from utils.user import User, get_all_users, get_user_by_full_name
from utils.item import get_item_by_id, Item
from utils.user_item import get_user_items_by_user_id, UserItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            create_db_and_tables()
        except Exception as e:
            pass
        try:
            self.__fill_out_list_widget()
        except Exception as e:
            pass
        self.ui.users_list.clicked.connect(self.select_user)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.input_search.textChanged.connect(self.input_search_text_changed)
        self.ui.combo_box_users_list.currentIndexChanged.connect(self.select_action)
        self.ui.btn_get_excel_selected_user.clicked.connect(self.user_excel)
        self.ui.users_list.resizeEvent = self.users_list_resize_event

    def resizeEvent(self, event):
        self.update_font_size()
        return super().resizeEvent(event)

    def update_font_size(self):
        width = self.width()
        height = self.height()

        font_size_title = min(width // 25, height // 22)
        font_size_text = min(width // 18, height // 27)

        if font_size_title >= 30:
            self.ui.label.setStyleSheet(f"font-size: {font_size_title}px; color: white;")
            self.ui.label_3.setStyleSheet(f"font-size: {font_size_title}px; color: white;")
            self.ui.label_selected_user.setStyleSheet(f"font-size: {font_size_title}px; color: white;")
        if font_size_text >= 18 and font_size_text <= 32:
            self.ui.users_list.setStyleSheet(self.ui.users_list.styleSheet() + f"font-size: {font_size_text}px;")

        
    def users_list_resize_event(self, event: QResizeEvent):
        self.set_size_for_row()


    def set_size_for_row(self):
        for i in range(self.ui.users_list.count()):
            item = self.ui.users_list.item(i)
            item.setSizeHint(QSize(self.ui.users_list.width()-2, 30))


    def input_search_text_changed(self, event):
        self.search()

    def select_action(self, action_id: int):
        if action_id == 1:
            self.import_excel()
            self.ui.combo_box_users_list.setCurrentIndex(0)
        elif action_id == 2:
            try:
                options = QFileDialog.Option()
                directory = QFileDialog.getExistingDirectory(
                    self,
                    "Выберите директорию для сохранения файла",
                    str(Path.home()),
                    options=options
                )
                if directory:
                    path_to_save_file = directory
                users = get_all_users()
                data = []
                data.append(['Создано:', datetime.now().strftime("%d.%m.%Y")])
                
                for user in users:
                    users_items = get_user_items_by_user_id(user.id)
                    data.append([user.full_name])
                    unique_items = []  
                    for i in users_items:
                        item_title = get_item_by_id(i.item_id).title
                        item_count = i.count
                        item_date = i.date_of_receipt
                        if item_title not in unique_items:
                            unique_items.append(item_title)
                        data.append([item_title, item_count, item_date])
                    data.append(['Итого:'])
                    for unique in unique_items:
                        count = 0
                        for i in users_items:
                            if unique == get_item_by_id(i.item_id).title:
                                count += i.count
                        data.append([unique, count])
                    data.append([''])

                current_time = datetime.now()
                formatted_time = current_time.strftime("%d-%m-%Y_%H.%M.%S")

                excel_file_name = f"Учёт_{formatted_time}.xlsx"
                df = pd.DataFrame(data=data)
                writer = pd.ExcelWriter(path=f'{path_to_save_file}/{excel_file_name}', engine='xlsxwriter')
                df.to_excel(writer, sheet_name="Sheet1")
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                worksheet.set_column(3,3, 10)
                worksheet.set_column(0,0, 10)
                writer._save()

                message_box = QMessageBox()
                message_box.setWindowTitle("Информация о создании excel")
                message_box.setText(f"""
                                    Excel файл был успешно создан!
                                    """)
                message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                message_box.exec()
                self.ui.combo_box_users_list.setCurrentIndex(0)
            except Exception as e:
                message_box = QMessageBox()
                message_box.setWindowTitle("Информация о создании excel")
                message_box.setText(f"""
                                    При создании excel отчета произошла ошибка!
                                    """)
                message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                message_box.exec()
                self.ui.combo_box_users_list.setCurrentIndex(0)
                                          
    
    def select_user(self, data: QModelIndex):
        try:
            if data.data() == "Пользователь не найден":
                raise Exception
            if str(data.data()[0]).isdigit():
                self.selected_user_str = " ".join(str(data.data()).split(" ")[1:])
            else:
                self.selected_user_str = data.data()
            selected_user_obg = get_user_by_full_name(self.selected_user_str)
            self.ui.label_selected_user.setText(self.selected_user_str)
            self.ui.btn_get_excel_selected_user.setEnabled(True)

            if not selected_user_obg:
                raise Exception
            user_items = get_user_items_by_user_id(user_id=selected_user_obg.id)

            table_widget_info_selected_user = self.ui.table_widget_info_selected_user

            user_items_len = len(user_items)
            table_widget_info_selected_user.setRowCount(user_items_len)

            self.items_and_count = {}

            for i in range(user_items_len):
                item_id = user_items[i].item_id
                item = get_item_by_id(item_id)
                try:
                    self.items_and_count[item.title] += user_items[i].count
                except:
                    self.items_and_count[item.title] = user_items[i].count
                table_widget_info_selected_user.setItem(i, 0, QTableWidgetItem(item.title))
                table_widget_info_selected_user.setItem(i, 1, QTableWidgetItem(str(user_items[i].count)))
                formatted_date = user_items[i].date_of_receipt.strftime("%d.%m.%Y")
                table_widget_info_selected_user.setItem(i, 2, QTableWidgetItem(str(formatted_date)))
                table_widget_info_selected_user.edit
            table_widget_info_selected_user.show()

            len_items_and_count = len(list(self.items_and_count.keys()))
            self.ui.table_widget_total_selected_user.setRowCount(len_items_and_count)

            for i in range(len_items_and_count):
                self.ui.table_widget_total_selected_user.setItem(i, 0, QTableWidgetItem(list(self.items_and_count.keys())[i]))
                self.ui.table_widget_total_selected_user.setItem(i, 1, QTableWidgetItem(str(list(self.items_and_count.values())[i])))
            self.ui.table_widget_total_selected_user.show()
    
        except Exception as e:
            self.ui.label_selected_user.setText("Выберите человека")
            self.ui.btn_get_excel_selected_user.setEnabled(False)
            self.ui.table_widget_info_selected_user.clearContents()
            self.ui.table_widget_total_selected_user.clearContents()

    def user_excel(self):
        try:
            options = QFileDialog.Option()
            directory = QFileDialog.getExistingDirectory(
                self,
                "Выберите директорию для сохранения файла",
                str(Path.home()),
                options=options
            )
            if directory:
                path_to_save_file = directory

            data=[]
            data.append(['Создано:', datetime.now().strftime("%d.%m.%Y")])
            
            selected_user_obg = get_user_by_full_name(self.selected_user_str)
            user_items = get_user_items_by_user_id(user_id=selected_user_obg.id)
            data.append([selected_user_obg.full_name])
            
            for i in user_items:
                item_title = get_item_by_id(i.item_id).title
                item_count = i.count
                item_date = i.date_of_receipt.strftime("%d.%m.%Y")
                data.append([item_title, item_count, item_date])
                
            data.append(['Итого:'])
            
            for i in self.items_and_count:
                data.append([i, self.items_and_count[i]])
                
            current_time = datetime.now()
            formatted_time = current_time.strftime("%d-%m-%Y_%H.%M.%S")
            excel_file_name = f"Учёт_{selected_user_obg.full_name}_{formatted_time}.xlsx"
            df = pd.DataFrame(data=data)
            writer = pd.ExcelWriter(path=f'{path_to_save_file}/{excel_file_name}', engine='xlsxwriter')
            df.to_excel(writer, sheet_name="Sheet1")
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            worksheet.set_column(3,3, 10)
            worksheet.set_column(0,0, 10)
            writer._save()

            message_box = QMessageBox()
            message_box.setWindowTitle("Информация о создании excel")
            message_box.setText(f"""
                                Excel файл был успешно создан!
                                """)
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            message_box.exec()
            self.ui.combo_box_users_list.setCurrentIndex(0)
        except Exception as e:
            message_box = QMessageBox()
            message_box.setWindowTitle("Информация о создании excel")
            message_box.setText(f"""
                                При создании excel отчета произошла ошибка!
                                """)
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            message_box.exec()
        

    def import_excel(self):
        options = QFileDialog.Option()
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите файлы Excel",
            "",
            "Excel Files (*.xlsx *.xls);;All Files (*)",
            options=options
        )

        if files:
            file_paths = [Path(file).resolve() for file in files]

            for file_path in file_paths:
                self.__excel_processing(file_path)
            
            self.ui.users_list.clear()
            self.__fill_out_list_widget()

    
    def __excel_processing(self, path_file: PosixPath):
        df = pd.read_excel(path_file)
        for row in df.values:
            # try:
                name, item, count_str, date_of_receipt = row
                count = int(str(count_str).split(" ")[0])
                
                user_obj = User(full_name=name)
                user_obj.save()


                item_obj = Item(title=item)
                item_obj.save()

                user_item_obj = UserItem(user_id=user_obj.id, item_id=item_obj.id,
                                        count=count, date_of_receipt=date_of_receipt)
                user_item_obj.save()
            # except:
            #     pass
        

    def search(self):
        search_user = self.ui.input_search.text()
        if search_user == "":
            self.ui.table_widget_info_selected_user.clearContents()
            self.ui.table_widget_info_selected_user.setRowCount(0)
            self.ui.table_widget_total_selected_user.clearContents()
            self.ui.table_widget_total_selected_user.setRowCount(0)
            self.ui.label_selected_user.setText("Выберите человека")
            self.ui.btn_get_excel_selected_user.setDisabled(True)
            self.ui.users_list.clear()
            self.__fill_out_list_widget()
        else:
            self.ui.users_list.clear()
            users = get_all_users()
            for user in users:
                if search_user in user.full_name:
                    self.ui.users_list.addItem(f"{user.id}. {user.full_name}")
            self.set_size_for_row()
            if self.ui.users_list.count() == 0:
                self.ui.users_list.addItem(f"Люди с таким именем не найдены")
                self.set_size_for_row()
        
    
    def __fill_out_list_widget(self):
        users = get_all_users()
        users_count = len(users)
        for i in range(users_count):
            self.ui.users_list.addItem(QListWidgetItem(f"{i+1}. {users[i].full_name}"))

        self.set_size_for_row()
    

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowIcon(QIcon(f"{os.path.dirname(__file__)}/hand_document_list_paper_file_icon_219510.ico"))
    window.show()
    app.exec()
    window.close()
    app.closeAllWindows()
    