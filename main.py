from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QTableWidgetItem)
from main_ui import Ui_MainWindow
from another_ui import Ui_Form
from models import create_db_and_tables, Session
from sqlalchemy.sql import select
from models import User, Item, UserItems

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
        create_db_and_tables()
        self.see_all()
        self.ui.listWidget.clicked.connect(self.open)
        self.ui.pushButton.clicked.connect(self.search)
        self.new_window = AnotherWindow()


    def search(self):
        search_user = self.ui.lineEdit.text()
        if search_user == "":
            self.ui.listWidget.clear()
            self.see_all()
        else:
            user_sql = select(User).where(User.full_name==search_user)
            with Session() as session:
                user = session.scalar(user_sql)
            if not user:
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem("Пользователь не найден")
            else:
                self.ui.listWidget.clear()
                self.ui.listWidget.addItem(user.full_name)

    def __set_user(self, user: User):
        pass
        
    
    def see_all(self):
        with Session() as session:
            users = session.scalars(select(User)).all()
            users_count = len(users)
            for i in range(users_count):
                self.ui.listWidget.addItem(QListWidgetItem(users[i].full_name))
    
    def open(self, data: QModelIndex):
        self.new_window.show()
        self.new_window.setWindowTitle(data.data())
        
        with Session() as session:
            user_sql = select(User).where(User.full_name==data.data())
            user = session.scalar(user_sql)
            
            user_items_sql = select(UserItems).where(UserItems.user_id==user.id)
            user_items = session.scalars(user_items_sql).all()

            tableWidget = self.new_window.ui.tableWidget

            user_items_len = len(user_items)
            tableWidget.setRowCount(user_items_len)

            for i in range(user_items_len):
                item_id = user_items[i].item_id
                item_sql = select(Item).where(Item.id==item_id)
                with Session() as session:
                    item = session.scalar(item_sql)
                tableWidget.setItem(i, 0, QTableWidgetItem(item.title))
                tableWidget.setItem(i, 1, QTableWidgetItem(str(user_items[i].count)))
                
    

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    