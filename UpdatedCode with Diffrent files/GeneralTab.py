from PyQt5 import QtCore, QtGui, QtWidgets        



class GeneralTab:
    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.setupGeneralPage(parent)
        

    def setupGeneralPage(self, parent):
                
        self.General_Page = QtWidgets.QWidget()
        self.General_Page.setObjectName("General_Page")
        self.General_Page_gridLayout = QtWidgets.QGridLayout(self.General_Page)
        self.General_Page_gridLayout.setObjectName("General_Page_gridLayout")
        self.GE_widget = QtWidgets.QWidget(self.General_Page)
        self.GE_widget.setObjectName("GE_widget")
        self.GE_widget_gridLayout = QtWidgets.QGridLayout(self.GE_widget)
        self.GE_widget_gridLayout.setContentsMargins(0, -1, -1, -1)
        self.GE_widget_gridLayout.setSpacing(100)
        self.GE_widget_gridLayout.setObjectName("GE_widget_gridLayout")
        self.GE_gridLayout = QtWidgets.QGridLayout()
        self.GE_gridLayout.setObjectName("GE_gridLayout")
        self.GE_Student_Label = QtWidgets.QLabel(self.GE_widget)
        self.GE_Student_Label.setMinimumSize(QtCore.QSize(240, 80))
        self.GE_Student_Label.setMaximumSize(QtCore.QSize(240, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Student_Label.setFont(font)
        self.GE_Student_Label.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Student_Label.setObjectName("GE_Student_Label")
        self.GE_gridLayout.addWidget(self.GE_Student_Label, 0, 0, 1, 1)
        self.GE_Student_Edit = QtWidgets.QLineEdit(self.GE_widget)
        self.GE_Student_Edit.setMinimumSize(QtCore.QSize(400, 60))
        self.GE_Student_Edit.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_Student_Edit.setFont(font)
        self.GE_Student_Edit.setStyleSheet("QLineEdit {\n"
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
        self.GE_Student_Edit.setObjectName("GE_Student_Edit")
        self.GE_gridLayout.addWidget(self.GE_Student_Edit, 0, 1, 1, 1)
        self.GE_Age_Label = QtWidgets.QLabel(self.GE_widget)
        self.GE_Age_Label.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_Age_Label.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Age_Label.setFont(font)
        self.GE_Age_Label.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Age_Label.setObjectName("GE_Age_Label")
        self.GE_gridLayout.addWidget(self.GE_Age_Label, 1, 0, 1, 1)
        self.GE_Age_Edit = QtWidgets.QLineEdit(self.GE_widget)
        self.GE_Age_Edit.setMinimumSize(QtCore.QSize(400, 60))
        self.GE_Age_Edit.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_Age_Edit.setFont(font)
        self.GE_Age_Edit.setStyleSheet("QLineEdit {\n"
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
        self.GE_Age_Edit.setObjectName("GE_Age_Edit")
        self.GE_gridLayout.addWidget(self.GE_Age_Edit, 1, 1, 1, 1)
        self.GE_Sex_Label = QtWidgets.QLabel(self.GE_widget)
        self.GE_Sex_Label.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_Sex_Label.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Sex_Label.setFont(font)
        self.GE_Sex_Label.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Sex_Label.setObjectName("GE_Sex_Label")
        self.GE_gridLayout.addWidget(self.GE_Sex_Label, 2, 0, 1, 1)
        self.GE_Age_Edit_2 = QtWidgets.QWidget(self.GE_widget)
        self.GE_Age_Edit_2.setMinimumSize(QtCore.QSize(400, 75))
        self.GE_Age_Edit_2.setMaximumSize(QtCore.QSize(400, 75))
        self.GE_Age_Edit_2.setStyleSheet("QRadioButton {\n"
"    /* General styling for the radio button */\n"
"    color: black;\n"
"; /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    /* Styling for the indicator (the circular part) */\n"
"    width: 20px; /* Width of the indicator */\n"
"    height: 20px; /* Height of the indicator */\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    /* Styling for the indicator when the radio button is unchecked */\n"
"    background-color: white; /* Background color */\n"
"    border: 2px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 10px; /* Makes the indicator circular */\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    /* Styling for the indicator when the radio button is checked */\n"
"    background-color: rgb(31, 149, 239); /* Background color */\n"
"    border: 2px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 10px; /* Makes the indicator circular */\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: rgb(245, 250, 254); /* Set the background color */\n"
"\n"
"\n"
"\n"
"    border: 2px solid rgb(0, 0, 0); /* Set the border color and width */\n"
"    border-radius: 20px; /* Set the border radius for rounded corners */\n"
"    padding: 10px; /* Set the padding inside the widget */\n"
"    margin: 5px; /* Set the margin outside the widget */\n"
"}\n"
"\n"
"")
        self.GE_Age_Edit_2.setObjectName("GE_Age_Edit_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.GE_Age_Edit_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.mf_horizontalLayout = QtWidgets.QHBoxLayout()
        self.mf_horizontalLayout.setObjectName("mf_horizontalLayout")
        self.GE_Sex_Male = QtWidgets.QRadioButton(self.GE_Age_Edit_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Sex_Male.setFont(font)
        self.GE_Sex_Male.setStyleSheet("QRadioButton {\n"
"    /* General styling for the radio button */\n"
"    color: black;\n"
"; /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    /* Styling for the indicator (the circular part) */\n"
"    width: 20px; /* Width of the indicator */\n"
"    height: 20px; /* Height of the indicator */\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    /* Styling for the indicator when the radio button is unchecked */\n"
"    background-color: white; /* Background color */\n"
"    border: 2px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 10px; /* Makes the indicator circular */\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    /* Styling for the indicator when the radio button is checked */\n"
"    background-color: rgb(31, 149, 239); /* Background color */\n"
"    border: 2px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 10px; /* Makes the indicator circular */\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: rgb(245, 250, 254);; /* Set the background color */\n"
"    border: 2px solid rgb(0, 0, 0); /* Set the border color and width */\n"
"    border-radius: 10px; /* Set the border radius for rounded corners */\n"
"    padding: 10px; /* Set the padding inside the widget */\n"
"    margin: 5px; /* Set the margin outside the widget */\n"
"}\n"
"\n"
"")
        self.GE_Sex_Male.setObjectName("GE_Sex_Male")
        self.mf_horizontalLayout.addWidget(self.GE_Sex_Male)
        self.GE_Female_Edit = QtWidgets.QRadioButton(self.GE_Age_Edit_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Female_Edit.setFont(font)
        self.GE_Female_Edit.setStyleSheet("QRadioButton {\n"
"    /* General styling for the radio button */\n"
"    color: black;\n"
"; /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    /* Styling for the indicator (the circular part) */\n"
"    width: 20px; /* Width of the indicator */\n"
"    height: 20px; /* Height of the indicator */\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    /* Styling for the indicator when the radio button is unchecked */\n"
"    background-color: white; /* Background color */\n"
"    border: 2px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 10px; /* Makes the indicator circular */\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    /* Styling for the indicator when the radio button is checked */\n"
"    background-color: rgb(31, 149, 239); /* Background color */\n"
"    border: 2px solid rgb(31, 149, 239); /* Border color and width */\n"
"    border-radius: 10px; /* Makes the indicator circular */\n"
"}\n"
"\n"
"QWidget {\n"
"   background-color: rgb(245, 250, 254); /* Set the background color */\n"
"    border: 2px solid rgb(0, 0, 0); /* Set the border color and width */\n"
"    border-radius: 10px; /* Set the border radius for rounded corners */\n"
"    padding: 10px; /* Set the padding inside the widget */\n"
"    margin: 5px; /* Set the margin outside the widget */\n"
"}\n"
"\n"
"")
        self.GE_Female_Edit.setObjectName("GE_Female_Edit")
        self.mf_horizontalLayout.addWidget(self.GE_Female_Edit)
        self.gridLayout_12.addLayout(self.mf_horizontalLayout, 0, 0, 1, 1)
        self.GE_gridLayout.addWidget(self.GE_Age_Edit_2, 2, 1, 1, 1)
        self.GE_School_Label = QtWidgets.QLabel(self.GE_widget)
        self.GE_School_Label.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_School_Label.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_School_Label.setFont(font)
        self.GE_School_Label.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_School_Label.setObjectName("GE_School_Label")
        self.GE_gridLayout.addWidget(self.GE_School_Label, 3, 0, 1, 1)
        self.GE_School_Edit = QtWidgets.QLineEdit(self.GE_widget)
        self.GE_School_Edit.setMinimumSize(QtCore.QSize(400, 60))
        self.GE_School_Edit.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.GE_School_Edit.setFont(font)
        self.GE_School_Edit.setStyleSheet("QLineEdit {\n"
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
        self.GE_School_Edit.setObjectName("GE_School_Edit")
        self.GE_gridLayout.addWidget(self.GE_School_Edit, 3, 1, 1, 1)
        self.GE_Date_Label = QtWidgets.QLabel(self.GE_widget)
        self.GE_Date_Label.setMinimumSize(QtCore.QSize(240, 60))
        self.GE_Date_Label.setMaximumSize(QtCore.QSize(240, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GE_Date_Label.setFont(font)
        self.GE_Date_Label.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 25px; /* Optional: if you want rounded corners */\n"
"}\n"
"")
        self.GE_Date_Label.setObjectName("GE_Date_Label")
        self.GE_gridLayout.addWidget(self.GE_Date_Label, 4, 0, 1, 1)
        self.GE_Date_Edit = QtWidgets.QDateEdit(self.GE_widget)
        self.GE_Date_Edit.setMinimumSize(QtCore.QSize(400, 60))
        self.GE_Date_Edit.setMaximumSize(QtCore.QSize(400, 60))
        self.GE_Date_Edit.setStyleSheet("QDateEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    padding-left: 20px; /* Adjust left padding to center text */\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QDateEdit::up-button, QDateEdit::down-button {\n"
"    subcontrol-origin: border;\n"
"    width: 15px;\n"
"    border-left: 1px solid black;\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    subcontrol-position: top right;\n"
"    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QDateEdit::up-arrow, QDateEdit::down-arrow {\n"
"    width: 7px;\n"
"    height: 7px;\n"
"    image: url(:/icon/icon/menu-4-32.ico);\n"
"}\n"
"\n"
"QDateEdit::up-button:pressed, QDateEdit::down-button:pressed {\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QDateEdit::up-button:hover, QDateEdit::down-button:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"")
        self.GE_Date_Edit.setObjectName("GE_Date_Edit")
        self.GE_gridLayout.addWidget(self.GE_Date_Edit, 4, 1, 1, 1)
        self.GE_widget_gridLayout.addLayout(self.GE_gridLayout, 0, 0, 1, 1)
        self.General_Page_gridLayout.addWidget(self.GE_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.General_Page)
               