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
    QStatusBar, QWidget, QTableWidgetItem, QFileDialog)
from main_ui import Ui_MainWindow
from another_ui import Ui_Form
from models import create_db_and_tables, Session
from sqlalchemy.sql import select
from pathlib import Path, PosixPath
from utils.user import User, get_all_users, get_user_by_full_name
from utils.item import get_item_by_id, Item
from utils.user_item import get_user_items_by_user_id, UserItem
from utils.logging import setup_logging, logging


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
        self.setFixedSize(self.size())
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
        self.ui.listWidget.clicked.connect(self.open)
        self.ui.pushButton.clicked.connect(self.search)

        self.ui.pushButton_2.clicked.connect(self.import_excel)

        self.new_window = AnotherWindow()


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
            
            self.ui.listWidget.clear()
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
        search_user = self.ui.lineEdit.text()
        if search_user == "":
            self.ui.listWidget.clear()
            self.__fill_out_list_widget()
        else:
            user = get_user_by_full_name(full_name=search_user)
            if user is None:
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem("Пользователь не найден")
            else:
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem(user.full_name)
        
    
    def __fill_out_list_widget(self):
        users = get_all_users()
        users_count = len(users)
        for i in range(users_count):
            self.ui.listWidget.addItem(QListWidgetItem(users[i].full_name))
    
    def open(self, data: QModelIndex):
        try:
            if data.data() == "Пользователь не найден":
                raise Exception
            self.new_window.show()
            self.new_window.setWindowTitle(data.data())
            logging.debug(f"Окно пользователя {data.data()} было открыто")
            user = get_user_by_full_name(data.data())
            if not user:
                raise Exception
            user_items = get_user_items_by_user_id(user_id=user.id)

            tableWidget = self.new_window.ui.tableWidget

            user_items_len = len(user_items)
            tableWidget.setRowCount(user_items_len)

            for i in range(user_items_len):
                item_id = user_items[i].item_id
                item = get_item_by_id(item_id)
                tableWidget.setItem(i, 0, QTableWidgetItem(item.title))
                tableWidget.setItem(i, 1, QTableWidgetItem(str(user_items[i].count)))
                tableWidget.setItem(i, 2, QTableWidgetItem(str(user_items[i].date_of_receipt)))
            tableWidget.show()

        except Exception as e:
            logging.warning(f"Окно с пользователем {data.data()} не было открыто {e}", exc_info=True)
            return 0
                
    

if __name__ == '__main__':
    setup_logging()
    logging.info("Приложение запущено")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    