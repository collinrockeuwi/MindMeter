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
        self.DatabaseTab.setStyleSheet("QTableWidget {font-family: 'Roboto'; color: black; background-color: white; border: 1px solid #D6D6D6; gridline-color: #D6D6D6; font-size: 18px;} QTableWidget::item {padding: 10px; border: none;} QTableWidget::item:hover {background-color: rgb(220, 240, 255);} QTableWidget::item:selected {background-color: #E0E0E0; color: black;} QHeaderView::section {background-color: rgb(35, 155, 245); padding: 10px; border: 1px solid #D6D6D6; font-size: 18px; font-weight: bold;} QHeaderView::section:hover {background-color: rgb(25, 135, 220);} QHeaderView::section:horizontal {font-family: 'Roboto Bk';} QHeaderView::section:vertical {font-family: 'Roboto Lt';} QScrollBar:vertical {width: 10px; background: #F5F5F5;} QScrollBar::handle:vertical {background: #D6D6D6; min-height: 20px; border-radius: 5px;} QScrollBar::handle:vertical:hover {background: #E0E0E0;} QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {border: none; background: none;} QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;} QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {width: 0px; height: 0px;}")
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