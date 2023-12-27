import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

if __name__ == "__main__":
    app = QApplication()
    view = QQuickView()

    parent = os.path.dirname(__file__)
    qml_path = os.path.join(parent, "view.qml")
    view.setSource(qml_path)

    view.show()
    sys.exit(app.exec())