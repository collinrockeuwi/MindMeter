from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup



class DepressionTab:
    questions = [
        ("Low energy", "High Energy"),
        ("Difficulty sleeping or sleep all the time", "Uninterrupted sleeping patterns"),
        ("No desire to be involved in activities", "Very involved in activities"),
        ("No desire for sex", "Healthy sex drive"),
        ("Aches and pain", "Feel great"),
        ("Loss of appetite", "Enjoy eating"),
        ("Sad (tearful)", "Joyful"),
        ("Despairing and hopeless", "Hopeful about the future"),
        ("Irritable (low frustration tolerance)", "Patient-high frustration tolerance"),
        ("Withdrawn", "Involved"),
        ("Mental anguish", "Peace of mind"),
        ("Low sense of self-worth", "High sense of self-worth"),
        ("Pessimistic about the future", "Optimistic about the future"),
        ("Perceive most circumstances as", "Perceive most circumstances"),
        ("Self-destructive (I and others would", "Self-preserving (I’m glad")
    ]

    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.stackedWidget.setMinimumSize(QtCore.QSize(1643, 868))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1643, 868))
        self.question_labels = {}
        self.a1_labels = {}  # Add this line
        self.a2_labels = {}  # Add this line
        self.buttons = {}    # Initialize the buttons dictionary
        self.setupDepressionPage(parent)

        
                

    def setupDepressionPage(self, parent):
        self.Depression_Page = QtWidgets.QWidget()
        self.Depression_Page.setStyleSheet("#depression_instructions {\n"
"    font-family: \'Roboto \';\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: rgb(24, 45, 83 ); /* Set the font color to white */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"\n"
"\n"
"#depression_savebutton {\n"
"    /* General styling for the checkbox */\n"
"    font-family: \'Roboto\';\n"
"    color: rgb(24, 45, 83); /* Text color */\n"
"    font-size: 16px; /* Font size */\n"
"    spacing: 5px; /* Space between the indicator and the text */\n"
"    background-color: transparent; /* Make the background transparent */\n"
"}\n"
"\n"
"#depression_savebutton::indicator {\n"
"    /* Styling for the indicator (the square part) */\n"
"    width: 150px; /* Width of the indicator */\n"
"    height: 150px; /* Height of the indicator */\n"
"}\n"
"\n"
"#depression_savebutton::indicator::unchecked {\n"
"    /* Styling for the indicator when the checkbox is unchecked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"     image: url(C:/Users/colli/Downloads/MakingUi/icon/notsaved.png); /* Absolute path to the checkmark image */\n"
"}\n"
"\n"
"\n"
"\n"
"#depression_savebutton::indicator::checked {\n"
"    /* Styling for the indicator when the checkbox is checked */\n"
"    background-color: transparent; /* Background color */\n"
"    border: transparent; /* Border color and width */\n"
"    border-radius: 4px; /* Optional: if you want rounded corners for the square */\n"
"    image: url(C:/Users/colli/Downloads/MakingUi/icon/saved.png); /* Absolute path to the checkmark image */\n"
"    \n"
"}")
        self.Depression_Page.setObjectName("Depression_Page")
        self.Depression_Page_gridLayout = QtWidgets.QGridLayout(self.Depression_Page)
        self.Depression_Page_gridLayout.setObjectName("Depression_Page_gridLayout")
        self.Depression_Page_tabWidget = QtWidgets.QTabWidget(self.Depression_Page)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(11)
        self.Depression_Page_tabWidget.setFont(font)
        self.Depression_Page_tabWidget.setStyleSheet("QTabWidget::pane {\n"
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
        self.Depression_Page_tabWidget.setObjectName("Depression_Page_tabWidget")

                # Create two pages (page 1 and page 2)
        for page_num in range(1, 3):
            page = QtWidgets.QWidget()
            page.setObjectName(f"DT_page_{page_num}")
            # Here, apply the layout properties to each page's QVBoxLayout
            page_layout = QtWidgets.QVBoxLayout(page)
            page_layout.setContentsMargins(11, 11, 11, 11)  # Set all margins to 11
            page_layout.setSpacing(7)  # Set the spacing between widgets in the layout to 7
            page_layout.setObjectName(f"DT_page_{page_num}_verticalLayout")

            # Add the instructions label to the top of the first page
            if page_num == 1:
                self.depression_instructions = QtWidgets.QLabel(page)
                self.depression_instructions.setMinimumSize(QtCore.QSize(1168, 50))
                self.depression_instructions.setMaximumSize(QtCore.QSize(1168, 50))
                self.depression_instructions.setObjectName("depression_instructions")
                self.depression_instructions.setText("Click the number that best describes you:")
                page_layout.addWidget(self.depression_instructions)

            # Determine the number of questions for the current page
            num_questions = 10 if page_num == 1 else 5

            # Create questions for the current page
            for question_num in range(1, num_questions + 1):
                total_question_num = (page_num - 1) * 10 + question_num

                # Special handling for questions 14 and 15
                if total_question_num in [14, 15]:
                    self.createSpecialQuestion(page, page_layout, total_question_num)
                else:
                    self.createQuestion(page, page_layout, total_question_num)

            # Add the save button to the bottom of the second page
            if page_num == 2:
                self.depression_savebutton = QtWidgets.QCheckBox(page)
                self.depression_savebutton.setMinimumSize(QtCore.QSize(1168, 50))
                self.depression_savebutton.setMaximumSize(QtCore.QSize(1168, 50))
                self.depression_savebutton.setText("")
                self.depression_savebutton.setObjectName("depression_savebutton")
                page_layout.addWidget(self.depression_savebutton)

            self.Depression_Page_tabWidget.addTab(page, f"Page {page_num}")

            # Set the current index to the first page
        

         


            

        self.Depression_Page_gridLayout.addWidget(self.Depression_Page_tabWidget, 0, 0, 1, 1)
                # Add the Depression_Page to the stackedWidget at a specific index
        index = 1  # Change this index to where you want to add the page in the stackedWidget
        
        self.stackedWidget.insertWidget(index, self.Depression_Page)

        

    def createQuestion(self, parent, layout, question_num):
                # Create a horizontal layout for the question
                question_layout = QtWidgets.QHBoxLayout()
                question_layout.setContentsMargins(0, 0, 0, 0)  # Set all margins to 0
                question_layout.setSpacing(7)  # Set the spacing between widgets in the layout to 7
                question_layout.setObjectName(f"DT_Q{question_num}_horizontal_question_lyt")

                # Create the question number label
                question_number = QtWidgets.QLabel(parent)
                question_number.setMinimumSize(QtCore.QSize(60, 60))
                question_number.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                question_number.setFont(font)
                question_number.setStyleSheet("QLabel {\n"
                                                "    color: rgb(31, 149, 239);\n"
                                                "    qproperty-alignment: AlignCenter;\n"
                                                "    border: 3px solid rgb(31, 149, 239);\n"
                                                "    border-radius: 10px;\n"
                                                "}")
                question_number.setObjectName(f"DT_Q{question_num}")
                question_number.setText(str(question_num))
                question_layout.addWidget(question_number)

                # Spacer
                spacer1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                question_layout.addItem(spacer1)

                # Create the question label
                question_label = QtWidgets.QLabel(parent)
                question_label.setMinimumSize(QtCore.QSize(475, 50))
                question_label.setMaximumSize(QtCore.QSize(400, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                question_label.setFont(font)
                question_label.setObjectName(f"DT_Q{question_num}_A1_Label")
                question_label.setText(self.questions[question_num - 1][0])  # Set the text from the questions list
                question_layout.addWidget(question_label)

                # Spacer
                spacer2 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                question_layout.addItem(spacer2)

                # Create the selection layout for the answer options
                selection_layout = QtWidgets.QHBoxLayout()
                selection_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
                selection_layout.setSpacing(20)
                selection_layout.setObjectName(f"DT_Q{question_num}_horizontal_selection_lyt")

                # Create a button group for this question
                button_group = QButtonGroup(parent)
                
                # Create answer option buttons
                for i in range(1, 6):
                        button = QtWidgets.QPushButton(parent)
                        button.setMinimumSize(QtCore.QSize(60, 55))
                        button.setMaximumSize(QtCore.QSize(60, 55))
                        button.setCheckable(True)
                        button.setAutoExclusive(True)
                        button.setObjectName(f"DT_{question_num}_pushButton_{i}")
                        button.setText(str(i))
                        button.setStyleSheet("""
                                QPushButton {
                                color: white;
                                text-align: center;
                                height: 70px;
                                border: 1px;
                                border-radius: 8px;
                                background-color: rgb(31, 149, 239);
                                font-size: 35px;
                                }
                                QPushButton:hover {
                                background-color: rgb(45, 45, 45);
                                color: rgb(220, 220, 220);
                                }
                                QPushButton:checked {
                                background-color: rgb(45, 45, 45);
                                }
                        """)
                        selection_layout.addWidget(button)
                        button_group.addButton(button)  # Add the button to the button group

                        # Add the button to the dictionary
                        self.buttons[f"DT_{question_num}_pushButton_{i}"] = button

                        question_layout.addLayout(selection_layout)

                # Spacer
                spacer3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                question_layout.addItem(spacer3)

                # Create the second question label (for the opposite end of the scale)
                question_label_2 = QtWidgets.QLabel(parent)
                question_label_2.setMinimumSize(QtCore.QSize(400, 50))
                question_label_2.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                question_label_2.setFont(font)
                question_label_2.setObjectName(f"DT_Q{question_num}_A2_Label")
                question_label_2.setText(self.questions[question_num - 1][1])  # Set the text from the questions list
                question_layout.addWidget(question_label_2)

                # Add the question layout to the parent layout
                layout.addLayout(question_layout)

                # Add the label to the dictionary
                self.question_labels[f"DT_Q{question_num}"] = question_number
                self.a1_labels[f"DT_Q{question_num}_A1_Label"] = question_label
                self.a2_labels[f"DT_Q{question_num}_A2_Label"] = question_label_2

                                # Refresh the layout
                layout.update()
                layout.activate()



    def createSpecialQuestion(self, parent, layout, question_num):
        # Create a horizontal layout for the question
        question_layout = QtWidgets.QHBoxLayout()
        question_layout.setContentsMargins(0, 0, 0, 0)  # Set all margins to 0
        question_layout.setSpacing(7)  # Set the spacing between widgets in the layout to 7
        question_layout.setObjectName(f"DT_Q{question_num}_horizontal_question_lyt")

        # Create the question number label
        question_number = QtWidgets.QLabel(parent)
        question_number.setMinimumSize(QtCore.QSize(60, 60))
        question_number.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(14)
        question_number.setFont(font)
        question_number.setStyleSheet("QLabel {\n"
                                        "     color: rgb(31, 149, 239);\n"
                                        "    qproperty-alignment: AlignCenter;\n"
                                        "    border: 3px solid rgb(31, 149, 239);\n"
                                        "    border-radius: 10px;\n"
                                        "}")
        question_number.setObjectName(f"DT_Q{question_num}")
        question_number.setText(str(question_num))
        question_layout.addWidget(question_number)

        # Spacer
        spacer1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        question_layout.addItem(spacer1)

        # Create a grid layout for the two-part question label
        question_label_grid = QtWidgets.QGridLayout()
        question_label_grid.setVerticalSpacing(0)
        question_label_grid.setObjectName(f"DT_Q{question_num}_A1_gridLayout")

        # Create the first part of the question label
        question_label_1 = QtWidgets.QLabel(parent)
        question_label_1.setMinimumSize(QtCore.QSize(430, 40))
        question_label_1.setMaximumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        question_label_1.setFont(font)
        question_label_1.setObjectName(f"DT_Q{question_num}_A1_Label")
        question_label_1.setText(self.questions[question_num - 1][0].split(" (")[0])  # Split the text to get the first part
        question_label_grid.addWidget(question_label_1, 0, 0, 1, 1)

        # Create the second part of the question label
        question_label_2 = QtWidgets.QLabel(parent)
        question_label_2.setMinimumSize(QtCore.QSize(430, 40))
        question_label_2.setMaximumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        question_label_2.setFont(font)
        question_label_2.setObjectName(f"DT_Q{question_num}_A1_Label_2")
        question_label_2_parts = self.questions[question_num - 1][0].split(" (")
        question_label_2_text = question_label_2_parts[1][:-1] if len(question_label_2_parts) > 1 else ""
        question_label_2.setText(question_label_2_text)  # Split the text to get the second part, or set empty if not present
        question_label_grid.addWidget(question_label_2, 1, 0, 1, 1)

        question_layout.addLayout(question_label_grid)

        # Spacer
        spacer2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        question_layout.addItem(spacer2)

        # Create the selection layout for the answer options
        selection_layout = QtWidgets.QHBoxLayout()
        selection_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        selection_layout.setSpacing(20)
        selection_layout.setObjectName(f"DT_Q{question_num}_horizontal_selection_lyt")

         #Create a button group for this question
        button_group = QButtonGroup(parent)
        
        # Create answer option buttons
        for i in range(1, 6):
                button = QtWidgets.QPushButton(parent)
                button.setMinimumSize(QtCore.QSize(60, 55))
                button.setMaximumSize(QtCore.QSize(60, 55))
                button.setCheckable(True)
                button.setAutoExclusive(True)
                button.setObjectName(f"DT_{question_num}_pushButton_{i}")
                button.setText(str(i))
                selection_layout.addWidget(button)
                button_group.addButton(button)  # Add the button to the button group
                button.setStyleSheet("""
                                QPushButton {
                                color: white;
                                text-align: center;
                                height: 70px;
                                border: 1px;
                                border-radius: 8px;
                                background-color: rgb(31, 149, 239);
                                font-size: 35px;
                                }
                                QPushButton:hover {
                                background-color: rgb(45, 45, 45);
                                color: rgb(220, 220, 220);
                                }
                                QPushButton:checked {
                                background-color: rgb(45, 45, 45);
                                }
                        """)

                # Add the button to the dictionary
                self.buttons[f"DT_{question_num}_pushButton_{i}"] = button

        question_layout.addLayout(selection_layout)

        # Spacer
        spacer3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        question_layout.addItem(spacer3)

        # Create a grid layout for the two-part opposite question label
        opposite_question_label_grid = QtWidgets.QGridLayout()
        opposite_question_label_grid.setObjectName(f"DT_Q{question_num}_A2_gridLayout")

        # Create the first part of the opposite question label
        opposite_question_label_1 = QtWidgets.QLabel(parent)
        opposite_question_label_1.setMinimumSize(QtCore.QSize(475, 40))
        opposite_question_label_1.setMaximumSize(QtCore.QSize(475, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        opposite_question_label_1.setFont(font)
        opposite_question_label_1.setObjectName(f"DT_Q{question_num}_A2_Label")
        opposite_question_label_1.setText(self.questions[question_num - 1][1].split(" (")[0])  # Split the text to get the first part
        opposite_question_label_grid.addWidget(opposite_question_label_1, 0, 0, 1, 1)

        # Create the second part of the opposite question label
        opposite_question_label_2 = QtWidgets.QLabel(parent)
        opposite_question_label_2.setMinimumSize(QtCore.QSize(475, 40))
        opposite_question_label_2.setMaximumSize(QtCore.QSize(475, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        opposite_question_label_2.setFont(font)
        opposite_question_label_2.setObjectName(f"DT_Q{question_num}_A2_Label_2")
        opposite_question_label_2_parts = self.questions[question_num - 1][1].split(" (")
        opposite_question_label_2_text = opposite_question_label_2_parts[1][:-1] if len(opposite_question_label_2_parts) > 1 else ""
        opposite_question_label_2.setText(opposite_question_label_2_text)  # Split the text to get the second part, or set empty if not present
        opposite_question_label_grid.addWidget(opposite_question_label_2, 1, 0, 1, 1)

        question_layout.addLayout(opposite_question_label_grid)

        # Add the question layout to the parent layout
        layout.addLayout(question_layout)

        # Add the label to the dictionary
        self.question_labels[f"DT_Q{question_num}"] = question_number
        self.a1_labels[f"DT_Q{question_num}_A1_Label"] = question_label_1
        self.a2_labels[f"DT_Q{question_num}_A2_Label"] = opposite_question_label_1
        self.a1_labels[f"DT_Q{question_num}_A1_Label_2"] = question_label_2
        self.a2_labels[f"DT_Q{question_num}_A2_Label_2"] = opposite_question_label_2

            # Refresh the layout
        layout.update()
        layout.activate()