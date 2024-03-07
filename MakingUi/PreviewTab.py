from PyQt5 import QtCore, QtGui, QtWidgets        



class PreviewTab:
    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.setupPreviewPage(parent)
        

    def setupPreviewPage(self, parent):

        self.GE_Preview_Page = QtWidgets.QWidget()
        self.GE_Preview_Page.setObjectName("GE_Preview_Page")
        self.GE_Preview_Page_gridLayout = QtWidgets.QGridLayout(self.GE_Preview_Page)
        self.GE_Preview_Page_gridLayout.setObjectName("GE_Preview_Page_gridLayout")
        self.GE_Preview_Page_widget = QtWidgets.QWidget(self.GE_Preview_Page)
        self.GE_Preview_Page_widget.setObjectName("GE_Preview_Page_widget")
        self.GE_Preview_Page_widget_gridLayout_2 = QtWidgets.QGridLayout(self.GE_Preview_Page_widget)
        self.GE_Preview_Page_widget_gridLayout_2.setObjectName("GE_Preview_Page_widget_gridLayout_2")
        self.GE_StudentName_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_StudentName_Preview.setMinimumSize(QtCore.QSize(240, 80))
        self.GE_StudentName_Preview.setMaximumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_StudentName_Preview.setFont(font)
        self.GE_StudentName_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_StudentName_Preview.setObjectName("GE_StudentName_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_StudentName_Preview, 0, 0, 1, 1)
        self.GE_StudentName_Preview_Edit = QtWidgets.QLineEdit(self.GE_Preview_Page_widget)
        self.GE_StudentName_Preview_Edit.setMinimumSize(QtCore.QSize(400, 60))
        self.GE_StudentName_Preview_Edit.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_StudentName_Preview_Edit.setFont(font)
        self.GE_StudentName_Preview_Edit.setStyleSheet("QLineEdit {\n"
"    /* General styling */\n"
"    background-color: white; /* Background color of the line edit */\n"
"    color: black; /* Text color */\n"
"    border: 3px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 5px; /* Space between the text and the border */\n"
"    font-size: 16px; /* Font size */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    /* Styling when the line edit has focus */\n"
"    border-color: rgb(41, 159, 249); /* Change border color */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    /* Styling when the line edit is disabled */\n"
"    background-color: rgb(220, 220, 220); /* Lighter background */\n"
"    color: rgb(150, 150, 150); /* Lighter text color */\n"
"}\n"
"")
        self.GE_StudentName_Preview_Edit.setObjectName("GE_StudentName_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_StudentName_Preview_Edit, 0, 1, 1, 1)
        self.GE_Age_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_Age_Preview.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_Age_Preview.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Age_Preview.setFont(font)
        self.GE_Age_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Age_Preview.setObjectName("GE_Age_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_Age_Preview, 1, 0, 1, 1)
        self.GE_Age_Preview_Edit = QtWidgets.QSpinBox(self.GE_Preview_Page_widget)
        self.GE_Age_Preview_Edit.setMinimumSize(QtCore.QSize(90, 60))
        self.GE_Age_Preview_Edit.setMaximumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(20)
        self.GE_Age_Preview_Edit.setFont(font)
        self.GE_Age_Preview_Edit.setStyleSheet("QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"\n"
"    padding-left: 20px; /* Adjust left padding to center text */\n"
"  \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /* Styling for the up-button */\n"
"    subcontrol-origin: border; /* Position within the border */\n"
"    subcontrol-position: top right; /* Position at the top right */\n"
"    width: 15px; /* Width of the up-button */\n"
"    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /* Styling for the down-button */\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"    border-left: 1px solid black;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    /* Arrow styling within the up-button */\n"
"    width: 7px; /* Width of the arrow */\n"
"    height: 7px; /* Height of the arrow */\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    /* Arrow styling within the down-button */\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    /* Styling for the up-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    /* Styling for the down-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    /* Styling for the buttons when hovered */\n"
"    background-color: #e0e0e0;\n"
"}")
        self.GE_Age_Preview_Edit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.GE_Age_Preview_Edit.setMaximum(20)
        self.GE_Age_Preview_Edit.setObjectName("GE_Age_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_Age_Preview_Edit, 1, 1, 1, 1)
        self.GE_Sex_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_Sex_Preview.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_Sex_Preview.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Sex_Preview.setFont(font)
        self.GE_Sex_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Sex_Preview.setObjectName("GE_Sex_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_Sex_Preview, 2, 0, 1, 1)
        self.GE_Sex_Preview_Edit = QtWidgets.QLineEdit(self.GE_Preview_Page_widget)
        self.GE_Sex_Preview_Edit.setMinimumSize(QtCore.QSize(200, 60))
        self.GE_Sex_Preview_Edit.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_Sex_Preview_Edit.setFont(font)
        self.GE_Sex_Preview_Edit.setStyleSheet("QLineEdit {\n"
"    /* General styling */\n"
"    background-color: white; /* Background color of the line edit */\n"
"    color: black; /* Text color */\n"
"    border: 3px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 5px; /* Space between the text and the border */\n"
"    font-size: 16px; /* Font size */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    /* Styling when the line edit has focus */\n"
"    border-color: rgb(41, 159, 249); /* Change border color */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    /* Styling when the line edit is disabled */\n"
"    background-color: rgb(220, 220, 220); /* Lighter background */\n"
"    color: rgb(150, 150, 150); /* Lighter text color */\n"
"}\n"
"")
        self.GE_Sex_Preview_Edit.setObjectName("GE_Sex_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_Sex_Preview_Edit, 2, 1, 1, 1)
        self.GE_School_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_School_Preview.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_School_Preview.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_School_Preview.setFont(font)
        self.GE_School_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_School_Preview.setObjectName("GE_School_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_School_Preview, 3, 0, 1, 1)
        self.GE_School_Preview_Edit = QtWidgets.QLineEdit(self.GE_Preview_Page_widget)
        self.GE_School_Preview_Edit.setMinimumSize(QtCore.QSize(400, 60))
        self.GE_School_Preview_Edit.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_School_Preview_Edit.setFont(font)
        self.GE_School_Preview_Edit.setStyleSheet("QLineEdit {\n"
"    /* General styling */\n"
"    background-color: white; /* Background color of the line edit */\n"
"    color: black; /* Text color */\n"
"    border: 3px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 5px; /* Space between the text and the border */\n"
"    font-size: 16px; /* Font size */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    /* Styling when the line edit has focus */\n"
"    border-color: rgb(41, 159, 249); /* Change border color */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    /* Styling when the line edit is disabled */\n"
"    background-color: rgb(220, 220, 220); /* Lighter background */\n"
"    color: rgb(150, 150, 150); /* Lighter text color */\n"
"}\n"
"")
        self.GE_School_Preview_Edit.setObjectName("GE_School_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_School_Preview_Edit, 3, 1, 1, 1)
        self.GE_Date_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_Date_Preview.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_Date_Preview.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Date_Preview.setFont(font)
        self.GE_Date_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Date_Preview.setObjectName("GE_Date_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_Date_Preview, 4, 0, 1, 1)
        self.GE_Date_Preview_Edit = QtWidgets.QLineEdit(self.GE_Preview_Page_widget)
        self.GE_Date_Preview_Edit.setMinimumSize(QtCore.QSize(200, 60))
        self.GE_Date_Preview_Edit.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_Date_Preview_Edit.setFont(font)
        self.GE_Date_Preview_Edit.setStyleSheet("QLineEdit {\n"
"    /* General styling */\n"
"    background-color: white; /* Background color of the line edit */\n"
"    color: black; /* Text color */\n"
"    border: 3px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 25px; /* Rounded corners */\n"
"    padding: 5px; /* Space between the text and the border */\n"
"    font-size: 16px; /* Font size */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    /* Styling when the line edit has focus */\n"
"    border-color: rgb(41, 159, 249); /* Change border color */\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    /* Styling when the line edit is disabled */\n"
"    background-color: rgb(220, 220, 220); /* Lighter background */\n"
"    color: rgb(150, 150, 150); /* Lighter text color */\n"
"}\n"
"")
        self.GE_Date_Preview_Edit.setObjectName("GE_Date_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_Date_Preview_Edit, 4, 1, 1, 1)
        self.GE_StressTest_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_StressTest_Preview.setMinimumSize(QtCore.QSize(240, 80))
        self.GE_StressTest_Preview.setMaximumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_StressTest_Preview.setFont(font)
        self.GE_StressTest_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_StressTest_Preview.setObjectName("GE_StressTest_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_StressTest_Preview, 5, 0, 1, 1)
        self.GE_StressTest_Preview_Edit = QtWidgets.QSpinBox(self.GE_Preview_Page_widget)
        self.GE_StressTest_Preview_Edit.setMinimumSize(QtCore.QSize(90, 60))
        self.GE_StressTest_Preview_Edit.setMaximumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(20)
        self.GE_StressTest_Preview_Edit.setFont(font)
        self.GE_StressTest_Preview_Edit.setStyleSheet("QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"\n"
"    padding-left: 20px; /* Adjust left padding to center text */\n"
"  \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /* Styling for the up-button */\n"
"    subcontrol-origin: border; /* Position within the border */\n"
"    subcontrol-position: top right; /* Position at the top right */\n"
"    width: 15px; /* Width of the up-button */\n"
"    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /* Styling for the down-button */\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"    border-left: 1px solid black;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    /* Arrow styling within the up-button */\n"
"    width: 7px; /* Width of the arrow */\n"
"    height: 7px; /* Height of the arrow */\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    /* Arrow styling within the down-button */\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    /* Styling for the up-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    /* Styling for the down-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    /* Styling for the buttons when hovered */\n"
"    background-color: #e0e0e0;\n"
"}")
        self.GE_StressTest_Preview_Edit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.GE_StressTest_Preview_Edit.setMaximum(20)
        self.GE_StressTest_Preview_Edit.setObjectName("GE_StressTest_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_StressTest_Preview_Edit, 5, 1, 1, 1)
        self.GE_DepressionTest_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_DepressionTest_Preview.setMinimumSize(QtCore.QSize(240, 80))
        self.GE_DepressionTest_Preview.setMaximumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.GE_DepressionTest_Preview.setFont(font)
        self.GE_DepressionTest_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_DepressionTest_Preview.setObjectName("GE_DepressionTest_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_DepressionTest_Preview, 6, 0, 1, 1)
        self.GE_DepressionTest_Preview_Edit = QtWidgets.QSpinBox(self.GE_Preview_Page_widget)
        self.GE_DepressionTest_Preview_Edit.setMinimumSize(QtCore.QSize(90, 60))
        self.GE_DepressionTest_Preview_Edit.setMaximumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(20)
        self.GE_DepressionTest_Preview_Edit.setFont(font)
        self.GE_DepressionTest_Preview_Edit.setStyleSheet("QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"\n"
"    padding-left: 20px; /* Adjust left padding to center text */\n"
"  \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /* Styling for the up-button */\n"
"    subcontrol-origin: border; /* Position within the border */\n"
"    subcontrol-position: top right; /* Position at the top right */\n"
"    width: 15px; /* Width of the up-button */\n"
"    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /* Styling for the down-button */\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"    border-left: 1px solid black;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    /* Arrow styling within the up-button */\n"
"    width: 7px; /* Width of the arrow */\n"
"    height: 7px; /* Height of the arrow */\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    /* Arrow styling within the down-button */\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    /* Styling for the up-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    /* Styling for the down-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    /* Styling for the buttons when hovered */\n"
"    background-color: #e0e0e0;\n"
"}")
        self.GE_DepressionTest_Preview_Edit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.GE_DepressionTest_Preview_Edit.setMaximum(20)
        self.GE_DepressionTest_Preview_Edit.setObjectName("GE_DepressionTest_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_DepressionTest_Preview_Edit, 6, 1, 1, 1)
        self.GE_SelfEsteemTest_Preview = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.GE_SelfEsteemTest_Preview.setMinimumSize(QtCore.QSize(240, 80))
        self.GE_SelfEsteemTest_Preview.setMaximumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.GE_SelfEsteemTest_Preview.setFont(font)
        self.GE_SelfEsteemTest_Preview.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_SelfEsteemTest_Preview.setObjectName("GE_SelfEsteemTest_Preview")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_SelfEsteemTest_Preview, 7, 0, 1, 1)
        self.GE_SelfEsteemTest_Preview_Edit = QtWidgets.QSpinBox(self.GE_Preview_Page_widget)
        self.GE_SelfEsteemTest_Preview_Edit.setMinimumSize(QtCore.QSize(90, 60))
        self.GE_SelfEsteemTest_Preview_Edit.setMaximumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(20)
        self.GE_SelfEsteemTest_Preview_Edit.setFont(font)
        self.GE_SelfEsteemTest_Preview_Edit.setStyleSheet("QSpinBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"\n"
"    padding-left: 20px; /* Adjust left padding to center text */\n"
"  \n"
"    margin: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    /* Styling for the up-button */\n"
"    subcontrol-origin: border; /* Position within the border */\n"
"    subcontrol-position: top right; /* Position at the top right */\n"
"    width: 15px; /* Width of the up-button */\n"
"    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    /* Styling for the down-button */\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"    border-left: 1px solid black;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    /* Arrow styling within the up-button */\n"
"    width: 7px; /* Width of the arrow */\n"
"    height: 7px; /* Height of the arrow */\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    /* Arrow styling within the down-button */\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    /* Styling for the up-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    /* Styling for the down-button when pressed */\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    /* Styling for the buttons when hovered */\n"
"    background-color: #e0e0e0;\n"
"}")
        self.GE_SelfEsteemTest_Preview_Edit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.GE_SelfEsteemTest_Preview_Edit.setMaximum(20)
        self.GE_SelfEsteemTest_Preview_Edit.setObjectName("GE_SelfEsteemTest_Preview_Edit")
        self.GE_Preview_Page_widget_gridLayout_2.addWidget(self.GE_SelfEsteemTest_Preview_Edit, 7, 1, 1, 1)
        self.GE_Preview_Page_gridLayout.addWidget(self.GE_Preview_Page_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.GE_Preview_Page)


