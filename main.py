import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

import rc_resources

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    app.setWindowIcon(QIcon(":/images/logo.png"))
    engine.load(":/qml/main.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
