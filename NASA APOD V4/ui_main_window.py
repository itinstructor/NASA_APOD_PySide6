# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
        self.lbl_explanation = QLabel(self.groupBox_2)
        self.lbl_explanation.setObjectName(u"lbl_explanation")
        self.lbl_explanation.setGeometry(QRect(10, 30, 576, 225))
        self.lbl_explanation.setFrameShape(QFrame.Box)
        self.lbl_explanation.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_explanation.setWordWrap(True)
        self.lbl_explanation.setMargin(5)
        self.lbl_explanation.setIndent(0)
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

        self.btn_hd_photo = QPushButton(self.groupBox)
        self.btn_hd_photo.setObjectName(u"btn_hd_photo")

        self.horizontalLayout.addWidget(self.btn_hd_photo)

        self.btn_random_photo = QPushButton(self.groupBox)
        self.btn_random_photo.setObjectName(u"btn_random_photo")

        self.horizontalLayout.addWidget(self.btn_random_photo)

        self.btn_save_file = QPushButton(self.groupBox)
        self.btn_save_file.setObjectName(u"btn_save_file")

        self.horizontalLayout.addWidget(self.btn_save_file)

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
        self.lbl_explanation.setText("")
#if QT_CONFIG(tooltip)
        self.lbl_thumbnail.setToolTip(QCoreApplication.translate("MainWindow", u"Click to see Full Photo", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_thumbnail.setText("")
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.dateEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Pick a date to see an APOD", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_display_apod.setToolTip(QCoreApplication.translate("MainWindow", u"Get NASA Astronomy Photo of the Day", None))
#endif // QT_CONFIG(tooltip)
        self.btn_display_apod.setText(QCoreApplication.translate("MainWindow", u"Get APOD", None))
#if QT_CONFIG(tooltip)
        self.btn_full_photo.setToolTip(QCoreApplication.translate("MainWindow", u"Display full photo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_full_photo.setText(QCoreApplication.translate("MainWindow", u"Full Photo", None))
#if QT_CONFIG(tooltip)
        self.btn_hd_photo.setToolTip(QCoreApplication.translate("MainWindow", u"Display HD photo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_hd_photo.setText(QCoreApplication.translate("MainWindow", u"HD Photo", None))
#if QT_CONFIG(tooltip)
        self.btn_random_photo.setToolTip(QCoreApplication.translate("MainWindow", u"Display HD photo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_random_photo.setText(QCoreApplication.translate("MainWindow", u"Random Photo", None))
        self.btn_save_file.setText(QCoreApplication.translate("MainWindow", u"&Save Image", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

