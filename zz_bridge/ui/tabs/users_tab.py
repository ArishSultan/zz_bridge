from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem


class UsersTab(QWidget):
    def __init__(self, users_service):
        super().__init__()

        self.users_service = users_service

        table = QTableWidget()
        table.setColumnCount(2)

        table.setHorizontalHeaderLabels(['Id', 'Name'])

        sync_btn = QPushButton('resync')
        sync_btn.clicked.connect(self.sync)

        layout = QVBoxLayout()
        layout.addWidget(sync_btn)
        layout.addWidget(table)

        self.table = table
        self.setLayout(layout)

        self.load_users()

    def sync(self):
        self.users_service.sync_to_device()
        self.load_users()

    def load_users(self):
        users = self.users_service.get_device_users()
        self.table.setRowCount(len(users))
        for i in range(len(users)):
            self.table.setItem(i, 0, QTableWidgetItem(users[i].user_id))
            self.table.setItem(i, 1, QTableWidgetItem(users[i].name))

        self.table.resizeColumnsToContents()
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
