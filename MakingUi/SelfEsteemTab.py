from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup


class SelfEsteemTab:
    questions = [
        "I am a good and worthwhile person.",
        "I am as valuable a person as anyone else.",
        "I have good values that guide me in my life.",
        "When I look at my eyes in the mirror, I feel good about myself.",
        "I feel like I have done well in my life.",
        "I can laugh at myself.",
        "I like being me.",
        "I like myself, even when others reject me.",
        "Overall, I am pleased with how I am developing as a person.",
        "I love and support myself, regardless of what happens.",
        "I would rather be me than someone else.",
        "I respect myself.",
        "I continue to grow personally.",
        "I feel confident about my abilities.",
        "I have pride in who I am and what I do.",
        "I am comfortable in expressing my thoughts and feelings.",
        "I like my body.",
        "I handle difficult situations well.",
        "Overall, I make good decisions.",
        "I am a good friend and people like to be with me."
    ]

    def __init__(self, parent, stackedWidget, previewTab):
        self.stackedWidget = stackedWidget
        self.question_widgets = {}  # Dictionary to store question widgets
        self.button_groups = {}  # Dictionary to store button groups
        self.responses = [None] * 20  # List to store responses for each question
        self.setupSelfEsteemPage(parent)
        self.previewTab = previewTab  # Store the PreviewTab instance
        self.selfEsteem_savebutton.clicked.connect(self.save_data)


    def setupSelfEsteemPage(self, parent):
        self.SelfEsteem_Page = QtWidgets.QWidget()
        self.SelfEsteem_Page.setObjectName("SelfEsteem_Page")
        self.SelfEsteem_Page.setStyleSheet("#selfEsteem_instructions {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: rgb(24, 45, 83 ); /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"\n"
"\n"
"#selfEsteem_savebutton {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#selfEsteem_savebutton::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 150px; /* Width of the indicator */\n"
"    height: 150px; /* Height of the indicator */\n"
"}\n"
"\n"
"#selfEsteem_savebutton::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(C:/Users/colli/Downloads/MakingUi/icon/notsaved.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"#selfEsteem_savebutton::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(C:/Users/colli/Downloads/MakingUi/icon/saved.png); /* Absolute path to the checkmark image */\n"
"    \n"
"}")
        self._gridLayout = QtWidgets.QGridLayout(self.SelfEsteem_Page)
        self._gridLayout.setObjectName("_gridLayout")
        self.SelfEsteem_tabWidget = QtWidgets.QTabWidget(self.SelfEsteem_Page)
        self.SelfEsteem_tabWidget.setObjectName("SelfEsteem_tabWidget")
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(11)
        self.SelfEsteem_tabWidget.setFont(font)
        self.SelfEsteem_tabWidget.setStyleSheet("QTabWidget::pane {\n"
                                                "    border-top: 2px solid rgb(31, 149, 239);\n"
                                                "    border-radius: 5px;\n"
                                                "}\n"
                                                "QTabWidget::tab-bar {\n"
                                                "    left: 5px;\n"
                                                "}\n"
                                                "QTabBar::tab {\n"
                                                "    background-color: rgb(31, 149, 239);\n"
                                                "    color: white;\n"
                                                "    padding: 5px;\n"
                                                "    border: none;\n"
                                                "    min-width: 80px;\n"
                                                "    min-height: 30px;\n"
                                                "    margin-right: 2px;\n"
                                                "    border-top-left-radius: 5px;\n"
                                                "    border-top-right-radius: 5px;\n"
                                                "}\n"
                                                "QTabBar::tab:selected {\n"
                                                "    background-color: rgb(45, 45, 45);\n"
                                                "    border-top-left-radius: 5px;\n"
                                                "    border-top-right-radius: 5px;\n"
                                                "}\n"
                                                "QTabBar::tab:hover {\n"
                                                "    background-color: rgb(51, 169, 259);\n"
                                                "}")

                # Create two pages
        for page_num in range(1, 3):  # Pages 1 and 2
            page = QtWidgets.QWidget()
            page.setObjectName(f"SE_Tab_Page_{page_num}")
            page_layout = QtWidgets.QVBoxLayout(page)
            page_layout.setObjectName(f"SE_Tab_Page_{page_num}_verticalLayout")

            # Add the instructions label to the top of the first page
            if page_num == 1:
                self.selfEsteem_instructions = QtWidgets.QLabel(page)
                self.selfEsteem_instructions.setMinimumSize(QtCore.QSize(500, 50))
                self.selfEsteem_instructions.setMaximumSize(QtCore.QSize(500, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto ")
                font.setPointSize(-1)
                font.setBold(True)
                font.setWeight(75)
                self.selfEsteem_instructions.setFont(font)
                self.selfEsteem_instructions.setObjectName("selfEsteem_instructions")
                self.selfEsteem_instructions.setText("Rate how much you believe each statement from 1 to 5:")
                page_layout.addWidget(self.selfEsteem_instructions)

            # Create 10 questions per page
            for question_num in range(1, 11):
                total_question_num = (page_num - 1) * 10 + question_num
                self.createQuestion(page, page_layout, total_question_num)

            # Add the save button to the bottom of the second page
            if page_num == 2:
                self.selfEsteem_savebutton = QtWidgets.QCheckBox(page)
                self.selfEsteem_savebutton.setMinimumSize(QtCore.QSize(1168, 50))
                self.selfEsteem_savebutton.setMaximumSize(QtCore.QSize(1168, 50))
                self.selfEsteem_savebutton.setText("")
                self.selfEsteem_savebutton.setObjectName("selfEsteem_savebutton")
                page_layout.addWidget(self.selfEsteem_savebutton)

            self.SelfEsteem_tabWidget.addTab(page, f"Page {page_num}")

        self._gridLayout.addWidget(self.SelfEsteem_tabWidget, 0, 0, 1, 1)

    def createQuestion(self, parent, layout, question_num):
        question_layout = QtWidgets.QHBoxLayout()
        question_layout.setObjectName(f"SE_Q{question_num}_horizontal_question_lyt")
       
        # Question number label
        no_label = QtWidgets.QLabel(parent)
        no_label.setMinimumSize(QtCore.QSize(60, 60))
        no_label.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        no_label.setFont(font)
        no_label.setStyleSheet("QLabel {\n"
                               "    color: rgb(31, 149, 239);\n"
                               "    qproperty-alignment: AlignCenter;\n"
                               "    border: 3px solid rgb(31, 149, 239);\n"
                               "    border-radius: 10px;\n"
                               "}")
        no_label.setObjectName(f"SE_Q{question_num}_no_Label")
        no_label.setText(str(question_num))
        setattr(self, f"SE_Q{question_num}_no_Label", no_label)
        question_layout.addWidget(no_label)

        # Spacer
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        question_layout.addItem(spacer)

        # Question label
        question_label = QtWidgets.QLabel(parent)
        question_label.setMinimumSize(QtCore.QSize(800, 50))
        question_label.setMaximumSize(QtCore.QSize(800, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        question_label.setFont(font)
        question_label.setObjectName(f"SE_Q{question_num}_question")
        question_label.setText(self.questions[question_num - 1])
        setattr(self, f"SE_Q{question_num}_question", question_label)
        question_layout.addWidget(question_label)


        # Add widgets to the dictionary after they have been created
        self.question_widgets[f"SE_Q{question_num}_no_Label"] = no_label
        self.question_widgets[f"SE_Q{question_num}_question"] = question_label

        # Add widgets to the layout
       # question_layout.addWidget(no_label)
       # question_layout.addWidget(question_label)

        # Answer buttons layout
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.setSpacing(20)  # This sets the spacing between the buttons

        # Create a button group for this question
        button_group = QButtonGroup(parent)

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
            button_group.addButton(button)  # Add the button to the button group
        self.button_groups[question_num] = button_group  # Store the button group

        question_layout.addLayout(buttons_layout)

        self._gridLayout.addWidget(self.SelfEsteem_tabWidget, 0, 0, 1, 1)

        # Add the SelfEsteem_Page to the stackedWidget at a specific index
        index = 0  # Change this index to where you want to add the page in the stackedWidget
        self.stackedWidget.insertWidget(index, self.SelfEsteem_Page)


        layout.addLayout(question_layout)

        
        button_group.buttonClicked.connect(lambda btn, q_num=question_num: self.updateResponse(q_num, btn.text()))


    def updateResponse(self, question_num, response):
        self.responses[question_num - 1] = response


    def save_data(self):
        if self.selfEsteem_savebutton.isChecked():
            responses = []
            for question_num in range(1, 21):  # Assuming 20 questions
                button_group = self.button_groups[question_num]
                checked_button = button_group.checkedButton()
                if checked_button:
                    responses.append(checked_button.text())
                else:
                    responses.append(None)

            if None in responses:
                QtWidgets.QMessageBox.warning(self.SelfEsteem_Page, "Incomplete Information",
                                              "Please answer all questions before saving.")
                self.selfEsteem_savebutton.setChecked(False)
                return

            # Update the preview tab with the new data
            self.previewTab.shared_data['selfEsteemResponses'] = responses
            self.previewTab.updatePreview()