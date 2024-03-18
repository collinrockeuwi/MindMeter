from PyQt5 import QtCore, QtGui, QtWidgets        
from GeneralTab import GeneralTab  # Import the GeneralTab class


class PreviewTab(QtCore.QObject):
    def __init__(self, parent, stackedWidget, generalTabInstance):
        self.stackedWidget = stackedWidget
        self.setupPreviewPage(parent)
        # Connect the GeneralTab signal to the updatePreview method
        generalTabInstance.generalInfoSaved.connect(self.updatePreview)
        print("Signal connected to updatePreview")

    def setupPreviewPage(self, parent):

        self.GE_Preview_Page = QtWidgets.QWidget()
        self.GE_Preview_Page.setObjectName("GE_Preview_Page")
        self.GE_Preview_Page_gridLayout = QtWidgets.QGridLayout(self.GE_Preview_Page)
        self.GE_Preview_Page_gridLayout.setObjectName("GE_Preview_Page_gridLayout")
        self.GE_Preview_Page_widget = QtWidgets.QWidget(self.GE_Preview_Page)
        self.GE_Preview_Page_widget.setStyleSheet("QLabel {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    color: white; /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#preview_instructions, #preview_date_instructions {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: rgb(24, 45, 83 ); /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#PreviewTabTitle_label {\n"
"    font-family: \'Roboto Cn\'; /* Specify the font family */\n"
"    font-size: 100px; /* Specify the font size */\n"
"    font-weight: bold; /* Make the font bold */\n"
"    color: white; /* Set the font color */\n"
"   border: 3px solid  rgb(24, 45, 83 ); /* This adds a 3px solid blue border around the name_widget */\n"
"    background-color: rgb(24, 45, 83 );\n"
"    border-radius: 20px; /* Optional: if you want rounded corners */\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#preview_name_widget, #preview_school_widget, #preview_gender_widget, #preview_dates_widget   {\n"
"    color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"    border: 3px solid rgb(24, 45, 83); /* This adds a 3px solid blue border */\n"
"    background-color: rgb(31, 149, 239);\n"
"    border-radius: 40px; /* Optional: if you want rounded corners */\n"
"}\n"
"\n"
"Line { /* This applies to all Line objects within the name_widget */\n"
"    background-color: rgb(24, 45, 83 ); /* Change the color of the line */\n"
"   \n"
"}\n"
"\n"
"/*background-color: rgb(31, 149, 239);*/\n"
"\n"
"QLineEdit {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto Cn\';\n"
"    color: rgb(24, 45, 83 ); /* Text color */\n"
"    font-size: 25px; /* Font size */\n"
"    border: 2px solid  rgb(24, 45, 83 ); /* This adds a 3px solid blue border around the name_widget */\n"
"    background-color: white;\n"
"    border-radius: 10px; /* Optional: if you want rounded corners */\n"
"    padding-left: 15px; /* Space between the text and the left margin */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 100px; /* Width of the indicator */\n"
"    height: 100px; /* Height of the indicator */\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(:/icon/icon/tickhere.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(:/icon/icon/tickmark.png); /* Absolute path to the checkmark image */\n"
"    \n"
"}\n"
"\n"
"QDateEdit {\n"
"/* General styling for the checkbox */\n"
"    font-family: \'Roboto Cn\';\n"
"    color: rgb(24, 45, 83 ); /* Text color */\n"
"    font-size: 25px; /* Font size */\n"
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
"\n"
"\n"
"#preview_savebutton {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#preview_savebutton::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 150px; /* Width of the indicator */\n"
"    height: 150px; /* Height of the indicator */\n"
"}\n"
"\n"
"#preview_savebutton::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(C:/Users/colli/Downloads/MakingUi/icon/notsaved.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"#preview_savebutton::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(C:/Users/colli/Downloads/MakingUi/icon/saved.png); /* Absolute path to the checkmark image */\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.GE_Preview_Page_widget.setObjectName("GE_Preview_Page_widget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.GE_Preview_Page_widget)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.TitleLayout_2 = QtWidgets.QHBoxLayout()
        self.TitleLayout_2.setObjectName("TitleLayout_2")
        spacerItem116 = QtWidgets.QSpacerItem(50, 97, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.TitleLayout_2.addItem(spacerItem116)
        self.PreviewTabTitle_label = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.PreviewTabTitle_label.setMinimumSize(QtCore.QSize(830, 100))
        self.PreviewTabTitle_label.setMaximumSize(QtCore.QSize(830, 100))
        self.PreviewTabTitle_label.setObjectName("PreviewTabTitle_label")
        self.TitleLayout_2.addWidget(self.PreviewTabTitle_label)
        spacerItem117 = QtWidgets.QSpacerItem(50, 97, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.TitleLayout_2.addItem(spacerItem117)
        self.gridLayout_14.addLayout(self.TitleLayout_2, 0, 0, 1, 1)
        self.preview_instructions = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.preview_instructions.setMinimumSize(QtCore.QSize(1168, 60))
        self.preview_instructions.setMaximumSize(QtCore.QSize(1168, 60))
        self.preview_instructions.setObjectName("preview_instructions")
        self.gridLayout_14.addWidget(self.preview_instructions, 1, 0, 1, 1)
        self.input_area_verical_lyt_2 = QtWidgets.QVBoxLayout()
        self.input_area_verical_lyt_2.setSpacing(30)
        self.input_area_verical_lyt_2.setObjectName("input_area_verical_lyt_2")
        self.preview_name_widget = QtWidgets.QWidget(self.GE_Preview_Page_widget)
        self.preview_name_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.preview_name_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.preview_name_widget.setStyleSheet("")
        self.preview_name_widget.setObjectName("preview_name_widget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.preview_name_widget)
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem118 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem118)
        self.preview_name_label = QtWidgets.QLabel(self.preview_name_widget)
        self.preview_name_label.setMinimumSize(QtCore.QSize(260, 50))
        self.preview_name_label.setMaximumSize(QtCore.QSize(260, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_name_label.setFont(font)
        self.preview_name_label.setStyleSheet("")
        self.preview_name_label.setObjectName("preview_name_label")
        self.horizontalLayout_9.addWidget(self.preview_name_label)
        spacerItem119 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem119)
        self.preview_name_display = QtWidgets.QLineEdit(self.preview_name_widget)
        self.preview_name_display.setMinimumSize(QtCore.QSize(300, 50))
        self.preview_name_display.setMaximumSize(QtCore.QSize(300, 50))
        self.preview_name_display.setText("")
        self.preview_name_display.setObjectName("preview_name_display")
        self.horizontalLayout_9.addWidget(self.preview_name_display)
        spacerItem120 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem120)
        self.name_vertical_line_6 = QtWidgets.QFrame(self.preview_name_widget)
        self.name_vertical_line_6.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_6.setObjectName("name_vertical_line_6")
        self.horizontalLayout_9.addWidget(self.name_vertical_line_6)
        spacerItem121 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem121)
        self.preview_school_label = QtWidgets.QLabel(self.preview_name_widget)
        self.preview_school_label.setMinimumSize(QtCore.QSize(100, 50))
        self.preview_school_label.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_school_label.setFont(font)
        self.preview_school_label.setStyleSheet("")
        self.preview_school_label.setObjectName("preview_school_label")
        self.horizontalLayout_9.addWidget(self.preview_school_label)
        spacerItem122 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem122)
        self.preview_school_display = QtWidgets.QLineEdit(self.preview_name_widget)
        self.preview_school_display.setMinimumSize(QtCore.QSize(300, 50))
        self.preview_school_display.setMaximumSize(QtCore.QSize(300, 50))
        self.preview_school_display.setText("")
        self.preview_school_display.setObjectName("preview_school_display")
        self.horizontalLayout_9.addWidget(self.preview_school_display)
        spacerItem123 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem123)
        self.gridLayout_10.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.input_area_verical_lyt_2.addWidget(self.preview_name_widget)
        self.preview_gender_widget = QtWidgets.QWidget(self.GE_Preview_Page_widget)
        self.preview_gender_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.preview_gender_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.preview_gender_widget.setStyleSheet("")
        self.preview_gender_widget.setObjectName("preview_gender_widget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.preview_gender_widget)
        self.gridLayout_12.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_12.setSpacing(5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem124 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem124)
        self.preview_gender_label = QtWidgets.QLabel(self.preview_gender_widget)
        self.preview_gender_label.setMinimumSize(QtCore.QSize(110, 50))
        self.preview_gender_label.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_gender_label.setFont(font)
        self.preview_gender_label.setStyleSheet("")
        self.preview_gender_label.setObjectName("preview_gender_label")
        self.horizontalLayout_11.addWidget(self.preview_gender_label)
        spacerItem125 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem125)
        self.name_vertical_line_14 = QtWidgets.QFrame(self.preview_gender_widget)
        self.name_vertical_line_14.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_14.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_14.setObjectName("name_vertical_line_14")
        self.horizontalLayout_11.addWidget(self.name_vertical_line_14)
        spacerItem126 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem126)
        self.preview_gender_display = QtWidgets.QLineEdit(self.preview_gender_widget)
        self.preview_gender_display.setMinimumSize(QtCore.QSize(150, 50))
        self.preview_gender_display.setMaximumSize(QtCore.QSize(150, 50))
        self.preview_gender_display.setText("")
        self.preview_gender_display.setObjectName("preview_gender_display")
        self.horizontalLayout_11.addWidget(self.preview_gender_display)
        spacerItem127 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem127)
        self.gridLayout_12.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.input_area_verical_lyt_2.addWidget(self.preview_gender_widget)
        self.preview_date_instructions = QtWidgets.QLabel(self.GE_Preview_Page_widget)
        self.preview_date_instructions.setMinimumSize(QtCore.QSize(1168, 30))
        self.preview_date_instructions.setMaximumSize(QtCore.QSize(1168, 30))
        self.preview_date_instructions.setObjectName("preview_date_instructions")
        self.input_area_verical_lyt_2.addWidget(self.preview_date_instructions)
        self.preview_dates_widget = QtWidgets.QWidget(self.GE_Preview_Page_widget)
        self.preview_dates_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.preview_dates_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.preview_dates_widget.setStyleSheet("")
        self.preview_dates_widget.setObjectName("preview_dates_widget")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.preview_dates_widget)
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_13.setSpacing(5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.preview_dateofBirth_label_2 = QtWidgets.QLabel(self.preview_dates_widget)
        self.preview_dateofBirth_label_2.setMinimumSize(QtCore.QSize(175, 50))
        self.preview_dateofBirth_label_2.setMaximumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_dateofBirth_label_2.setFont(font)
        self.preview_dateofBirth_label_2.setStyleSheet("")
        self.preview_dateofBirth_label_2.setObjectName("preview_dateofBirth_label_2")
        self.horizontalLayout_12.addWidget(self.preview_dateofBirth_label_2)
        self.preview_dateofBirth_display = QtWidgets.QLineEdit(self.preview_dates_widget)
        self.preview_dateofBirth_display.setMinimumSize(QtCore.QSize(150, 50))
        self.preview_dateofBirth_display.setMaximumSize(QtCore.QSize(150, 50))
        self.preview_dateofBirth_display.setText("")
        self.preview_dateofBirth_display.setObjectName("preview_dateofBirth_display")
        self.horizontalLayout_12.addWidget(self.preview_dateofBirth_display)
        self.name_vertical_line_16 = QtWidgets.QFrame(self.preview_dates_widget)
        self.name_vertical_line_16.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_16.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_16.setObjectName("name_vertical_line_16")
        self.horizontalLayout_12.addWidget(self.name_vertical_line_16)
        spacerItem128 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem128)
        self.preview_todaysdate_label = QtWidgets.QLabel(self.preview_dates_widget)
        self.preview_todaysdate_label.setMinimumSize(QtCore.QSize(177, 50))
        self.preview_todaysdate_label.setMaximumSize(QtCore.QSize(177, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_todaysdate_label.setFont(font)
        self.preview_todaysdate_label.setStyleSheet("")
        self.preview_todaysdate_label.setObjectName("preview_todaysdate_label")
        self.horizontalLayout_12.addWidget(self.preview_todaysdate_label)
        self.preview_todaysdate_display = QtWidgets.QLineEdit(self.preview_dates_widget)
        self.preview_todaysdate_display.setMinimumSize(QtCore.QSize(150, 50))
        self.preview_todaysdate_display.setMaximumSize(QtCore.QSize(150, 50))
        self.preview_todaysdate_display.setText("")
        self.preview_todaysdate_display.setObjectName("preview_todaysdate_display")
        self.horizontalLayout_12.addWidget(self.preview_todaysdate_display)
        self.gridLayout_13.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.input_area_verical_lyt_2.addWidget(self.preview_dates_widget)
        self.preview_school_widget = QtWidgets.QWidget(self.GE_Preview_Page_widget)
        self.preview_school_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.preview_school_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.preview_school_widget.setStyleSheet("")
        self.preview_school_widget.setObjectName("preview_school_widget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.preview_school_widget)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_11.setSpacing(5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem129 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem129)
        self.preview_stress_label = QtWidgets.QLabel(self.preview_school_widget)
        self.preview_stress_label.setMinimumSize(QtCore.QSize(100, 50))
        self.preview_stress_label.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_stress_label.setFont(font)
        self.preview_stress_label.setStyleSheet("")
        self.preview_stress_label.setObjectName("preview_stress_label")
        self.horizontalLayout_10.addWidget(self.preview_stress_label)
        spacerItem130 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem130)
        self.preview_stress_display = QtWidgets.QLineEdit(self.preview_school_widget)
        self.preview_stress_display.setMinimumSize(QtCore.QSize(65, 50))
        self.preview_stress_display.setMaximumSize(QtCore.QSize(150, 50))
        self.preview_stress_display.setText("")
        self.preview_stress_display.setObjectName("preview_stress_display")
        self.horizontalLayout_10.addWidget(self.preview_stress_display)
        spacerItem131 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem131)
        self.name_vertical_line_18 = QtWidgets.QFrame(self.preview_school_widget)
        self.name_vertical_line_18.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_18.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_18.setObjectName("name_vertical_line_18")
        self.horizontalLayout_10.addWidget(self.name_vertical_line_18)
        spacerItem132 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem132)
        self.preview_depression_label = QtWidgets.QLabel(self.preview_school_widget)
        self.preview_depression_label.setMinimumSize(QtCore.QSize(165, 50))
        self.preview_depression_label.setMaximumSize(QtCore.QSize(165, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_depression_label.setFont(font)
        self.preview_depression_label.setStyleSheet("")
        self.preview_depression_label.setObjectName("preview_depression_label")
        self.horizontalLayout_10.addWidget(self.preview_depression_label)
        spacerItem133 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem133)
        self.preview_depression_display = QtWidgets.QLineEdit(self.preview_school_widget)
        self.preview_depression_display.setMinimumSize(QtCore.QSize(65, 50))
        self.preview_depression_display.setMaximumSize(QtCore.QSize(150, 50))
        self.preview_depression_display.setText("")
        self.preview_depression_display.setObjectName("preview_depression_display")
        self.horizontalLayout_10.addWidget(self.preview_depression_display)
        spacerItem134 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem134)
        self.name_vertical_line_13 = QtWidgets.QFrame(self.preview_school_widget)
        self.name_vertical_line_13.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_13.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_13.setObjectName("name_vertical_line_13")
        self.horizontalLayout_10.addWidget(self.name_vertical_line_13)
        spacerItem135 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem135)
        self.preview_selfEsteem_label = QtWidgets.QLabel(self.preview_school_widget)
        self.preview_selfEsteem_label.setMinimumSize(QtCore.QSize(165, 50))
        self.preview_selfEsteem_label.setMaximumSize(QtCore.QSize(165, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.preview_selfEsteem_label.setFont(font)
        self.preview_selfEsteem_label.setStyleSheet("")
        self.preview_selfEsteem_label.setObjectName("preview_selfEsteem_label")
        self.horizontalLayout_10.addWidget(self.preview_selfEsteem_label)
        spacerItem136 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem136)
        self.preview_selfEsteem_display = QtWidgets.QLineEdit(self.preview_school_widget)
        self.preview_selfEsteem_display.setMinimumSize(QtCore.QSize(65, 50))
        self.preview_selfEsteem_display.setMaximumSize(QtCore.QSize(150, 50))
        self.preview_selfEsteem_display.setText("")
        self.preview_selfEsteem_display.setObjectName("preview_selfEsteem_display")
        self.horizontalLayout_10.addWidget(self.preview_selfEsteem_display)
        spacerItem137 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem137)
        self.gridLayout_11.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.input_area_verical_lyt_2.addWidget(self.preview_school_widget)
        self.gridLayout_14.addLayout(self.input_area_verical_lyt_2, 2, 0, 1, 1)
        self.preview_savebutton = QtWidgets.QCheckBox(self.GE_Preview_Page_widget)
        self.preview_savebutton.setMinimumSize(QtCore.QSize(150, 80))
        self.preview_savebutton.setMaximumSize(QtCore.QSize(150, 80))
        self.preview_savebutton.setText("")
        self.preview_savebutton.setIconSize(QtCore.QSize(100, 100))
        self.preview_savebutton.setObjectName("preview_savebutton")
        self.gridLayout_14.addWidget(self.preview_savebutton, 3, 0, 1, 1)
        self.GE_Preview_Page_gridLayout.addWidget(self.GE_Preview_Page_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.GE_Preview_Page)

    def updatePreview(self, general_info):
            print("Received General Info:", general_info)  # Print the received general information
            # Update the preview displays with the received information
            # Update the preview displays with the received information
            self.preview_name_display.setText(general_info['name'])
            self.preview_school_display.setText(general_info['school'])
            self.preview_gender_display.setText(general_info['gender'])
            self.preview_dateofBirth_display.setText(general_info['date_of_birth'])
            self.preview_todaysdate_display.setText(general_info['todays_date'])

   