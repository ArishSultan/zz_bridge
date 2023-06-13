import re

from zk import ZK
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QGridLayout, QSpacerItem, \
    QPushButton, QErrorMessage, QMessageBox, QMainWindow

from .home import HomeWindow
from ..api import ZkAPI, ZohoAPI
from ..services import UsersService, AttendanceService


class ConnectorWindow(QWidget):
    _state = {
        'timeout': 5,
        'verbose': False,
        'password': 0,
        'encoding': 'UTF-8',
    }

    def __init__(self):
        super().__init__()

        connect_button = QPushButton('Connect')
        connect_button.setDefault(True)
        connect_button.clicked.connect(self.connect_clicked)

        self.ip_input = QLineEdit()
        self.port_input = QLineEdit()

        self.ip_input.setText('192.168.18.249')
        self.port_input.setText('4370')

        label1 = QLabel('Device IP:')
        label2 = QLabel('Port:')

        label1.setFixedWidth(60)
        label2.setFixedWidth(60)

        grid_layout = QGridLayout()
        grid_layout.addWidget(label1, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid_layout.addWidget(self.ip_input, 0, 1, 1, 2)

        grid_layout.addWidget(label2, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.port_input.setFixedWidth(70)
        grid_layout.addWidget(self.port_input, 1, 1, 1, 1)  # Span 1 column
        grid_layout.setColumnStretch(1, 1)

        force_udp_cb = QCheckBox('Force UDP')
        force_udp_cb.setChecked(False)
        force_udp_cb.stateChanged.connect(self.handle_force_udp_cb)

        omit_ping_cb = QCheckBox('Omit UDP')
        omit_ping_cb.setChecked(True)
        omit_ping_cb.stateChanged.connect(self.handle_omit_ping_cb)

        cb_layout = QHBoxLayout()
        cb_layout.addWidget(force_udp_cb)
        cb_layout.addWidget(omit_ping_cb)

        v_layout = QVBoxLayout()
        v_layout.setSpacing(10)
        v_layout.addLayout(grid_layout)
        v_layout.addSpacing(5)
        v_layout.addLayout(cb_layout)
        v_layout.addSpacing(20)
        v_layout.addWidget(connect_button)

        self.setFixedSize(250, 190)
        self.setWindowTitle('ZZ Bridge - Device Connection')
        self.setLayout(v_layout)
        self.home_window = None

    def handle_force_udp_cb(self, state):
        self._state['force_udp'] = state == Qt.CheckState.Checked

    def handle_omit_ping_cb(self, state):
        self._state['ommit_ping'] = state == Qt.CheckState.Checked

    def connect_clicked(self):
        try:
            self._state['ip'] = self.ip_input.text()
            self._state['port'] = int(self.port_input.text())

            zk_api = ZkAPI(**self._state)
            zoho_api = ZohoAPI()

            self.home_window = HomeWindow(UsersService(zk_api, zoho_api), AttendanceService(zk_api, zoho_api))
            self.home_window.show()
            self.hide()
        except Exception as ex:
            QMessageBox().critical(self, 'Unable to Connect', str(ex))
