from zk import const
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout


class AttendanceTab(QWidget):
    def __init__(self, attendance_service):
        super().__init__()
        self.attendance_service = attendance_service

        table = QTableWidget()
        table.setColumnCount(3)

        table.setHorizontalHeaderLabels(['User Id', 'Punch', 'Timestamp'])

        button = QPushButton('zoho sync')
        refresh = QPushButton('refresh')
        refresh.clicked.connect(self.refresh)

        actions = QHBoxLayout()
        actions.addWidget(button)
        actions.addWidget(refresh)

        layout = QVBoxLayout()
        layout.addLayout(actions)
        layout.addWidget(table)

        button.clicked.connect(self.sync_attendance)

        self.table = table
        self.setLayout(layout)
        self.refresh()

    def refresh(self):
        self.load_attendance()

    def load_attendance(self):
        attendance = self.attendance_service.get_device_attendance()
        self.table.setRowCount(len(attendance))
        for i in range(len(attendance)):
            self.table.setItem(i, 0, QTableWidgetItem(attendance[i].user_id))
            self.table.setItem(i, 1, QTableWidgetItem(AttendanceTab.resolve_status(attendance[i].punch)))
            self.table.setItem(i, 2, QTableWidgetItem(str(attendance[i].timestamp)))

        self.table.resizeColumnsToContents()
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

    @staticmethod
    def resolve_punch(punch):
        return 'Yes' if punch == 1 else 'No'

    @staticmethod
    def resolve_status(status):
        if status == 0:
            return 'Check In'
        elif status == 1:
            return 'Check Out'

    def sync_attendance(self):
        self.attendance_service.sync_to_zoho()
