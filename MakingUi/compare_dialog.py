from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal



class CompareDialog(QtWidgets.QDialog):
    compareTestsSignal = QtCore.pyqtSignal(int, int)  # Custom signal to emit selected test IDs

    def __init__(self, parent=None, db_manager=None):
        super().__init__(parent)
        self.db_manager = db_manager
        self.setWindowTitle("Compare Tests")
        self.layout = QtWidgets.QVBoxLayout(self)

        self.comboBox1 = QtWidgets.QComboBox(self)
        self.comboBox2 = QtWidgets.QComboBox(self)
        self.enterButton = QtWidgets.QPushButton("Enter", self)  # Enter button

        self.layout.addWidget(self.comboBox1)
        self.layout.addWidget(self.comboBox2)
        self.layout.addWidget(self.enterButton)

        self.enterButton.clicked.connect(self.emitSelection)  # Connect the enter button to the emitSelection method

    def populateComboBox(self, comboBox, student_id, test_table):
        test_dates = self.db_manager.get_test_dates_by_student_id(student_id, test_table)
        print(f"Populating combo box with test dates: {test_dates}")  # Print the test_dates list
        comboBox.clear()
        for i, (test_id, date) in enumerate(test_dates):
            print(f"Adding TestID {test_id} with date {date}")  # Print the TestID and date being added
            comboBox.addItem(f"Test {i + 1}: {date}", test_id)  # Set TestID as item data



    def setComboBoxItems(self, student_id, test_table):
        self.populateComboBox(self.comboBox1, student_id, test_table)
        self.populateComboBox(self.comboBox2, student_id, test_table)

    def getSelectedTestIds(self):
        test_id1 = self.comboBox1.currentData()
        test_id2 = self.comboBox2.currentData()
        print(f"Selected Test IDs: {test_id1}, {test_id2}")  # Print the selected TestIDs
        print(f"Types: {type(test_id1)}, {type(test_id2)}")  # Print the types of the selected TestIDs
        return test_id1, test_id2

    def compareStressTests(self):
        dialog = CompareDialog(self.Form)
        dialog.compareTestsSignal.connect(self.handleTestComparison)  # Connect the signal to a slot
        # Rest of the code...



    def emitSelection(self):
        test_id1, test_id2 = self.getSelectedTestIds()
        print(f"Emitting signal with Test IDs: {test_id1}, {test_id2}")
        self.compareTestsSignal.emit(test_id1, test_id2)  # Emit the signal with selected test IDs
        self.accept()  # Close the dialog
