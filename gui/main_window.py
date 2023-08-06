from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDialog
from gui.login_window import LoginDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Rankone')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.show_login_dialog)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def show_login_dialog(self):
        login_dialog = LoginDialog(self)
        if login_dialog.exec() == QDialog.accepted:
            print("Login successful!")