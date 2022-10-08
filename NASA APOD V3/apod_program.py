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
from PySide6.QtWidgets import QMainWindow, QDialog, QApplication
# Import gui py file created by QT Designer
from ui_main_window import Ui_MainWindow
from ui_display_photo import Ui_Dialog
# Import controller class that does all the work
from apod_class import APODClass


class APODViewer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(APODViewer, self).__init__()
        """NASA APOD Viewer"""
        # Create the GUI from Ui_MainWindow argument
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
        # Create apod_class object to access methods and properties
        # APODClass does all the work on getting APOD data
        self.apod_class = APODClass()

        # Create an instance of the photo dialog gui
        # Used to show photo_dialog dialog for APOD photo
        self.photo_dialog = photo_dialog()

        # Connect the clicked event/signal to the display_data handler/slot
        # Display APOD with button or return/enter keys
        self.btn_display_apod.clicked.connect(self.display_apod_data)
        self.btn_display_apod.setShortcut("Return")
        self.btn_display_apod.setShortcut("Enter")
        # Display photo in dialog
        self.btn_full_photo.clicked.connect(self.display_photo)

        # Exit the program with button or escape key
        self.btn_exit.clicked.connect(self.close)
        self.btn_exit.setShortcut("Esc")
        # Display initial NASA APOD on startup
        self.display_apod_data()

#--------------------- DISPLAY APOD -------------------------------------------#
    def display_photo(self):
        """Display APOD in dialog box."""
        # Set APOD photo to label
        self.photo_dialog.photo_label.setPixmap(self.apod_class.img)
        # Display APOD photo dialog box
        self.photo_dialog.display_info()

#--------------------- DISPLAY APOD DATA --------------------------------------#
    def display_apod_data(self):
        """Get and display APOD description and thumbnail on form label."""
        # Get date from dateEdit widget
        temp_date = self.dateEdit.date()
        # Convert QDate to Python date
        display_date = temp_date.toPython()
        # Get display_date's APOD data
        self.apod_class.get_data(display_date)
        # Display explanation in labe.
        self.lbl_explanation.setText(
            f"{self.apod_class.explanation}")

        if self.apod_class.img == None:
            # If there is not an image, it is a video
            self.lbl_thumbnail.setText("YouTube Video")
            self.btn_full_photo.setEnabled(False)

        else:
            self.btn_full_photo.setEnabled(True)
            # Set APOD photo to image on label
            self.lbl_thumbnail.setPixmap(self.apod_class.img)
            # Scale image to fit label
            self.lbl_thumbnail.setScaledContents(True)
            # Set label size
            self.lbl_thumbnail.resize(225, 225)

#------------ OVERRIDE MOUSE EVENTS TO MOVE PROGRAM WINDOW --------------------#
    def mousePressEvent(self, event):
        """Override the mousePressEvent."""
        # Store the current position of the mouse in previous position
        self.previous_pos = event.globalPosition()

    def mouseMoveEvent(self, event):
        """Override the mouseMoveEvent."""
        # Subtract the previous position from the current position
        delta = event.globalPosition() - self.previous_pos
        # Add the delta calculation to the current position
        self.move(self.x() + delta.x(), self.y()+delta.y())
        # Store the current position
        self.previous_pos = event.globalPosition()
        # self._drag_active = True

    def mouseReleaseEvent(self, event):
        """Override the mouseReleaseEvent."""
        pass


#--------------------- DISPLAY PHOTO DIALOG CLASS -----------------------------#
class photo_dialog(QDialog):
    def __init__(self, parent=None):
        """Display NASA APOD in dialog box."""
        super().__init__(parent)
        self.photo_display_ui = Ui_Dialog()
        self.photo_display_ui.setupUi(self)

        # Set window title bar icon, shows in task bar
        my_icon = QIcon()
        my_icon.addFile("telescope-icon.png")
        self.setWindowIcon(my_icon)

        # Create reference to lbl_photo for use
        # APODViewer class display_photo method to display image
        self.photo_label = self.photo_display_ui.lbl_photo

    def display_info(self):
        """Display photo_dialog."""
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
