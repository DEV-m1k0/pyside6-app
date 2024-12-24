from datetime import datetime, date
import os
import pandas as pd
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QTableWidgetItem, QFileDialog,
    QMessageBox)
from main_ui import Ui_MainWindow
from another_ui import Ui_Form
from models import create_db_and_tables, Session
from sqlalchemy.sql import select
from pathlib import Path, PosixPath
from utils.user import User, get_all_users, get_user_by_full_name
from utils.item import get_item_by_id, Item
from utils.user_item import get_user_items_by_user_id, UserItem
from utils.logging import setup_logging, logging
import openpyxl

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            create_db_and_tables()
            logging.debug("Таблицы в базе данных созданы")
        except Exception as e:
            logging.error(f"Таблицы в базе данных не были созданы {e}")
        try:
            self.__fill_out_list_widget()
            logging.debug("ListWidget заполнен списком пользователей")
        except Exception as e:
            logging.warning(f"При заполнении ListWidget списком пользователей возникла ошибка {e}", exc_info=True)
        self.ui.users_list.clicked.connect(self.select_user)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.combo_box_users_list.currentIndexChanged.connect(self.select_action)
        # self.ui.btn_get_excel_selected_user.clicked.connect(self.user_excel)
        self.new_window = AnotherWindow()
    

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
                for user in users:
                    users_items = get_user_items_by_user_id(user.id)
                    data.append([user.full_name])
                    total = 0
                    for i in users_items:
                        data.append([get_item_by_id(i.item_id).title, i.count, i.date_of_receipt])
                        total += i.count
                    data.append(['Итого', total])
                    data.append([])
                
                current_time = datetime.now()
                formatted_time = current_time.strftime("%d.%m.%Y-%H:%M:%S")

                excel_file_name = f"Учет_{formatted_time}.xlsx"
                df = pd.DataFrame(data=data)
                writer = pd.ExcelWriter(f'{path_to_save_file}/{excel_file_name}', engine='xlsxwriter')
                df.to_excel(writer, sheet_name="Sheet1")
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                worksheet.set_column(3,3, 10)
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
                logging.error(f"{e}", exc_info=True)
                message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                message_box.exec()
                self.ui.combo_box_users_list.setCurrentIndex(0)
                                          
    
    def select_user(self, data: QModelIndex):
        try:
            if data.data() == "Пользователь не найден":
                raise Exception
            if str(data.data()[0]).isdigit():
                selected_user_str = " ".join(str(data.data()).split(" ")[1:])
            else:
                selected_user_str = data.data()
            logging.info(f"Выбран {selected_user_str}")
            selected_user_obg = get_user_by_full_name(selected_user_str)
            logging.debug(f"{selected_user_obg} был найден в базе данных")
            self.ui.label_selected_user.setText(selected_user_str)
            self.ui.btn_get_excel_selected_user.setEnabled(True)

            if not selected_user_obg:
                raise Exception
            user_items = get_user_items_by_user_id(user_id=selected_user_obg.id)

            table_widget_info_selected_user = self.ui.table_widget_info_selected_user

            user_items_len = len(user_items)
            table_widget_info_selected_user.setRowCount(user_items_len)

            items_and_count = {}

            for i in range(user_items_len):
                item_id = user_items[i].item_id
                item = get_item_by_id(item_id)
                try:
                    items_and_count[item.title] += user_items[i].count
                except:
                    items_and_count[item.title] = user_items[i].count
                table_widget_info_selected_user.setItem(i, 0, QTableWidgetItem(item.title))
                table_widget_info_selected_user.setItem(i, 1, QTableWidgetItem(str(user_items[i].count)))
                formatted_date = user_items[i].date_of_receipt.strftime("%d.%m.%Y")
                table_widget_info_selected_user.setItem(i, 2, QTableWidgetItem(str(formatted_date)))
            table_widget_info_selected_user.show()

            len_items_and_count = len(list(items_and_count.keys()))
            self.ui.table_widget_total_selected_user.setRowCount(len_items_and_count)

            for i in range(len_items_and_count):
                self.ui.table_widget_total_selected_user.setItem(i, 0, QTableWidgetItem(list(items_and_count.keys())[i]))
                self.ui.table_widget_total_selected_user.setItem(i, 1, QTableWidgetItem(str(list(items_and_count.values())[i])))
            self.ui.table_widget_total_selected_user.show()
    
        except Exception as e:
            self.ui.label_selected_user.setText("Выберите человека")
            self.ui.btn_get_excel_selected_user.setEnabled(False)
            self.ui.table_widget_info_selected_user.clearContents()
            self.ui.table_widget_total_selected_user.clearContents()
            logging.warning(f"Окно с пользователем {data.data()} не было открыто {e}", exc_info=True)



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
            name, item, count_str, date_of_receipt = row
            count = int(str(count_str).split(" ")[0])
            
            user_obj = User(full_name=name)
            user_obj.save()

            item_obj = Item(title=item)
            item_obj.save()

            user_item_obj = UserItem(user_id=user_obj.id, item_id=item_obj.id,
                                     count=count, date_of_receipt=date_of_receipt)
            user_item_obj.save()
        

    def search(self):
        search_user = self.ui.input_search.text()
        if search_user == "":
            self.ui.users_list.clear()
            self.__fill_out_list_widget()
        else:
            user = get_user_by_full_name(full_name=search_user)
            if user is None:
                self.ui.users_list.clear()
                self.ui.users_list.addItem("Пользователь не найден")
            else:
                self.ui.users_list.clear()
                self.ui.users_list.addItem(f"{user.id}. {user.full_name}")
        
    
    def __fill_out_list_widget(self):
        users = get_all_users()
        users_count = len(users)
        for i in range(users_count):
            self.ui.users_list.addItem(QListWidgetItem(f"{i+1}. {users[i].full_name}"))
    

if __name__ == '__main__':
    setup_logging()
    logging.info("Приложение запущено")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    window.close()
    app.closeAllWindows()
    