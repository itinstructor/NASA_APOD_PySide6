"""
    Name: apog_program.py
    Author: William A Loring
    Created: 09-29-2022
    Purpose: 
    Command line to rebuild ui to py
    pyside6-uic main_window.ui -o main_ui.py
"""

import sys
from PySide6.QtCore import Qt
# from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
# Import gui py file created by QT Designer
from main_ui import Ui_MainWindow
# Import controller class that does all the work.
from apod_class import APODClass


class APODViewer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(APODViewer, self).__init__()

        """ Initialize PySide6 QT GUI"""
        # Create the GUI
        self.setupUi(self)
        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.apod_class = APODClass()

        # Connect the clicked event/signal to the set_weather event handler/slot
        self.btn_get_data.clicked.connect(self.display_data)
        self.btn_get_data.setShortcut("Return")

        # Exit the program
        self.btn_exit.clicked.connect(self.close)
        self.btn_exit.setShortcut("Esc")

#--------------------- GET WEATHER -------------------#
    def display_data(self):
        """ Get and display weather on form """
        # self.apod_class.get_data()
        self.lbl_description.setText(
            f"{self.apod_class.get_data()}")

#-------- OVERRIDE MOUSE EVENTS TO MOVE PROGRAM WINDOW -------------#
    def mousePressEvent(self, event):
        """ Override the mousePressEvent """
        # Store the current position of the mouse in previous position
        self.previous_pos = event.globalPosition()

    def mouseMoveEvent(self, event):
        """ Override the mouseMoveEvent """
        # Subtract the previous position from the current position
        delta = event.globalPosition() - self.previous_pos
        # Add the delta calculation to the current position
        self.move(self.x() + delta.x(), self.y()+delta.y())
        # Store the current position
        self.previous_pos = event.globalPosition()
        # self._drag_active = True

    def mouseReleaseEvent(self, event):
        """ Override the mouseReleaseEvent """
        pass
        # if self._drag_active:
        #     self._drag_active = False


#--------------------- START APPLICATION -------------------#
# Create application object
apod_viewer = QApplication(sys.argv)
# Set a QT style
apod_viewer.setStyle('Fusion')
# Set colors to darkPalette, from external py file
#    cat_fact.setPalette(dark_palette.darkPalette)
# Create program object
window = APODViewer()
# Make program visible
window.show()
# Execute the program, setup clean exit of program
sys.exit(apod_viewer.exec())
