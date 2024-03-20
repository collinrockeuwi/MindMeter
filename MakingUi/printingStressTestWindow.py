from PyQt5 import QtCore, QtWidgets, QtGui, QtPrintSupport

class StressTab:
    questions = [
        "Been upset because of something that happened unexpectedly?",
        "Felt that you were unable to control the important things in your life?",
        "Felt nervous and 'stressed'?",
        "Felt confident about your ability to handle your personal problems?",
        "Felt that things were going your way?",
        "Found that you could not cope with all the things that you had to do?",
        "Been able to control irritations in your life?",
        "Felt that you were on top of things?",
        "Been angered because of things that were outside of your control?",
        "Felt difficulties were piling up so high that you could not overcome them?"
    ]

class PrintingStressTestWindow(QtWidgets.QMainWindow):
    def __init__(self, general_info, test_scores, test_id, test_date, parent=None):
        super().__init__(parent)
        self.general_info = general_info
        self.test_scores = test_scores
        self.test_id = test_id
        self.test_date = test_date
        self.setupUi(self)



    def setupUi(self, PsycheEval_MainWindow):
        PsycheEval_MainWindow.setObjectName("PsycheEval_MainWindow")
        PsycheEval_MainWindow.resize(2038, 1116)

        self.central_widget = QtWidgets.QWidget(PsycheEval_MainWindow)
        PsycheEval_MainWindow.setCentralWidget(self.central_widget)

        self.textEdit = QtWidgets.QTextEdit(self.central_widget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 2018, 1040))

        self.menubar = QtWidgets.QMenuBar(PsycheEval_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2038, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PsycheEval_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PsycheEval_MainWindow)
        self.statusbar.setObjectName("statusbar")
        PsycheEval_MainWindow.setStatusBar(self.statusbar)
        self.actionPrint = QtWidgets.QAction(PsycheEval_MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.menuFile.addAction(self.actionPrint)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PsycheEval_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(PsycheEval_MainWindow)

        # Connect the print action to the printTest method
        self.actionPrint.triggered.connect(self.printTest)
           
        self.setTestDetails(self.general_info, self.test_scores, self.test_id, self.test_date)


    def retranslateUi(self, PsycheEval_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        PsycheEval_MainWindow.setWindowTitle(_translate("PsycheEval_MainWindow", "PsycheEval"))
        self.menuFile.setTitle(_translate("PsycheEval_MainWindow", "File"))
        self.actionPrint.setText(_translate("PsycheEval_MainWindow", "Print"))

    def printTest(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setPageSize(QtPrintSupport.QPrinter.Letter)
        dialog = QtPrintSupport.QPrintDialog(printer, self.central_widget)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.textEdit.print_(printer)

    def setTestDetails(self, general_info, test_scores, test_id, test_date):
        # Clear the existing content
        self.textEdit.clear()

        # Add general information to the QTextEdit
        for key, value in general_info.items():
            self.textEdit.append(f"{key}: {value}")

        # Add the test date
        self.textEdit.append(f"Test Date: {test_date}")

        # Assuming test_scores is a list of responses for the questions
        for i, response in enumerate(test_scores):
            question = StressTab.questions[i]
            self.textEdit.append(f"{i + 1}. {question}")
            self.textEdit.append(f"Response: {response}")

        # Add the test ID at the bottom
        self.textEdit.append(f"Test ID: {test_id}")

        self.textEdit.moveCursor(QtGui.QTextCursor.Start)

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Sample general information and test details for demonstration
    general_info = {
        "Name": "John Doe",
        "Date of Birth": "01/01/1990",
        "Age": "31",
        "Sex": "Male",
        "School": "ABC High School"
    }
    test_details = [3, 2, 4, 1, 5, 2, 3, 4, 1, 5]

    # Create and show the main window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PsycheEval_MainWindow()
    ui.setupUi(MainWindow)
    ui.setTestDetails(general_info, test_details)
    MainWindow.show()

    sys.exit(app.exec_())
'''