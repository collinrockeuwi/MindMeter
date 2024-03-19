from PyQt5 import QtCore, QtGui, QtWidgets        



class GeneralTab:
    

    
    def __init__(self, shared_data, stackedWidget, previewTab):
        self.stackedWidget = stackedWidget
        self.shared_data = shared_data
        self.previewTab = previewTab  # Store the PreviewTab instance
        self.setupGeneralPage()
        
         # Set all checkboxes to unchecked
        self.name_checkBox.setChecked(False)
        self.school_checkBox.setChecked(False)
        self.male_checkBox.setChecked(False)
        self.female_checkBox.setChecked(False)
        self.dateofBirth_checkBox.setChecked(False)
        self.todaysDate_checkBox.setChecked(False)
        self.general_savebutton.setChecked(False)

        

        # Connect the stateChanged signal of the gender checkboxes to the handler
        self.male_checkBox.stateChanged.connect(lambda state: self.handleGenderCheckboxStateChange(state, self.male_checkBox))
        self.female_checkBox.stateChanged.connect(lambda state: self.handleGenderCheckboxStateChange(state, self.female_checkBox))

#not ui
        # Connect the save button to a new method
        self.general_savebutton.clicked.connect(self.save_data)



    # Add the handler method for the gender checkboxes
    def handleGenderCheckboxStateChange(self, state, checkbox):
        if state == QtCore.Qt.Checked:
                if checkbox == self.male_checkBox:
                        self.female_checkBox.hide()
                elif checkbox == self.female_checkBox:
                        self.male_checkBox.hide()
        else:
                self.male_checkBox.show()
                self.female_checkBox.show()

    def setupGeneralPage(self):
                
        self.General_Page = QtWidgets.QWidget()
        self.General_Page.setObjectName("General_Page")
        self.General_Page_gridLayout = QtWidgets.QGridLayout(self.General_Page)
        self.General_Page_gridLayout.setObjectName("General_Page_gridLayout")
        self.GE_widget = QtWidgets.QWidget(self.General_Page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GE_widget.setFont(font)
        self.GE_widget.setStyleSheet("QLabel {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"    color: white; /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#general_instructions, #general_date_instructions {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: rgb(24, 45, 83 ); /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#GeneralTabTitle_label {\n"
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
"#name_widget, #school_widget, #gender_widget, #dates_widget   {\n"
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
"    padding-left: 125px; /* Space between the text and the left margin */\n"
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
"     image: url(C:/Users/colli/Downloads/MakingUi/icon/tickhere.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(C:/Users/colli/Downloads/MakingUi/icon/tickmark.png); /* Absolute path to the checkmark image */\n"
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
"#general_savebutton {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#general_savebutton::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 150px; /* Width of the indicator */\n"
"    height: 150px; /* Height of the indicator */\n"
"}\n"
"\n"
"#general_savebutton::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(C:/Users/colli/Downloads/MakingUi/icon/notsaved.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"#general_savebutton::indicator::checked {\n"
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
        self.GE_widget.setObjectName("GE_widget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.GE_widget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.TitleLayout = QtWidgets.QHBoxLayout()
        self.TitleLayout.setObjectName("TitleLayout")
        spacerItem96 = QtWidgets.QSpacerItem(50, 97, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.TitleLayout.addItem(spacerItem96)
        self.GeneralTabTitle_label = QtWidgets.QLabel(self.GE_widget)
        self.GeneralTabTitle_label.setMinimumSize(QtCore.QSize(830, 100))
        self.GeneralTabTitle_label.setMaximumSize(QtCore.QSize(830, 100))
        self.GeneralTabTitle_label.setObjectName("GeneralTabTitle_label")
        self.TitleLayout.addWidget(self.GeneralTabTitle_label)
        spacerItem97 = QtWidgets.QSpacerItem(50, 97, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.TitleLayout.addItem(spacerItem97)
        self.gridLayout_9.addLayout(self.TitleLayout, 0, 0, 1, 1)
        self.input_area_verical_lyt = QtWidgets.QVBoxLayout()
        self.input_area_verical_lyt.setSpacing(30)
        self.input_area_verical_lyt.setObjectName("input_area_verical_lyt")
        self.name_widget = QtWidgets.QWidget(self.GE_widget)
        self.name_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.name_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.name_widget.setStyleSheet("")
        self.name_widget.setObjectName("name_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.name_widget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem98 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem98)
        self.general_name_label = QtWidgets.QLabel(self.name_widget)
        self.general_name_label.setMinimumSize(QtCore.QSize(260, 50))
        self.general_name_label.setMaximumSize(QtCore.QSize(260, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_name_label.setFont(font)
        self.general_name_label.setStyleSheet("")
        self.general_name_label.setObjectName("general_name_label")
        self.horizontalLayout.addWidget(self.general_name_label)
        spacerItem99 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem99)
        self.name_Insert = QtWidgets.QLineEdit(self.name_widget)
        self.name_Insert.setMinimumSize(QtCore.QSize(550, 50))
        self.name_Insert.setMaximumSize(QtCore.QSize(390, 50))
        self.name_Insert.setText("")
        self.name_Insert.setObjectName("name_Insert")
        self.horizontalLayout.addWidget(self.name_Insert)
        spacerItem100 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem100)
        self.name_vertical_line = QtWidgets.QFrame(self.name_widget)
        self.name_vertical_line.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line.setObjectName("name_vertical_line")
        self.horizontalLayout.addWidget(self.name_vertical_line)
        spacerItem101 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem101)
        self.name_checkBox = QtWidgets.QCheckBox(self.name_widget)
        self.name_checkBox.setMinimumSize(QtCore.QSize(100, 100))
        self.name_checkBox.setMaximumSize(QtCore.QSize(100, 100))
        self.name_checkBox.setText("")
        self.name_checkBox.setIconSize(QtCore.QSize(120, 120))
        self.name_checkBox.setObjectName("name_checkBox")
        self.horizontalLayout.addWidget(self.name_checkBox)
        spacerItem102 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem102)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.input_area_verical_lyt.addWidget(self.name_widget)
        self.school_widget = QtWidgets.QWidget(self.GE_widget)
        self.school_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.school_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.school_widget.setStyleSheet("")
        self.school_widget.setObjectName("school_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.school_widget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem103 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem103)
        self.general_school_label = QtWidgets.QLabel(self.school_widget)
        self.general_school_label.setMinimumSize(QtCore.QSize(260, 50))
        self.general_school_label.setMaximumSize(QtCore.QSize(260, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_school_label.setFont(font)
        self.general_school_label.setStyleSheet("")
        self.general_school_label.setObjectName("general_school_label")
        self.horizontalLayout_2.addWidget(self.general_school_label)
        spacerItem104 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem104)
        self.school_Insert = QtWidgets.QLineEdit(self.school_widget)
        self.school_Insert.setMinimumSize(QtCore.QSize(550, 50))
        self.school_Insert.setMaximumSize(QtCore.QSize(390, 50))
        self.school_Insert.setText("")
        self.school_Insert.setObjectName("school_Insert")
        self.horizontalLayout_2.addWidget(self.school_Insert)
        spacerItem105 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem105)
        self.name_vertical_line_2 = QtWidgets.QFrame(self.school_widget)
        self.name_vertical_line_2.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_2.setObjectName("name_vertical_line_2")
        self.horizontalLayout_2.addWidget(self.name_vertical_line_2)
        spacerItem106 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem106)
        self.school_checkBox = QtWidgets.QCheckBox(self.school_widget)
        self.school_checkBox.setMinimumSize(QtCore.QSize(100, 100))
        self.school_checkBox.setMaximumSize(QtCore.QSize(100, 100))
        self.school_checkBox.setText("")
        self.school_checkBox.setIconSize(QtCore.QSize(120, 120))
        self.school_checkBox.setObjectName("school_checkBox")
        self.horizontalLayout_2.addWidget(self.school_checkBox)
        spacerItem107 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem107)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.input_area_verical_lyt.addWidget(self.school_widget)

        self.gender_widget = QtWidgets.QWidget(self.GE_widget)
        self.gender_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.gender_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.gender_widget.setStyleSheet("")
        self.gender_widget.setObjectName("gender_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gender_widget)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem108 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem108)
        self.general_gender_label = QtWidgets.QLabel(self.gender_widget)
        self.general_gender_label.setMinimumSize(QtCore.QSize(110, 50))
        self.general_gender_label.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_gender_label.setFont(font)
        self.general_gender_label.setStyleSheet("")
        self.general_gender_label.setObjectName("general_gender_label")
        self.horizontalLayout_3.addWidget(self.general_gender_label)
        spacerItem109 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem109)
        self.name_vertical_line_4 = QtWidgets.QFrame(self.gender_widget)
        self.name_vertical_line_4.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_4.setObjectName("name_vertical_line_4")
        self.horizontalLayout_3.addWidget(self.name_vertical_line_4)
        spacerItem110 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem110)
        self.general_male_label = QtWidgets.QLabel(self.gender_widget)
        self.general_male_label.setMinimumSize(QtCore.QSize(70, 50))
        self.general_male_label.setMaximumSize(QtCore.QSize(70, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_male_label.setFont(font)
        self.general_male_label.setStyleSheet("")
        self.general_male_label.setObjectName("general_male_label")
        self.horizontalLayout_3.addWidget(self.general_male_label)
        spacerItem111 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem111)
        self.male_checkBox = QtWidgets.QCheckBox(self.gender_widget)
        self.male_checkBox.setMinimumSize(QtCore.QSize(100, 100))
        self.male_checkBox.setMaximumSize(QtCore.QSize(100, 100))
        self.male_checkBox.setText("")
        self.male_checkBox.setIconSize(QtCore.QSize(120, 120))
        self.male_checkBox.setObjectName("male_checkBox")
        self.horizontalLayout_3.addWidget(self.male_checkBox)
        spacerItem112 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem112)
        self.name_vertical_line_3 = QtWidgets.QFrame(self.gender_widget)
        self.name_vertical_line_3.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_3.setObjectName("name_vertical_line_3")
        self.horizontalLayout_3.addWidget(self.name_vertical_line_3)
        self.general_female_label = QtWidgets.QLabel(self.gender_widget)
        self.general_female_label.setMinimumSize(QtCore.QSize(100, 50))
        self.general_female_label.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_female_label.setFont(font)
        self.general_female_label.setStyleSheet("")
        self.general_female_label.setObjectName("general_female_label")
        self.horizontalLayout_3.addWidget(self.general_female_label)
        spacerItem113 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem113)
        self.female_checkBox = QtWidgets.QCheckBox(self.gender_widget)
        self.female_checkBox.setMinimumSize(QtCore.QSize(100, 100))
        self.female_checkBox.setMaximumSize(QtCore.QSize(100, 100))
        self.female_checkBox.setText("")
        self.female_checkBox.setIconSize(QtCore.QSize(120, 120))
        self.female_checkBox.setObjectName("female_checkBox")
        self.horizontalLayout_3.addWidget(self.female_checkBox)
        spacerItem114 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem114)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.input_area_verical_lyt.addWidget(self.gender_widget)


        self.general_date_instructions = QtWidgets.QLabel(self.GE_widget)
        self.general_date_instructions.setMinimumSize(QtCore.QSize(1168, 30))
        self.general_date_instructions.setMaximumSize(QtCore.QSize(1168, 30))
        self.general_date_instructions.setObjectName("general_date_instructions")
        self.input_area_verical_lyt.addWidget(self.general_date_instructions)
        self.dates_widget = QtWidgets.QWidget(self.GE_widget)
        self.dates_widget.setMinimumSize(QtCore.QSize(1168, 112))
        self.dates_widget.setMaximumSize(QtCore.QSize(1168, 112))
        self.dates_widget.setStyleSheet("")
        self.dates_widget.setObjectName("dates_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dates_widget)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.general_dateofBirth_label = QtWidgets.QLabel(self.dates_widget)
        self.general_dateofBirth_label.setMinimumSize(QtCore.QSize(175, 50))
        self.general_dateofBirth_label.setMaximumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_dateofBirth_label.setFont(font)
        self.general_dateofBirth_label.setStyleSheet("")
        self.general_dateofBirth_label.setObjectName("general_dateofBirth_label")
        self.horizontalLayout_4.addWidget(self.general_dateofBirth_label)
        self.general_dateofBrith_Edit = QtWidgets.QDateEdit(self.dates_widget)
        self.general_dateofBrith_Edit.setMinimumSize(QtCore.QSize(180, 60))
        self.general_dateofBrith_Edit.setMaximumSize(QtCore.QSize(180, 60))
        self.general_dateofBrith_Edit.setStyleSheet("\n"
"")
        self.general_dateofBrith_Edit.setDate(QtCore.QDate(2008, 1, 1))
        self.general_dateofBrith_Edit.setDisplayFormat("dd/MM/yyyy")  # Set the display format to day month year
        self.general_dateofBrith_Edit.setObjectName("general_dateofBrith_Edit")
        self.horizontalLayout_4.addWidget(self.general_dateofBrith_Edit)
        self.dateofBirth_checkBox = QtWidgets.QCheckBox(self.dates_widget)
        self.dateofBirth_checkBox.setMinimumSize(QtCore.QSize(100, 100))
        self.dateofBirth_checkBox.setMaximumSize(QtCore.QSize(100, 100))
        self.dateofBirth_checkBox.setText("")
        self.dateofBirth_checkBox.setIconSize(QtCore.QSize(120, 120))
        self.dateofBirth_checkBox.setObjectName("dateofBirth_checkBox")
        self.horizontalLayout_4.addWidget(self.dateofBirth_checkBox)
        self.name_vertical_line_5 = QtWidgets.QFrame(self.dates_widget)
        self.name_vertical_line_5.setMinimumSize(QtCore.QSize(0, 100))
        self.name_vertical_line_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.name_vertical_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.name_vertical_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.name_vertical_line_5.setObjectName("name_vertical_line_5")
        self.horizontalLayout_4.addWidget(self.name_vertical_line_5)
        spacerItem115 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem115)
        self.general_todaysdate_label = QtWidgets.QLabel(self.dates_widget)
        self.general_todaysdate_label.setMinimumSize(QtCore.QSize(177, 50))
        self.general_todaysdate_label.setMaximumSize(QtCore.QSize(177, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.general_todaysdate_label.setFont(font)
        self.general_todaysdate_label.setStyleSheet("")
        self.general_todaysdate_label.setObjectName("general_todaysdate_label")
        self.horizontalLayout_4.addWidget(self.general_todaysdate_label)
        self.general_todaysDate_Edit = QtWidgets.QDateEdit(self.dates_widget)
        self.general_todaysDate_Edit.setMinimumSize(QtCore.QSize(180, 60))
        self.general_todaysDate_Edit.setMaximumSize(QtCore.QSize(180, 60))
        self.general_todaysDate_Edit.setStyleSheet("\n"
"")
        self.general_todaysDate_Edit.setDate(QtCore.QDate(2024, 2, 3))
        self.general_todaysDate_Edit.setDisplayFormat("dd/MM/yyyy")  # Set the display format to day month year
        self.general_todaysDate_Edit.setObjectName("general_todaysDate_Edit")
        self.horizontalLayout_4.addWidget(self.general_todaysDate_Edit)
        self.todaysDate_checkBox = QtWidgets.QCheckBox(self.dates_widget)
        self.todaysDate_checkBox.setMinimumSize(QtCore.QSize(100, 100))
        self.todaysDate_checkBox.setMaximumSize(QtCore.QSize(100, 100))
        self.todaysDate_checkBox.setText("")
        self.todaysDate_checkBox.setIconSize(QtCore.QSize(120, 120))
        self.todaysDate_checkBox.setObjectName("todaysDate_checkBox")
        self.horizontalLayout_4.addWidget(self.todaysDate_checkBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.input_area_verical_lyt.addWidget(self.dates_widget)
        self.gridLayout_9.addLayout(self.input_area_verical_lyt, 2, 0, 1, 1)
        self.general_savebutton = QtWidgets.QCheckBox(self.GE_widget)
        self.general_savebutton.setMinimumSize(QtCore.QSize(150, 80))
        self.general_savebutton.setMaximumSize(QtCore.QSize(150, 80))
        self.general_savebutton.setText("")
        self.general_savebutton.setIconSize(QtCore.QSize(100, 100))
        self.general_savebutton.setObjectName("general_savebutton")
        self.gridLayout_9.addWidget(self.general_savebutton, 3, 0, 1, 1)
        self.general_instructions = QtWidgets.QLabel(self.GE_widget)
        self.general_instructions.setMinimumSize(QtCore.QSize(1168, 60))
        self.general_instructions.setMaximumSize(QtCore.QSize(1168, 60))
        self.general_instructions.setObjectName("general_instructions")
        self.gridLayout_9.addWidget(self.general_instructions, 1, 0, 1, 1)
        self.General_Page_gridLayout.addWidget(self.GE_widget, 0, 1, 1, 1)
        

        # Add the SelfEsteem_Page to the stackedWidget at a specific index
        index = 3  # Change this index to where you want to add the page in the stackedWidget
        self.stackedWidget.insertWidget(index, self.General_Page)


               
        
    def save_data(self):
        if self.general_savebutton.isChecked():
                # Check if all questions are answered
                if not all([self.name_checkBox.isChecked(), self.school_checkBox.isChecked(),
                                self.male_checkBox.isChecked() or self.female_checkBox.isChecked(),
                                self.dateofBirth_checkBox.isChecked(), self.todaysDate_checkBox.isChecked()]):
                        # Display warning dialog
                        QtWidgets.QMessageBox.warning(self.General_Page, "Incomplete Information",
                                                        "Please ensure all questions are answered before saving.")
                        self.general_savebutton.setChecked(False)  # Uncheck the save button
                        return

                # Save the data from the form into the shared_data dictionary
                self.shared_data['name'] = self.name_Insert.text()
                self.shared_data['school'] = self.school_Insert.text()
                self.shared_data['gender'] = 'Male' if self.male_checkBox.isChecked() else 'Female'
                self.shared_data['dateOfBirth'] = self.general_dateofBrith_Edit.date().toString("dd/MM/yyyy")
                self.shared_data['todaysDate'] = self.general_todaysDate_Edit.date().toString("dd/MM/yyyy")

                # Update the preview tab with the new data
                self.previewTab.updatePreview()                