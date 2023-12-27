import sys
import os

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QGuiApplication()
    engine = QQmlApplicationEngine()

    parent = os.path.dirname(__file__)
    qml_file = os.path.join(parent, 'view.qml')
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
