from PyQt5 import QtCore, QtGui, QtWidgets

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

    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.question_widgets = {}  # Dictionary to store question widgets
        self.setupSelfEsteemPage(parent)

    def setupSelfEsteemPage(self, parent):
        self.SelfEsteem_Page = QtWidgets.QWidget()
        self.SelfEsteem_Page.setObjectName("SelfEsteem_Page")
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

            # Create 10 questions per page
            for question_num in range(1, 11):
                total_question_num = (page_num - 1) * 10 + question_num
                self.createQuestion(page, page_layout, total_question_num)

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


        # Slider
        slider = QtWidgets.QSlider(parent)
        slider.setMinimumSize(QtCore.QSize(351, 71))
        slider.setMaximumSize(QtCore.QSize(351, 71))
        slider.setMaximum(20)
        slider.setPageStep(5)
        slider.setOrientation(QtCore.Qt.Horizontal)
        slider.setStyleSheet("QSlider::groove:horizontal {\n"
                            "    border: 1px solid #999999;\n"
                            "    height: 30px;\n"
                            "    background: white;\n"
                            "    margin: 2px 0;\n"
                            "    border-radius: 4px;\n"
                            "}\n"
                            "QSlider::handle:horizontal {\n"
                            "    background: rgb(31, 149, 239);\n"
                            "    border: none;\n"
                            "    width: 60px;\n"
                            "    margin: -2px 0;\n"
                            "    border-radius: 5px;\n"
                            "    position: absolute;\n"
                            "}\n"
                            "QSlider::handle:horizontal:hover {\n"
                            "    background: rgb(45, 45, 45);\n"
                            "}\n"
                            "QSlider::handle:horizontal:pressed {\n"
                            "    background: rgb(31, 149, 239);\n"
                            "}\n"
                            "QSlider::sub-page:horizontal {\n"
                            "    background: rgb(31, 149, 239);\n"
                            "    border-radius: 4px;\n"
                            "}\n"
                            "QSlider::add-page:horizontal {\n"
                            "    background: white;\n"
                            "    border-radius: 4px;\n"
                            "}")
        slider.setObjectName(f"SE_Q{question_num}_horizontalSlider")
        setattr(self, f"SE_Q{question_num}_horizontalSlider", slider)
        question_layout.addWidget(slider)

        # SpinBox
        spin_box = QtWidgets.QSpinBox(parent)
        spin_box.setMinimumSize(QtCore.QSize(90, 60))
        spin_box.setMaximumSize(QtCore.QSize(90, 60))
        spin_box.setMaximum(20)
        font = QtGui.QFont()
        font.setFamily("Roboto Bk")
        font.setPointSize(20)
        spin_box.setFont(font)
        spin_box.setStyleSheet("QSpinBox {\n"
                            "    background-color: white;\n"
                            "    color: black;\n"
                            "    border: 2px solid black;\n"
                            "    border-radius: 5px;\n"
                            "    padding-left: 20px;\n"
                            "    margin: 2px;\n"
                            "}\n"
                            "QSpinBox::up-button {\n"
                            "    subcontrol-origin: border;\n"
                            "    subcontrol-position: top right;\n"
                            "    width: 15px;\n"
                                                       "    border-left: 1px solid black;\n"
                           "}\n"
                           "QSpinBox::down-button {\n"
                           "    subcontrol-origin: border;\n"
                           "    subcontrol-position: bottom right;\n"
                           "    width: 15px;\n"
                           "    border-left: 1px solid black;\n"
                           "}\n"
                           "QSpinBox::up-arrow {\n"
                           "    width: 7px;\n"
                           "    height: 7px;\n"
                           "    image: url(:/icon/icon/menu-4-32.ico);\n"
                           "}\n"
                           "QSpinBox::down-arrow {\n"
                           "    width: 7px;\n"
                           "    height: 7px;\n"
                           "    image: url(:/icon/icon/menu-4-32.ico);\n"
                           "}\n"
                           "QSpinBox::up-button:pressed {\n"
                           "    background-color: lightgray;\n"
                           "}\n"
                           "QSpinBox::down-button:pressed {\n"
                           "    background-color: lightgray;\n"
                           "}\n"
                           "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
                           "    background-color: #e0e0e0;\n"
                           "}")
        spin_box.setObjectName(f"SE_Q{question_num}_spinBox")
        setattr(self, f"SE_Q{question_num}_spinBox", spin_box)
        question_layout.addWidget(spin_box)

        self._gridLayout.addWidget(self.SelfEsteem_tabWidget, 0, 0, 1, 1)

        # Add the SelfEsteem_Page to the stackedWidget at a specific index
        index = 0  # Change this index to where you want to add the page in the stackedWidget
        self.stackedWidget.insertWidget(index, self.SelfEsteem_Page)


        layout.addLayout(question_layout)
