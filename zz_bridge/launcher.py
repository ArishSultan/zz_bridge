import sys

from PyQt6.QtWidgets import QApplication

from .ui import ConnectorWindow
from .api.zoho_api import ZohoAPI


def main():
    app = QApplication(sys.argv)

    window = ConnectorWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
