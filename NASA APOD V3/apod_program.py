"""
    Name: apod_program.py
    Author: William A Loring
    Created: 09-29-2022
    Purpose: Get Astronomy Photo of the Day
    Display as a thumbnail and normal size
    Command line to rebuild ui to py
    pyside6-uic main_window.ui -o ui_main_window.py
"""

import sys
import datetime
# pip install pyside6
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
# Import gui py file created by QT Designer
from ui_main_window import Ui_MainWindow
from ui_display_photo import Ui_Dialog
# Import controller class that does all the work
from apod_class import APODClass


class APODViewer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(APODViewer, self).__init__()
        """NASA APOD Viewer"""
        # Create the GUI
        self.setupUi(self)
        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Set window title bar icon, shows in task bar
        my_icon = QIcon()
        my_icon.addFile("telescope-32.png")
        self.setWindowIcon(my_icon)
        
        # Get today's date
        display_date = datetime.date.today()
        # Set dateEdit widget to today's date
        self.dateEdit.setDate(display_date)
        # Create apod object
        self.apod_class = APODClass()

        # Create an instance of the photo dialog gui
        self.photo_dialog = photo_dialog()

        # Connect the clicked event/signal to the display_data handler/slot
        # Display apod with button or return/enter keys
        self.btn_display_apod.clicked.connect(self.display_data)
        self.btn_display_apod.setShortcut("Return")
        self.btn_display_apod.setShortcut("Enter")
        self.btn_full_photo.clicked.connect(self.display_photo)

        # Exit the program with button or escape key
        self.btn_exit.clicked.connect(self.close)
        self.btn_exit.setShortcut("Esc")
        # Display initial NASA APOD on startup
        self.display_data()

#--------------------- DISPLAY APOD -------------------------------------------#
    def display_photo(self):
        self.photo_dialog.photo_label.setPixmap(self.apod_class.img)

        self.photo_dialog.display_info()

#--------------------- DISPLAY APOD -------------------------------------------#
    def display_data(self):
        """Get and display APOD description and thumbnail on form label."""
        # Get date from dateEdit widget
        temp_date = self.dateEdit.date()
        # Convert QDate to Python date
        display_date = temp_date.toPython()
        self.lbl_description.setText(
            f"{self.apod_class.get_data(display_date)}")

        self.lbl_thumbnail.setPixmap(self.apod_class.img)

        self.lbl_thumbnail.setScaledContents(True)
        self.lbl_thumbnail.resize(225, 225)

#------------ OVERRIDE MOUSE EVENTS TO MOVE PROGRAM WINDOW --------------------#
    def mousePressEvent(self, event):
        """Override the mousePressEvent"""
        # Store the current position of the mouse in previous position
        self.previous_pos = event.globalPosition()

    def mouseMoveEvent(self, event):
        """Override the mouseMoveEvent"""
        # Subtract the previous position from the current position
        delta = event.globalPosition() - self.previous_pos
        # Add the delta calculation to the current position
        self.move(self.x() + delta.x(), self.y()+delta.y())
        # Store the current position
        self.previous_pos = event.globalPosition()
        # self._drag_active = True

    def mouseReleaseEvent(self, event):
        """Override the mouseReleaseEvent"""
        pass
        # if self._drag_active:
        #     self._drag_active = False


#--------------------- DISPLAY PHOTO DIALOG CLASS -----------------------------#
class photo_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.photo_display_ui = Ui_Dialog()
        self.photo_display_ui.setupUi(self)

        # Set window title bar icon, shows in task bar
        my_icon = QIcon()
        my_icon.addFile("telescope-icon.png")
        self.setWindowIcon(my_icon)
        self.setWindowTitle("NASA APOD")

        self.photo_label = self.photo_display_ui.lbl_photo

    def display_info(self):
        """ Create the 7 day forecast dialog """
        # Show the dialog with exec()
        # Blocks all other windows until this is closed
        self.exec()


#-------------------------- START APPLICATION ---------------------------------#
# Create application object
apod_viewer = QApplication(sys.argv)
# Set a QT style
apod_viewer.setStyle("Fusion")
# Create program object
window = APODViewer()
# Make program visible
window.show()
# Execute the program, setup clean exit of program
sys.exit(apod_viewer.exec())
