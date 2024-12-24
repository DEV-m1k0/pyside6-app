# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from PySide6 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 600)
        MainWindow.setStyleSheet(u"background-color: #14213D;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, 5)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFFFFF;")
        self.label.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.users_list = QListWidget(self.frame)
        self.users_list.setObjectName(u"users_list")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.users_list.setFont(font1)
        self.users_list.setStyleSheet(u"background-color: #E5E5E5;\n"
"color: black;\n"
"border-radius: 5px;\n"
"padding-top: 10px;")
        self.users_list.setFrameShadow(QFrame.Shadow.Plain)
        self.users_list.setLineWidth(1)
        self.users_list.setMidLineWidth(0)
        self.users_list.setSpacing(5)
        self.users_list.setGridSize(QSize(0, 30))
        self.users_list.setModelColumn(0)
        self.users_list.setUniformItemSizes(False)
        self.users_list.setWordWrap(False)
        self.users_list.setItemAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.users_list)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_search = QLineEdit(self.frame)
        self.input_search.setObjectName(u"input_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_search.sizePolicy().hasHeightForWidth())
        self.input_search.setSizePolicy(sizePolicy1)
        self.input_search.setMinimumSize(QSize(200, 40))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.input_search.setFont(font2)
        self.input_search.setAutoFillBackground(False)
        self.input_search.setStyleSheet(u"background-color: #FFFFFF;\n"
"color: black;\n"
"border-radius: 5px;\n"
"padding-left: 5px;")
        self.input_search.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.horizontalLayout.addWidget(self.input_search)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy1)
        self.btn_search.setMinimumSize(QSize(100, 40))
        self.btn_search.setMaximumSize(QSize(250, 16777215))
        self.btn_search.setFont(font2)
        self.btn_search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search.setStyleSheet(u"background-color: #FCA311;\n"
"border-radius: 5px;\n"
"color: black;")

        self.horizontalLayout.addWidget(self.btn_search)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.combo_box_users_list = QComboBox(self.frame)
        self.combo_box_users_list.addItem("")
        self.combo_box_users_list.addItem("")
        self.combo_box_users_list.addItem("")
        self.combo_box_users_list.setObjectName(u"combo_box_users_list")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_box_users_list.sizePolicy().hasHeightForWidth())
        self.combo_box_users_list.setSizePolicy(sizePolicy2)
        self.combo_box_users_list.setMinimumSize(QSize(250, 40))
        self.combo_box_users_list.setMaximumSize(QSize(16777215, 16777215))
        self.combo_box_users_list.setFont(font2)
        self.combo_box_users_list.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.combo_box_users_list.setStyleSheet(u"background-color: #FCA311;\n"
"color: black;\n"
"border-radius: 5px;\n"
"min-height: 40px;\n"
"min-width: 250px;\n"
"text-align: center;")

        self.verticalLayout_5.addWidget(self.combo_box_users_list)

        self.splitter.addWidget(self.frame)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 85, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_selected_user = QLabel(self.layoutWidget)
        self.label_selected_user.setObjectName(u"label_selected_user")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_selected_user.sizePolicy().hasHeightForWidth())
        self.label_selected_user.setSizePolicy(sizePolicy3)
        self.label_selected_user.setFont(font)
        self.label_selected_user.setStyleSheet(u"color: #FFFFFF;")
        self.label_selected_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_selected_user)

        self.table_widget_info_selected_user = QTableWidget(self.layoutWidget)
        if (self.table_widget_info_selected_user.columnCount() < 3):
            self.table_widget_info_selected_user.setColumnCount(3)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.table_widget_info_selected_user.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.table_widget_info_selected_user.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.table_widget_info_selected_user.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_widget_info_selected_user.setObjectName(u"table_widget_info_selected_user")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_widget_info_selected_user.sizePolicy().hasHeightForWidth())
        self.table_widget_info_selected_user.setSizePolicy(sizePolicy4)
        self.table_widget_info_selected_user.setMinimumSize(QSize(400, 0))
        self.table_widget_info_selected_user.setFont(font2)
        self.table_widget_info_selected_user.setStyleSheet(u"background-color: #E5E5E5;\n"
"border-radius: 5px;\n"
"color: black;")
        self.table_widget_info_selected_user.horizontalHeader().setDefaultSectionSize(125)
        self.table_widget_info_selected_user.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_widget_info_selected_user.horizontalHeader().setStretchLastSection(True)
        self.table_widget_info_selected_user.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_2.addWidget(self.table_widget_info_selected_user)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #FFFFFF;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.table_widget_total_selected_user = QTableWidget(self.layoutWidget)
        self.table_widget_total_selected_user.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        if (self.table_widget_total_selected_user.columnCount() < 2):
            self.table_widget_total_selected_user.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.table_widget_total_selected_user.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.table_widget_total_selected_user.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.table_widget_total_selected_user.setObjectName(u"table_widget_total_selected_user")
        self.table_widget_total_selected_user.setFont(font2)
        self.table_widget_total_selected_user.setAutoFillBackground(False)
        self.table_widget_total_selected_user.setStyleSheet(u"background-color: #E5E5E5;\n"
"border-radius: 5px;\n"
"color: black;")
        self.table_widget_total_selected_user.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_widget_total_selected_user.horizontalHeader().setCascadingSectionResizes(False)
        self.table_widget_total_selected_user.horizontalHeader().setHighlightSections(True)
        self.table_widget_total_selected_user.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_widget_total_selected_user.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.table_widget_total_selected_user)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.btn_get_excel_selected_user = QPushButton(self.layoutWidget)
        self.btn_get_excel_selected_user.setObjectName(u"btn_get_excel_selected_user")
        self.btn_get_excel_selected_user.setEnabled(False)
        self.btn_get_excel_selected_user.setMinimumSize(QSize(250, 55))
        self.btn_get_excel_selected_user.setMaximumSize(QSize(16777215, 16777215))
        self.btn_get_excel_selected_user.setFont(font2)
        self.btn_get_excel_selected_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_get_excel_selected_user.setStyleSheet(u"QPushButton{\n"
"	background-color: #FCA311;\n"
"	color: black;\n"
"	border-radius: 5px;\n"
"	min-height: 40px;\n"
"	min-width: 250px;\n"
"	text-align: center;\n"
"	margin-bottom: 15px;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(213, 137, 14);\n"
"	color: rgb(44, 44, 44);\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.btn_get_excel_selected_user)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_7.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043b\u044e\u0434\u0435\u0439", None))
        self.input_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.combo_box_users_list.setItemText(0, "Выберите действие")
        self.combo_box_users_list.setItemText(1, "Импортировать excel")
        self.combo_box_users_list.setItemText(2, "Экспортировать excel")

        self.combo_box_users_list.setCurrentText("")
        self.combo_box_users_list.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.label_selected_user.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
        ___qtablewidgetitem = self.table_widget_info_selected_user.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None));
        ___qtablewidgetitem1 = self.table_widget_info_selected_user.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem2 = self.table_widget_info_selected_user.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e:", None))
        ___qtablewidgetitem3 = self.table_widget_total_selected_user.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None));
        ___qtablewidgetitem4 = self.table_widget_total_selected_user.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        self.btn_get_excel_selected_user.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c excel \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

