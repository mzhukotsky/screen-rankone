from utils.rankone_api import get_profile_events
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys

def main():
    username = "bilibomka"
    profile_events = get_profile_events(username)
    if profile_events:
        
        print(profile_events)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())