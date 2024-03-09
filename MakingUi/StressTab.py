from PyQt5 import QtCore, QtGui, QtWidgets

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

    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.question_widgets = {}  # Dictionary to store question widgets
        self.setupStressPage(parent)

    def setupStressPage(self, parent):
        self.Stress_Page = QtWidgets.QWidget()
        self.Stress_Page.setObjectName("Stress_Page")
        self.Stress_Page_gridLayout = QtWidgets.QGridLayout(self.Stress_Page)
        self.Stress_Page_gridLayout.setObjectName("Stress_Page_gridLayout")
        self.Stress_tabWidget = QtWidgets.QTabWidget(self.Stress_Page)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(11)
        self.Stress_tabWidget.setFont(font)
        self.Stress_tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    /* The tab widget frame */\n"
"    border-top: 2px solid rgb(31, 149, 239);\n"
"    border-radius: 5px; /* Rounded corners for the pane */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    /* The tab bar */\n"
"    left: 5px; /* Move the bar to the right */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    /* The tab */\n"
"    background-color: rgb(31, 149, 239);\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    min-width: 80px; /* Set the minimum width of the tab */\n"
"    min-height: 30px; /* Set the minimum height of the tab */\n"
"    margin-right: 2px; /* Space between tabs */\n"
"    border-top-left-radius: 5px; /* Rounded top-left corner */\n"
"    border-top-right-radius: 5px; /* Rounded top-right corner */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    /* The selected tab */\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-top-left-radius: 5px; /* Maintain rounded corner when selected */\n"
"    border-top-right-radius: 5px; /* Maintain rounded corner when selected */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    /* The tab when hovered over */\n"
"    background-color: rgb(51, 169, 259);\n"
"}\n"
"")
        self.Stress_tabWidget.setObjectName("Stress_tabWidget")

        self.ST_Tab = QtWidgets.QWidget()
        self.ST_Tab.setObjectName("ST_Tab")
        self.ST_Tab_gridLayout = QtWidgets.QVBoxLayout(self.ST_Tab)
        self.ST_Tab_gridLayout.setObjectName("ST_Tab_gridLayout")

        # Create a single page with 10 questions
        for i, question_text in enumerate(self.questions, start=1):
            self.createQuestion(self.ST_Tab, self.ST_Tab_gridLayout, i, question_text)

        self.Stress_tabWidget.addTab(self.ST_Tab, "Page 1")
        self.Stress_Page_gridLayout.addWidget(self.Stress_tabWidget)
        self.stackedWidget.insertWidget(2, self.Stress_Page)  # Adjust the index as needed

    def createQuestion(self, parent, layout, question_num, question_text):
        question_layout = QtWidgets.QHBoxLayout()
        question_layout.setObjectName(f"ST_Q{question_num}_horizontalLayout")
        
        # Question number label
        q_num_label = QtWidgets.QLabel(parent)
        q_num_label.setMinimumSize(QtCore.QSize(60, 60))
        q_num_label.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        q_num_label.setFont(font)
        q_num_label.setText(str(question_num))
        question_layout.addWidget(q_num_label)
        q_num_label.setStyleSheet("QLabel {\n"
"     color: rgb(31, 149, 239);\n"
"    qproperty-alignment: AlignCenter;\n"
"   \n"
"    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
"    border-radius: 10px; /* Optional: if you want rounded corners */\n"
"}\n"
"")

        # Spacer
        question_layout.addItem(QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))

        # Question text label
        q_text_label = QtWidgets.QLabel(parent)
        q_text_label.setMinimumSize(QtCore.QSize(825, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        q_text_label.setFont(font)
        q_text_label.setText(question_text)
        question_layout.addWidget(q_text_label)



        
        # Answer buttons layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.setSpacing(20)  # This sets the spacing between the buttons


        # Answer buttons
        for i in range(5):  # Assuming 5 answer options
            button = QtWidgets.QPushButton(parent)
            button.setMinimumSize(QtCore.QSize(60, 55))
            button.setMaximumSize(QtCore.QSize(60, 55))
            button.setCheckable(True)
            button.setAutoExclusive(True)
            button.setObjectName(f"ST_{question_num}_pushButton_{i+1}")
            button.setText(str(i + 1))
            button.setStyleSheet("QPushButton {\n"
                                 "    color: white;\n"
                                 "    background-color: #1F95EF;\n"
                                 "    font-size: 35px;\n"
                                 "    border-radius: 8px;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #2D2D2D;\n"
                                 "    color: #DCDCDC;\n"
                                 "}\n"
                                 "QPushButton:checked {\n"
                                 "    background-color: #2D2D2D;\n"
                                 "}\n")
            buttons_layout.addWidget(button)


        # Now, add the buttons layout to the main question layout
        question_layout.addLayout(buttons_layout)
        layout.addLayout(question_layout)

        # Store widgets in the dictionary for access when translating UI
        self.question_widgets[f"ST_Q{question_num}_no_Label"] = q_num_label
        self.question_widgets[f"ST_Q{question_num}_question"] = q_text_label
