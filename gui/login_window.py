from PyQt6.QtWidgets import QPushButton, QLineEdit, QVBoxLayout, QDialog, QCheckBox
from PyQt6.QtCore import QSettings
from utils.selenium_utils import login_to_rankone
from gui.profile_window import ProfileWindow

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

        self.remember_password_checkbox = QCheckBox("Remember Password", self)
        layout.addWidget(self.remember_password_checkbox)

        self.load_saved_credentials()

        self.setLayout(layout)

    def load_saved_credentials(self):
        settings = QSettings("YourOrganization", "YourApplication")
        saved_username = settings.value("username", type=str)
        saved_password = settings.value("password", type=str)
        saved_remember_password = settings.value("remember_password", type=bool)

        if saved_username:
            self.login_edit.setText(saved_username)
        if saved_remember_password and saved_password:
            self.password_edit.setText(saved_password)
            self.remember_password_checkbox.setChecked(True)

    def on_login_clicked(self):
        self.login = self.login_edit.text()
        self.password = self.password_edit.text()
        success, short_profile_name = login_to_rankone(self.login, self.password)
    

        if success:
            self.accept()
            self.save_credentials()
            self.open_profile_window(short_profile_name)
        else:
            print("Login failed. Please try again")

    def open_profile_window(self, short_profile_name):  # Add short_profile_name as an argument
        profile_name = f"https://p1.api.rankone.global/profile-events/{short_profile_name}"
        profile_window = ProfileWindow(profile_name)
        profile_window.exec()

    def save_credentials(self):
        settings = QSettings("YourOrganization", "YourApplication")
        settings.setValue("username", self.login)
        settings.setValue("password", self.password if self.remember_password_checkbox.isChecked() else "")
        settings.setValue("remember_password", self.remember_password_checkbox.isChecked())
    