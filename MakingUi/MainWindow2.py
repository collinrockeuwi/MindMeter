from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MainWindow # Import the class


#Top bar options
class MainWindow2:
    def __init__(self, parent, main_window):
        self.main_window = main_window
        self.setupMainWindow2page(parent)
        

    def setupMainWindow2page(self, parent):
        self.MainWindow_2 = QtWidgets.QWidget(self.main_window.MainWindow_grid_lyt)
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.MainWindow_2_verticalLayout = QtWidgets.QVBoxLayout(self.MainWindow_2)
        self.MainWindow_2_verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.MainWindow_2_verticalLayout.setObjectName("MainWindow_2_verticalLayout")
        self.topbar_widget = QtWidgets.QWidget(self.MainWindow_2)
        self.topbar_widget.setMinimumSize(QtCore.QSize(0, 61))
        self.topbar_widget.setMaximumSize(QtCore.QSize(16777215, 61))
        self.topbar_widget.setStyleSheet("QWidget{\n"
"\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    text-align: centre;\n"
"    height: 30px;\n"
"    border: none;\n"
"    \n"
"    border-radius: 5px; \n"
"    \n"
"    background-color: rgb(31, 149, 239); /* Normal background color */\n"
"    font-size: 14px; /* Set the font size here */\n"
"    /* Other styles */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(45, 45, 45); /* Darker background color on hover */\n"
"    color: rgb(220, 220, 220); /* Slightly lighter text color on hover */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
" \n"
"     background-color: rgb(45, 45, 45); /* Darker background color on checked */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    qproperty-alignment: AlignCenter; /* This will center the text */\n"
"}\n"
"\n"
"\n"
"")
        self.topbar_widget.setObjectName("topbar_widget")
        self.topbar_widget_gridLayout = QtWidgets.QGridLayout(self.topbar_widget)
        self.topbar_widget_gridLayout.setContentsMargins(3, 3, 3, 3)
        self.topbar_widget_gridLayout.setObjectName("topbar_widget_gridLayout")
        self.topbar_horizontalLayout = QtWidgets.QHBoxLayout()
        self.topbar_horizontalLayout.setObjectName("topbar_horizontalLayout")
        self.topbar_menu_button = QtWidgets.QPushButton(self.topbar_widget)
        self.topbar_menu_button.setMinimumSize(QtCore.QSize(50, 50))
        self.topbar_menu_button.setMaximumSize(QtCore.QSize(50, 50))
        self.topbar_menu_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/menu-4-32-white.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topbar_menu_button.setIcon(icon7)
        self.topbar_menu_button.setIconSize(QtCore.QSize(30, 30))
        self.topbar_menu_button.setCheckable(True)
        self.topbar_menu_button.setObjectName("topbar_menu_button")
        self.topbar_horizontalLayout.addWidget(self.topbar_menu_button)
        self.topbar_menu_button.setChecked(True)

      
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topbar_horizontalLayout.addItem(spacerItem3)
        self.topbar_widget_gridLayout.addLayout(self.topbar_horizontalLayout, 0, 0, 1, 1)
        self.MainWindow_2_verticalLayout.addWidget(self.topbar_widget)




