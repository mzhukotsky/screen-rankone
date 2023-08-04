from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QDialog
from utils.selenium_utils import login_to_rankone

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("E-mail")

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setPlaceholderText("Password")

        layout.addWidget(self.login_edit)
        layout.addWidget(self.password_edit)

        self.login_button = QPushButton("Sign in", self)
        self.login_button.clicked.connect(self.on_login_clicked)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def on_login_clicked(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        success = login_to_rankone(login, password)

        if success:
            self.accept()
        else:
            print("Login failed. Please try again")

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
        if login_dialog.exec() == QDialog.Accepted:
            print("Login successful!")