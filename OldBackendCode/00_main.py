import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from database import init_db

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
