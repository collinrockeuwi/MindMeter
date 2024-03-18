from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup


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
        self.Stress_Page.setStyleSheet("#stress_instructions {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: rgb(24, 45, 83 ); /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"")
        self.Stress_Page_gridLayout = QtWidgets.QGridLayout(self.Stress_Page)
        self.Stress_Page_gridLayout.setObjectName("Stress_Page_gridLayout")
        self.Stress_Page_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Stress_Page_gridLayout.setSpacing(0)

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
        self.Stress_tabWidget.setMinimumSize(QtCore.QSize(1550, 800))
        self.Stress_tabWidget.setMaximumSize(QtCore.QSize(1550, 800))

        self.ST_Tab = QtWidgets.QWidget()
        self.ST_Tab.setObjectName("ST_Tab")
        self.ST_Tab_gridLayout = QtWidgets.QVBoxLayout(self.ST_Tab)
        self.ST_Tab_gridLayout.setObjectName("ST_Tab_gridLayout")



    #instruction heading
        #question layout
        self.st_instructions = QtWidgets.QHBoxLayout()
        self.st_instructions.setObjectName("instructions")

        #spacer item
        self.stress_instructions = QtWidgets.QLabel(self.ST_Tab)
        self.stress_instructions.setMinimumSize(QtCore.QSize(340, 50))
        self.stress_instructions.setMaximumSize(QtCore.QSize(340, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto ")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.stress_instructions.setFont(font)
        self.stress_instructions.setObjectName("stress_instructions")
        self.st_instructions.addWidget(self.stress_instructions)
        spacerItem69 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.st_instructions.addItem(spacerItem69)


        self.ST_instruction_lyt = QtWidgets.QHBoxLayout()
        self.ST_instruction_lyt.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ST_instruction_lyt.setSpacing(0)
        self.ST_instruction_lyt.setObjectName("ST_instruction_lyt")
        spacerItem70 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ST_instruction_lyt.addItem(spacerItem70)
        self.Never_Label = QtWidgets.QLabel(self.ST_Tab)
        self.Never_Label.setMinimumSize(QtCore.QSize(40, 30))
        self.Never_Label.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(8)

        font.setWeight(50)
        self.Never_Label.setFont(font)
        self.Never_Label.setObjectName("Never_Label")
        self.ST_instruction_lyt.addWidget(self.Never_Label)
        spacerItem71 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ST_instruction_lyt.addItem(spacerItem71)
        self.AlmostNever_label = QtWidgets.QLabel(self.ST_Tab)
        self.AlmostNever_label.setMinimumSize(QtCore.QSize(80, 30))
        self.AlmostNever_label.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.AlmostNever_label.setFont(font)
        self.AlmostNever_label.setObjectName("AlmostNever_label")
        self.ST_instruction_lyt.addWidget(self.AlmostNever_label)
        spacerItem72 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ST_instruction_lyt.addItem(spacerItem72)
        self.Sometimes_label = QtWidgets.QLabel(self.ST_Tab)
        self.Sometimes_label.setMinimumSize(QtCore.QSize(70, 30))
        self.Sometimes_label.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Sometimes_label.setFont(font)
        self.Sometimes_label.setObjectName("Sometimes_label")
        self.ST_instruction_lyt.addWidget(self.Sometimes_label)
        spacerItem73 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ST_instruction_lyt.addItem(spacerItem73)
        self.FairlyOften_label = QtWidgets.QLabel(self.ST_Tab)
        self.FairlyOften_label.setMinimumSize(QtCore.QSize(70, 30))
        self.FairlyOften_label.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.FairlyOften_label.setFont(font)
        self.FairlyOften_label.setObjectName("FairlyOften_label")
        self.ST_instruction_lyt.addWidget(self.FairlyOften_label)
        spacerItem74 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ST_instruction_lyt.addItem(spacerItem74)
        self.VeryOften_label = QtWidgets.QLabel(self.ST_Tab)
        self.VeryOften_label.setMinimumSize(QtCore.QSize(70, 30))
        self.VeryOften_label.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.VeryOften_label.setFont(font)
        self.VeryOften_label.setObjectName("VeryOften_label")
        self.ST_instruction_lyt.addWidget(self.VeryOften_label)
        spacerItem75 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ST_instruction_lyt.addItem(spacerItem75)
        self.st_instructions.addLayout(self.ST_instruction_lyt)

        #Add to layout with all of the questions
        self.ST_Tab_gridLayout.addLayout(self.st_instructions)




        # Create a dictionary to store button groups for each question
        self.button_groups = {}


        # Create a single page with 10 questions
        for i, question_text in enumerate(self.questions, start=1):
            self.createQuestion(self.ST_Tab, self.ST_Tab_gridLayout, i, question_text)

#save button
        self.ST_Q10_horizontal_question_lyt_2 = QtWidgets.QHBoxLayout()
        self.ST_Q10_horizontal_question_lyt_2.setObjectName("ST_Q10_horizontal_question_lyt_2")
        self.stress_savebutton = QtWidgets.QCheckBox(self.ST_Tab)
        self.stress_savebutton.setMinimumSize(QtCore.QSize(150, 40))
        self.stress_savebutton.setMaximumSize(QtCore.QSize(40, 100))
        self.stress_savebutton.setStyleSheet("#stress_savebutton {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#stress_savebutton::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 150px; /* Width of the indicator */\n"
"    height: 150px; /* Height of the indicator */\n"
"}\n"
"\n"
"#stress_savebutton::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(C:/Users/colli/Downloads/MakingUi/icon/notsaved.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"#stress_savebutton::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(C:/Users/colli/Downloads/MakingUi/icon/saved.png); /* Absolute path to the checkmark image */\n"
"    \n"
"}")
        self.stress_savebutton.setText("")
        self.stress_savebutton.setObjectName("stress_savebutton")
        self.ST_Q10_horizontal_question_lyt_2.addWidget(self.stress_savebutton)
        self.ST_Tab_gridLayout.addLayout(self.ST_Q10_horizontal_question_lyt_2)


#Tab and stacked widget
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


        # Create a button group for this question
        self.button_groups[question_num] = QButtonGroup(parent)
        


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
            # Add the button to the button group for this question
            self.button_groups[question_num].addButton(button)
            buttons_layout.addWidget(button)


        # Now, add the buttons layout to the main question layout
        question_layout.addLayout(buttons_layout)
        layout.addLayout(question_layout)

        # Store widgets in the dictionary for access when translating UI
        self.question_widgets[f"ST_Q{question_num}_no_Label"] = q_num_label
        self.question_widgets[f"ST_Q{question_num}_question"] = q_text_label
