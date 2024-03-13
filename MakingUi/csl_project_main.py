# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'makingui3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from SelfEsteemTab import SelfEsteemTab  # Import the class
from DepressionTab import DepressionTab  # Import the class
from StressTab import StressTab # Import the class
from GeneralTab import GeneralTab # Import the class
from PreviewTab import PreviewTab # Import the class
from DataBaseTab import DataBaseTab # Import the class
from DatabaseManager import DatabaseManager # Import the class
from MainWindow import MainWindow # Import the class
from MainWindow2 import MainWindow2 # Import the class


class Ui_PsycheEval_MainWindow(object):
    def setupUi(self, PsycheEval_MainWindow):
       

        self.MainWindow = MainWindow(PsycheEval_MainWindow)
        self.MainWindow2 = MainWindow2(PsycheEval_MainWindow, self.MainWindow)
        

#stack widget           #stack widget           #stack widget           #stack widget              
#stack widget           #stack widget           #stack widget           #stack widget  
#stack widget           #stack widget           #stack widget           #stack widget  
#stack widget           #stack widget           #stack widget           #stack widget  
#stack widget           #stack widget           #stack widget           #stack widget  
#stack widget           #stack widget           #stack widget           #stack widget  




        self.Active_widget = QtWidgets.QWidget(self.MainWindow2.MainWindow_2)
        self.Active_widget.setObjectName("Active_widget")
        self.Active_widget_vertical_lyt = QtWidgets.QVBoxLayout(self.Active_widget)
        self.Active_widget_vertical_lyt.setObjectName("Active_widget_vertical_lyt")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Active_widget)
        self.stackedWidget.setStyleSheet("QLabel {\n"
" \n"
"    qproperty-alignment: \'AlignVCenter | AlignLeft\'; /* Vertically centered and left-aligned */\n"
"  \n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")

#Button Connection              #Button Connection              #Button Connection              #Button Connection
#Button Connection              #Button Connection              #Button Connection              #Button Connection
#Button Connection              #Button Connection              #Button Connection              #Button Connection
#Button Connection              #Button Connection              #Button Connection              #Button Connection
#Button Connection              #Button Connection              #Button Connection              #Button Connection
        self.MainWindow.General_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.MainWindow.Stress_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.MainWindow.Depression_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.MainWindow.SelfEsteem_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.MainWindow.Preview_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.MainWindow.Database_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

        self.MainWindow.expanded_icon_General_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.MainWindow.expanded_icon_Stress_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.MainWindow.expanded_icon_Depression_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.MainWindow.expanded_icon_SelfEsteem_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.MainWindow.expanded_icon_Preview_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.MainWindow.expanded_icon_Database_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))




#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page 
#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page 
#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page 
#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page 
#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page         
#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page 
#SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page                #SelfEsteem Page 

        # Create an instance of the SelfEsteemTab class
        self.selfEsteemTab = SelfEsteemTab(PsycheEval_MainWindow, self.stackedWidget)

         # Connect the SelfEsteem_pushButton to switch to the SelfEsteemTab in the stackedWidget
        self.MainWindow.SelfEsteem_pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))




#DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage
#DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage
#DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage
#DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage       
#DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage         #DepressionPage


        self.DepressionTab = DepressionTab(PsycheEval_MainWindow, self.stackedWidget)


#StressPage             #StressPage             #StressPage             #StressPage             #StressPage
#StressPage             #StressPage             #StressPage             #StressPage             #StressPage
#StressPage             #StressPage             #StressPage             #StressPage             #StressPage
#StressPage             #StressPage             #StressPage             #StressPage             #StressPage
#StressPage             #StressPage             #StressPage             #StressPage             #StressPage
#StressPage             #StressPage             #StressPage             #StressPage             #StressPage
#StressPage             #StressPage             #StressPage             #StressPage             #StressPage

        self.StressTab = StressTab(PsycheEval_MainWindow, self.stackedWidget)

