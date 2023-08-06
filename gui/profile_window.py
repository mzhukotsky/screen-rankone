from PyQt6.QtWidgets import QLabel, QVBoxLayout, QDialog, QTableWidget, QTableWidgetItem
from utils.rankone_api import get_profile_events

class ProfileWindow(QDialog):
    def __init__(self, profile_name):
        super().__init__()
        self.setWindowTitle('Profile')
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        self.profile_name_label = QLabel(f"Profile Name: {profile_name}", self)
        layout.addWidget(self.profile_name_label)

        self.events_label = QLabel("Profile Events:", self)
        layout.addWidget(self.events_label)

        # Create a QTableWidget to display events
        self.events_table = QTableWidget(self)
        layout.addWidget(self.events_table)

        self.setLayout(layout)

        # Fetch and display the events
        self.populate_events(profile_name)

    def populate_events(self, profile_name):
        events_data = get_profile_events(profile_name)
        if events_data and isinstance(events_data, list):
            if len(events_data) > 0:
                self.events_table.setRowCount(len(events_data))
                self.events_table.setColumnCount(len(events_data[0]))

                for row_idx, event in enumerate(events_data):
                    for col_idx, (key, value) in enumerate(event.items()):
                        item = QTableWidgetItem(str(value))
                        self.events_table.setItem(row_idx, col_idx, item)
            else:
                self.events_label.setText("No events found.")
        else:
            self.events_label.setText("Failed to fetch profile events.")