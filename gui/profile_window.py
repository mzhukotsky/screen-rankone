from PyQt6.QtWidgets import QLabel, QVBoxLayout, QDialog
from utils.rankone_api import get_profile_events

class ProfileWindow(QDialog):
    def __init__(self, profile_name):
        super().__init__()
        self.setWindowTitle('Profile')
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.profile_name_label = QLabel(f"Profile Name: {profile_name}", self)
        layout.addWidget(self.profile_name_label)

        self.avatar_label = QLabel("", self)  # Создайте метку для аватара
        layout.addWidget(self.avatar_label)

        self.setLayout(layout)

        # Fetch and display the profile information
        self.populate_profile_info(profile_name)

    def populate_profile_info(self, profile_name):
        profile_name_key = profile_name.split('/')[-1]
        profile_data_get = get_profile_events(profile_name)  # Получите данные о профиле

        if profile_data_get:
            profile_basics = profile_data_get.get("profileBasics", {})
            if profile_name_key in profile_basics:
                profile_info = profile_basics.get(profile_name_key, {})
                profile_nickname = profile_info.get('name', 'N/A')
                avatar_link = profile_info.get('avatar', 'N/A')

                self.profile_name_label.setText(f"Profile Name: {profile_nickname}")
                self.avatar_label.setText(f"Avatar: {avatar_link}")
            else:
                self.profile_name_label.setText("Profile info not found.")
        else:
            self.profile_name_label.setText("Failed to fetch profile info.")