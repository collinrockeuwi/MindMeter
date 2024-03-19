from PyQt5 import QtCore, QtGui, QtWidgets        
from profile_print_dialouge import Ui_Form  # Import the Ui_Form class


class DataBaseTab:
    def __init__(self, parent, stackedWidget, db_manager):
        self.stackedWidget = stackedWidget
        self.db_manager = db_manager  # Store the DatabaseManager instance
        self.setupDataBasePage(parent)
        

    def setupDataBasePage(self, parent):


        self.Database = QtWidgets.QWidget()
        self.Database.setStyleSheet("#database_toolbar_widget{\n"
"\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"    text-align: left;\n"
"    height:70px;\n"
"    border: 1px;\n"
"    padding-left: 10px;\n"
"    border-radius: 5px; /* Round top left corner */\n"
"    \n"
"    background-color: rgb(31, 149, 239); /* Normal background color */\n"
"    font-family: \'Roboto\';\n"
"    font-size: 15px; /* Set the font size here */\n"
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
"#preview_savebutton {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#database_savebutton::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 90px; /* Width of the indicator */\n"
"    height: 30px; /* Height of the indicator */\n"
"}\n"
"\n"
"#database_savebutton::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(C:/Users/colli/Downloads/MakingUi/icon//notsaved.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"#database_savebutton::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(C:/Users/colli/Downloads/MakingUi/icon/saved.png); /* Absolute path to the checkmark image */\n"
"    \n"
"}")
        self.Database.setObjectName("Database")
        self.Database_gridLayout = QtWidgets.QGridLayout(self.Database)
        self.Database_gridLayout.setObjectName("Database_gridLayout")




        self.databasebutton_widget = QtWidgets.QWidget(self.Database)
        self.databasebutton_widget.setMinimumSize(QtCore.QSize(1200, 50))
        self.databasebutton_widget.setMaximumSize(QtCore.QSize(1200, 50))
        self.databasebutton_widget.setObjectName("databasebutton_widget")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.databasebutton_widget)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.database_refresh_button = QtWidgets.QPushButton(self.databasebutton_widget)
        self.database_refresh_button.setMinimumSize(QtCore.QSize(90, 30))
        self.database_refresh_button.setMaximumSize(QtCore.QSize(90, 30))
        self.database_refresh_button.setObjectName("database_refresh_button")
        self.horizontalLayout_15.addWidget(self.database_refresh_button)
        spacerItem138 = QtWidgets.QSpacerItem(90, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem138)
        self.database_edit_button = QtWidgets.QPushButton(self.databasebutton_widget)
        self.database_edit_button.setMinimumSize(QtCore.QSize(90, 30))
        self.database_edit_button.setMaximumSize(QtCore.QSize(90, 30))
        self.database_edit_button.setObjectName("database_edit_button")
        self.horizontalLayout_15.addWidget(self.database_edit_button)
        self.database_undo_button = QtWidgets.QPushButton(self.databasebutton_widget)
        self.database_undo_button.setMinimumSize(QtCore.QSize(90, 30))
        self.database_undo_button.setMaximumSize(QtCore.QSize(90, 30))
        self.database_undo_button.setObjectName("database_undo_button")
        self.horizontalLayout_15.addWidget(self.database_undo_button)
        self.database_reset_button = QtWidgets.QPushButton(self.databasebutton_widget)
        self.database_reset_button.setMinimumSize(QtCore.QSize(90, 30))
        self.database_reset_button.setMaximumSize(QtCore.QSize(90, 30))
        self.database_reset_button.setObjectName("database_reset_button")
        self.horizontalLayout_15.addWidget(self.database_reset_button)
        self.database_savebutton = QtWidgets.QCheckBox(self.databasebutton_widget)
        self.database_savebutton.setMinimumSize(QtCore.QSize(90, 30))
        self.database_savebutton.setMaximumSize(QtCore.QSize(90, 30))
        self.database_savebutton.setText("")
        self.database_savebutton.setObjectName("database_savebutton")
        self.horizontalLayout_15.addWidget(self.database_savebutton)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)
        spacerItem139 = QtWidgets.QSpacerItem(800, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem139)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)
        self.Database_gridLayout.addWidget(self.databasebutton_widget, 0, 0, 1, 1)


        # Make the Edit Mode button checkable
        self.database_edit_button.setCheckable(True)
        self.database_edit_button.setChecked(False)  # Start off unchecked

        # Connect the Edit Mode button's toggled signal to a slot
        self.database_edit_button.toggled.connect(self.toggleEditMode)

        # Initially hide the Undo, Reset, and Save buttons
        self.database_undo_button.hide()
        self.database_reset_button.hide()
        self.database_savebutton.hide()





        self.DatabaseTab = QtWidgets.QTableWidget(self.Database)
        self.DatabaseTab.setMinimumSize(QtCore.QSize(0, 0))
        self.DatabaseTab.setMaximumSize(QtCore.QSize(1550, 800))
        self.DatabaseTab.setStyleSheet("QTableWidget {\n"
"    font-family: \"Roboto\"; /* Using the Roboto font */\n"
"    color: black; /* Text color */\n"
"    background-color: white; /* Background color */\n"
"    border: 1px solid #D6D6D6; /* Border color and width */\n"
"    gridline-color: #D6D6D6; /* Color of the grid lines */\n"
"    font-size: 18px; /* Increase font size */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 10px; /* Increase padding inside cells */\n"
"    border: none; /* No borders for individual items */\n"
"}\n"
"\n"
"/* Hover effect for cells */\n"
"QTableWidget::item:hover {\n"
"    background-color: rgb(220, 240, 255); /* Light blue background for hover */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #E0E0E0; /* Background color for selected items */\n"
"    color: black; /* Text color for selected items */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(35, 155, 245); /* Slightly different blue */\n"
"    padding: 10px; /* Increase padding inside header cells */\n"
"    border: 1px solid #D6D6D6; /* Border for header cells */\n"
"    font-size: 18px; /* Larger font size for header text */\n"
"    font-weight: bold; /* Bold font weight for header text */\n"
"    color: white; /* Text color */\n"
"}\n"
"\n"
"/* Hover effect for headers */\n"
"QHeaderView::section:hover {\n"
"    background-color: rgb(25, 135, 220); /* A different blue for hover */\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    font-family: \"Roboto Bk\";\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    font-family: \"Roboto Lt\";\n"
"}\n"
"\n"
"/* Scrollbar styling */\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
"    background: #F5F5F5;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #D6D6D6;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #E0E0E0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"


"")
        self.DatabaseTab.setObjectName("DatabaseTab")
        self.DatabaseTab.setColumnCount(8)
        self.DatabaseTab.setHorizontalHeaderLabels([
            "Name","Date of Birth", "Age", "Sex", "School", 
            "Stress Test", "Depression Test", "Self-Esteem Test"
        ])

        # Set column widths
        self.DatabaseTab.setColumnWidth(0, 180)  # Set width for "Self-Esteem Test" column
        self.DatabaseTab.setColumnWidth(1, 180)  # Set width for "Self-Esteem Test" column
        self.DatabaseTab.setColumnWidth(5, 150)  # Set width for "Depression Test" column
        self.DatabaseTab.setColumnWidth(6, 180)  # Set width for "Self-Esteem Test" column
        self.DatabaseTab.setColumnWidth(7, 180)  # Set width for "Self-Esteem Test" column



        self.Database_gridLayout.addWidget(self.DatabaseTab, 1, 0, 1, 1)

       




        
        
        self.stackedWidget.insertWidget(5, self.Database)
        self.DatabaseTab.cellClicked.connect(self.openProfilePrintDialogue)





    def toggleEditMode(self, checked):
        if checked:
            # Show the Undo, Reset, and Save buttons
            self.database_undo_button.show()
            self.database_reset_button.show()
            self.database_savebutton.show()
        else:
            # Hide the Undo, Reset, and Save buttons
            self.database_undo_button.hide()
            self.database_reset_button.hide()
            self.database_savebutton.hide()



    def updateTable(self, data):
        print("Updating table with data:", data)  # Table Update Check
        self.DatabaseTab.setRowCount(len(data))
        for row, entry in enumerate(data):
            for col, value in enumerate(entry):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.DatabaseTab.setItem(row, col, item)

    def refreshTable(self):
        student_test_summary = self.db_manager.fetch_student_test_summary()
        self.updateTable(student_test_summary)

    
    def openProfilePrintDialogue(self, row, column):
        if column == 0:  # Check if the first column is clicked
            student_name = self.DatabaseTab.item(row, 0).text()  # Retrieve the student's name from the first column
            self.profilePrintDialog = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.profilePrintDialog)
            self.profilePrintDialog.setWindowTitle(f"{student_name} Assessment Profile")  # Set the window title with the student's name
            self.profilePrintDialog.show()