#General Page           #General Page           #General Page           #General Page
#General Page           #General Page           #General Page           #General Page     
#General Page           #General Page           #General Page           #General Page
#General Page           #General Page           #General Page           #General Page
#General Page           #General Page           #General Page           #General Page        


        self.GeneralTab = GeneralTab(PsycheEval_MainWindow, self.stackedWidget)


#Preview                #Preview                #Preview                #Preview                #Preview
#Preview                #Preview                #Preview                #Preview                #Preview
#Preview                #Preview                #Preview                #Preview                #Preview
#Preview                #Preview                #Preview                #Preview                #Preview
#Preview                #Preview                #Preview                #Preview                #Preview

        self.PreviewTab = PreviewTab(PsycheEval_MainWindow, self.stackedWidget)


#DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage 
#DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage
#DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage 
#DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage 
#DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage           #DatabasePage  

        self.DataBaseTab = DataBaseTab(PsycheEval_MainWindow, self.stackedWidget)
        # Fetch student test summary and update the table
        db = DatabaseManager('student_tests.db')
        student_test_summary = db.fetch_student_test_summary()
        #print("Student Test Summary:", student_test_summary)  # Data Fetching Check
        self.DataBaseTab.updateTable(student_test_summary)

#Other          #Other          #Other          #Other
#Other          #Other          #Other          #Other
#Other          #Other          #Other          #Other
#Other          #Other          #Other          #Other
#Other          #Other          #Other          #Other
#Other          #Other          #Other          #Other


        self.Active_widget_vertical_lyt.addWidget(self.stackedWidget)
        self.MainWindow2.MainWindow_2_verticalLayout.addWidget(self.Active_widget)
        self.MainWindow.MainWindow_gridLayout.addWidget(self.MainWindow2.MainWindow_2, 0, 2, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.MainWindow.MainWindow_grid_lyt)
        self.verticalScrollBar.setMinimumSize(QtCore.QSize(21, 1001))
        self.verticalScrollBar.setMaximumSize(QtCore.QSize(21, 1001))
        self.verticalScrollBar.setStyleSheet("QScrollBar:vertical {\n"
"    border: none;\n"
"    background: white; /* Inverted scrollbar background to white */\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    margin: 0px 0px 0px 0px; /* Margins around the scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(31, 149, 239); /* Inverted handle color to blue */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Handle border radius */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(45, 45, 45); /* Darker color for hover, can be adjusted */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: white; /* Inverted button background to white */\n"
"    height: 0px; /* Hide the button */\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: white; /* Inverted button background to white */\n"
"    height: 0px; /* Hide the button */\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* Arrow background */\n"
"    color: none; /* Arrow color */\n"
"    width: 0px; /* Arrow width */\n"
"    height: 0px; /* Arrow height */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* Page background when clicking above/below the handle */\n"
"}\n"
"")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.MainWindow.MainWindow_gridLayout.addWidget(self.verticalScrollBar, 0, 3, 1, 1)
        PsycheEval_MainWindow.setCentralWidget(self.MainWindow.MainWindow_grid_lyt)
        self.menubar = QtWidgets.QMenuBar(PsycheEval_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
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
        self.stackedWidget.setCurrentIndex(5)
        self.selfEsteemTab.SelfEsteem_tabWidget.setCurrentIndex(0)
        self.DepressionTab.Depression_Page_tabWidget.setCurrentIndex(1)
        self.StressTab.Stress_tabWidget.setCurrentIndex(0)

        #topbar menu
        self.MainWindow2.topbar_menu_button.toggled['bool'].connect(self.MainWindow.small_icon_widget.setHidden) # type: ignore
        self.MainWindow2.topbar_menu_button.toggled['bool'].connect(self.MainWindow.expanded_icon_widget.setVisible) # type: ignore

        # Set the initial visibility of the bars based on the button's checked state
        self.MainWindow.small_icon_widget.setHidden(self.MainWindow2.topbar_menu_button.isChecked())
        self.MainWindow.expanded_icon_widget.setVisible(self.MainWindow2.topbar_menu_button.isChecked())



        self.MainWindow.General_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_General_pushButton.setChecked) # type: ignore
        self.MainWindow.Stress_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_Stress_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_General_pushButton.toggled['bool'].connect(self.MainWindow.General_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_Stress_pushButton.toggled['bool'].connect(self.MainWindow.Stress_pushButton.setChecked) # type: ignore
        self.MainWindow.Depression_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_Depression_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_Depression_pushButton.toggled['bool'].connect(self.MainWindow.Depression_pushButton.setChecked) # type: ignore
        self.MainWindow.SelfEsteem_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_SelfEsteem_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_SelfEsteem_pushButton.toggled['bool'].connect(self.MainWindow.SelfEsteem_pushButton.setChecked) # type: ignore
        self.MainWindow.Preview_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_Preview_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_Preview_pushButton.toggled['bool'].connect(self.MainWindow.Preview_pushButton.setChecked) # type: ignore
        self.MainWindow.Database_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_Database_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_Database_pushButton.toggled['bool'].connect(self.MainWindow.Database_pushButton.setChecked) # type: ignore
        self.MainWindow.Exit_pushButton.toggled['bool'].connect(self.MainWindow.expanded_icon_Exit_pushButton.setChecked) # type: ignore
        self.MainWindow.expanded_icon_Exit_pushButton.toggled['bool'].connect(self.MainWindow.Exit_pushButton.setChecked) # type: ignore
        # Connect sliders and spin boxes dynamically
        for question_num in range(1, len(SelfEsteemTab.questions) + 1):
                slider = getattr(self.selfEsteemTab, f"SE_Q{question_num}_horizontalSlider")
                spin_box = getattr(self.selfEsteemTab, f"SE_Q{question_num}_spinBox")

                slider.sliderMoved.connect(spin_box.setValue)
                spin_box.valueChanged.connect(slider.setValue)
                slider.valueChanged.connect(spin_box.setValue)
        QtCore.QMetaObject.connectSlotsByName(PsycheEval_MainWindow)

    def retranslateUi(self, PsycheEval_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        PsycheEval_MainWindow.setWindowTitle(_translate("PsycheEval_MainWindow", "MainWindow"))
        self.MainWindow.logo_mainlabel.setText(_translate("PsycheEval_MainWindow", "PsycheEval"))
        self.MainWindow.expanded_icon_General_pushButton.setText(_translate("PsycheEval_MainWindow", "   General"))
        self.MainWindow.expanded_icon_Stress_pushButton.setText(_translate("PsycheEval_MainWindow", "   Stress "))
        self.MainWindow.expanded_icon_Depression_pushButton.setText(_translate("PsycheEval_MainWindow", "   Depression"))
        self.MainWindow.expanded_icon_SelfEsteem_pushButton.setText(_translate("PsycheEval_MainWindow", "   Self-Esteem"))
        self.MainWindow.expanded_icon_Preview_pushButton.setText(_translate("PsycheEval_MainWindow", "   Preview"))
        self.MainWindow.expanded_icon_Database_pushButton.setText(_translate("PsycheEval_MainWindow", "   Database"))
        self.MainWindow.expanded_icon_Exit_pushButton.setText(_translate("PsycheEval_MainWindow", "   Exit"))
        
        # Set text for self-esteem questions
        for question_num, question_text in enumerate(SelfEsteemTab.questions, start=1):
                no_label = self.selfEsteemTab.question_widgets[f"SE_Q{question_num}_no_Label"]
                question_label = self.selfEsteemTab.question_widgets[f"SE_Q{question_num}_question"]
                no_label.setText(_translate("PsycheEval_MainWindow", str(question_num)))
                question_label.setText(_translate("PsycheEval_MainWindow", question_text))

                # Set text for depression questions
        for question_num, (a1_text, a2_text) in enumerate(self.DepressionTab.questions, start=1):
                no_label = self.DepressionTab.question_labels[f"DT_Q{question_num}"]
                a1_label = self.DepressionTab.a1_labels[f"DT_Q{question_num}_A1_Label"]
                a2_label = self.DepressionTab.a2_labels[f"DT_Q{question_num}_A2_Label"]

                no_label.setText(_translate("PsycheEval_MainWindow", str(question_num)))
                a1_label.setText(_translate("PsycheEval_MainWindow", a1_text))
                a2_label.setText(_translate("PsycheEval_MainWindow", a2_text))

                if question_num == 14:
                        a1_label_2 = self.DepressionTab.a1_labels[f"DT_Q{question_num}_A1_Label_2"]
                        a2_label_2 = self.DepressionTab.a2_labels[f"DT_Q{question_num}_A2_Label_2"]
                        a1_label_2.setText(_translate("PsycheEval_MainWindow", "negative and harmful to self"))
                        a2_label_2.setText(_translate("PsycheEval_MainWindow", "as opportunities for growth"))
                elif question_num == 15:
                        a1_label_2 = self.DepressionTab.a1_labels[f"DT_Q{question_num}_A1_Label_2"]
                        a2_label_2 = self.DepressionTab.a2_labels[f"DT_Q{question_num}_A2_Label_2"]
                        a1_label_2.setText(_translate("PsycheEval_MainWindow", "be better off if I weren’t here"))
                        a2_label_2.setText(_translate("PsycheEval_MainWindow", "I’m here)"))
                
                # Set the text for the buttons (1-5)
        for question_num in range(1, 16):  # Assuming there are 15 questions
                for btn_num in range(1, 6):
                        button = self.DepressionTab.buttons[f"DT_{question_num}_pushButton_{btn_num}"]
                        button.setText(_translate("PsycheEval_MainWindow", str(btn_num)))


        # Update the stress questions
        for question_num, question_text in enumerate(self.StressTab.questions, start=1):
            q_num_label = self.StressTab.question_widgets[f"ST_Q{question_num}_no_Label"]
            q_text_label = self.StressTab.question_widgets[f"ST_Q{question_num}_question"]
            q_num_label.setText(_translate("PsycheEval_MainWindow", str(question_num)))
            q_text_label.setText(_translate("PsycheEval_MainWindow", question_text))


        self.GeneralTab.GE_Student_Label.setText(_translate("PsycheEval_MainWindow", "Student Name:"))
        self.GeneralTab.GE_Age_Label.setText(_translate("PsycheEval_MainWindow", " Age:"))
        self.GeneralTab.GE_Sex_Label.setText(_translate("PsycheEval_MainWindow", "Sex:"))
        self.GeneralTab.GE_Sex_Male.setText(_translate("PsycheEval_MainWindow", "Male"))
        self.GeneralTab.GE_Female_Edit.setText(_translate("PsycheEval_MainWindow", "Female"))
        self.GeneralTab.GE_School_Label.setText(_translate("PsycheEval_MainWindow", "School:"))
        self.GeneralTab.GE_Date_Label.setText(_translate("PsycheEval_MainWindow", "Date:"))
        self.PreviewTab.GE_StudentName_Preview.setText(_translate("PsycheEval_MainWindow", "Student Name:"))
        self.PreviewTab.GE_Age_Preview.setText(_translate("PsycheEval_MainWindow", " Age:"))
        self.PreviewTab.GE_Sex_Preview.setText(_translate("PsycheEval_MainWindow", "Sex:"))
        self.PreviewTab.GE_School_Preview.setText(_translate("PsycheEval_MainWindow", "School:"))
        self.PreviewTab.GE_Date_Preview.setText(_translate("PsycheEval_MainWindow", "Date:"))
        self.PreviewTab.GE_StressTest_Preview.setText(_translate("PsycheEval_MainWindow", "Stress Test"))
        self.PreviewTab.GE_DepressionTest_Preview.setText(_translate("PsycheEval_MainWindow", "Depression Test"))
        self.PreviewTab.GE_SelfEsteemTest_Preview.setText(_translate("PsycheEval_MainWindow", "Self-Esteem Test"))
        self.menuFile.setTitle(_translate("PsycheEval_MainWindow", "File"))
        self.actionPrint.setText(_translate("PsycheEval_MainWindow", "Print"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PsycheEval_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PsycheEval_MainWindow()
    ui.setupUi(PsycheEval_MainWindow)
    PsycheEval_MainWindow.show()
    sys.exit(app.exec_())
