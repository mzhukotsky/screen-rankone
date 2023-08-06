from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.profile_window import ProfileWindow
import sys

# Executing GUI window with login
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())