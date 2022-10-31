from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from ui_display_photo import Ui_Dialog

#--------------------- DISPLAY PHOTO DIALOG CLASS -----------------------------#
class PhotoDialog(QDialog):
    def __init__(self, parent=None):
        """Display NASA APOD in dialog box."""
        super().__init__(parent)
        self.photo_display_ui = Ui_Dialog()
        self.photo_display_ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Set window title bar icon, shows in task bar
        my_icon = QIcon()
        my_icon.addFile("telescope-icon-24300.png")
        self.setWindowIcon(my_icon)

        # Create reference to lbl_photo for use
        # APODViewer class display_photo method to display image
        self.photo_label = self.photo_display_ui.lbl_photo

    def display_info(self):
        """Display photo_dialog."""
        # Show the dialog with exec()
        # Blocks all other windows until this is closed
        self.exec()
