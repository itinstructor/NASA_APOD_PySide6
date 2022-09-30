# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 346)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette = QPalette()
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 830, 266))
        self.lbl_description = QLabel(self.groupBox_2)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setGeometry(QRect(10, 30, 576, 225))
        self.lbl_description.setFrameShape(QFrame.Box)
        self.lbl_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_description.setWordWrap(True)
        self.lbl_thumbnail = QLabel(self.groupBox_2)
        self.lbl_thumbnail.setObjectName(u"lbl_thumbnail")
        self.lbl_thumbnail.setGeometry(QRect(604, 30, 225, 225))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 285, 830, 50))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.btn_display_apod = QPushButton(self.groupBox)
        self.btn_display_apod.setObjectName(u"btn_display_apod")

        self.horizontalLayout.addWidget(self.btn_display_apod)

        self.btn_full_photo = QPushButton(self.groupBox)
        self.btn_full_photo.setObjectName(u"btn_full_photo")

        self.horizontalLayout.addWidget(self.btn_full_photo)

        self.btn_exit = QPushButton(self.groupBox)
        self.btn_exit.setObjectName(u"btn_exit")

        self.horizontalLayout.addWidget(self.btn_exit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NASA APOD Viewer", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"NASA APOD", None))
        self.lbl_description.setText("")
        self.lbl_thumbnail.setText("")
        self.groupBox.setTitle("")
        self.btn_display_apod.setText(QCoreApplication.translate("MainWindow", u"Get APOD", None))
        self.btn_full_photo.setText(QCoreApplication.translate("MainWindow", u"Full Photo", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

