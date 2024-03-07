from PyQt5 import QtCore, QtGui, QtWidgets        



class DataBaseTab:
    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.setupDataBasePage(parent)
        

    def setupDataBasePage(self, parent):


        self.Database = QtWidgets.QWidget()
        self.Database.setObjectName("Database")
        self.Database_gridLayout = QtWidgets.QGridLayout(self.Database)
        self.Database_gridLayout.setObjectName("Database_gridLayout")
        self.DatabaseTab = QtWidgets.QTableWidget(self.Database)
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
        self.DatabaseTab.setColumnCount(7)
        self.DatabaseTab.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTab.setHorizontalHeaderItem(6, item)
        self.Database_gridLayout.addWidget(self.DatabaseTab, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Database)




