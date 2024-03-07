from PyQt5 import QtCore, QtGui, QtWidgets        



class SelfEsteemTab:
    def __init__(self, parent, stackedWidget):
        self.stackedWidget = stackedWidget
        self.setupSelfEsteemPage(parent)
        

    def setupSelfEsteemPage(self, parent):
                self.SelfEsteem_Page = QtWidgets.QWidget()
                self.SelfEsteem_Page.setObjectName("SelfEsteem_Page")
                self._gridLayout = QtWidgets.QGridLayout(self.SelfEsteem_Page)
                self._gridLayout.setObjectName("_gridLayout")
                self.SelfEsteem_tabWidget = QtWidgets.QTabWidget(self.SelfEsteem_Page)
                font = QtGui.QFont()
                font.setFamily("Roboto Cn")
                font.setPointSize(11)
                self.SelfEsteem_tabWidget.setFont(font)
                self.SelfEsteem_tabWidget.setStyleSheet("QTabWidget::pane {\n"
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
                self.SelfEsteem_tabWidget.setObjectName("SelfEsteem_tabWidget")
                self.SE_Tab_Page_1 = QtWidgets.QWidget()
                self.SE_Tab_Page_1.setStyleSheet("QLabel {\n"
        "\n"
        " \n"
        "   \n"
        "    \n"
        "}\n"
        "")
                self.SE_Tab_Page_1.setObjectName("SE_Tab_Page_1")
                self.SE_Tab_Page_verticalLayout = QtWidgets.QVBoxLayout(self.SE_Tab_Page_1)
                self.SE_Tab_Page_verticalLayout.setObjectName("SE_Tab_Page_verticalLayout")
                self.SE_Q1_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q1_horizontal_question_lyt.setObjectName("SE_Q1_horizontal_question_lyt")
                self.SE_Q1_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q1_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q1_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q1_no_Label.setFont(font)
                self.SE_Q1_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q1_no_Label.setObjectName("SE_Q1_no_Label")
                self.SE_Q1_horizontal_question_lyt.addWidget(self.SE_Q1_no_Label)
                spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q1_horizontal_question_lyt.addItem(spacerItem4)
                self.SE_Q1_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q1_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q1_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q1_question.setFont(font)
                self.SE_Q1_question.setObjectName("SE_Q1_question")




                self.SE_Q1_horizontal_question_lyt.addWidget(self.SE_Q1_question)
                self.SE_Q1_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q1_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q1_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q1_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q1_horizontalSlider.setMaximum(20)
                self.SE_Q1_horizontalSlider.setPageStep(5)
                self.SE_Q1_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q1_horizontalSlider.setObjectName("SE_Q1_horizontalSlider")
                self.SE_Q1_horizontal_question_lyt.addWidget(self.SE_Q1_horizontalSlider)



                self.SE_1_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_1_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_1_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_1_spinBox.setFont(font)
                self.SE_1_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_1_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_1_spinBox.setMaximum(20)
                self.SE_1_spinBox.setObjectName("SE_1_spinBox")
                self.SE_Q1_horizontal_question_lyt.addWidget(self.SE_1_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q1_horizontal_question_lyt)

                
                self.SE_Q2_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q2_horizontal_question_lyt.setObjectName("SE_Q2_horizontal_question_lyt")
                self.SE_Q2_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q2_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q2_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q2_no_Label.setFont(font)
                self.SE_Q2_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q2_no_Label.setObjectName("SE_Q2_no_Label")
                self.SE_Q2_horizontal_question_lyt.addWidget(self.SE_Q2_no_Label)
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q2_horizontal_question_lyt.addItem(spacerItem5)
                self.SE_Q2_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q2_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q2_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q2_question.setFont(font)
                self.SE_Q2_question.setObjectName("SE_Q2_question")
                self.SE_Q2_horizontal_question_lyt.addWidget(self.SE_Q2_question)
                self.SE_Q2_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q2_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q2_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q2_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q2_horizontalSlider.setMaximum(20)
                self.SE_Q2_horizontalSlider.setPageStep(5)
                self.SE_Q2_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q2_horizontalSlider.setObjectName("SE_Q2_horizontalSlider")
                self.SE_Q2_horizontal_question_lyt.addWidget(self.SE_Q2_horizontalSlider)
                self.SE_2_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_2_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_2_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_2_spinBox.setFont(font)
                self.SE_2_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_2_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_2_spinBox.setMaximum(20)
                self.SE_2_spinBox.setObjectName("SE_2_spinBox")
                self.SE_Q2_horizontal_question_lyt.addWidget(self.SE_2_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q2_horizontal_question_lyt)
                self.SE_Q3_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q3_horizontal_question_lyt.setObjectName("SE_Q3_horizontal_question_lyt")
                self.SE_Q3_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q3_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q3_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q3_no_Label.setFont(font)
                self.SE_Q3_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q3_no_Label.setObjectName("SE_Q3_no_Label")
                self.SE_Q3_horizontal_question_lyt.addWidget(self.SE_Q3_no_Label)
                spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q3_horizontal_question_lyt.addItem(spacerItem6)
                self.SE_Q3_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q3_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q3_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q3_question.setFont(font)
                self.SE_Q3_question.setObjectName("SE_Q3_question")
                self.SE_Q3_horizontal_question_lyt.addWidget(self.SE_Q3_question)
                self.SE_Q3_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q3_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q3_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q3_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q3_horizontalSlider.setMaximum(20)
                self.SE_Q3_horizontalSlider.setPageStep(5)
                self.SE_Q3_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q3_horizontalSlider.setObjectName("SE_Q3_horizontalSlider")
                self.SE_Q3_horizontal_question_lyt.addWidget(self.SE_Q3_horizontalSlider)
                self.SE_3_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_3_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_3_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_3_spinBox.setFont(font)
                self.SE_3_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_3_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_3_spinBox.setMaximum(20)
                self.SE_3_spinBox.setObjectName("SE_3_spinBox")
                self.SE_Q3_horizontal_question_lyt.addWidget(self.SE_3_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q3_horizontal_question_lyt)
                self.SE_Q4_horizontal_question_ly = QtWidgets.QHBoxLayout()
                self.SE_Q4_horizontal_question_ly.setObjectName("SE_Q4_horizontal_question_ly")
                self.SE_Q4_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q4_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q4_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q4_no_Label.setFont(font)
                self.SE_Q4_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q4_no_Label.setObjectName("SE_Q4_no_Label")
                self.SE_Q4_horizontal_question_ly.addWidget(self.SE_Q4_no_Label)
                spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q4_horizontal_question_ly.addItem(spacerItem7)
                self.SE_Q4_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q4_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q4_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q4_question.setFont(font)
                self.SE_Q4_question.setObjectName("SE_Q4_question")
                self.SE_Q4_horizontal_question_ly.addWidget(self.SE_Q4_question)
                self.SE_Q4_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q4_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q4_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q4_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q4_horizontalSlider.setMaximum(20)
                self.SE_Q4_horizontalSlider.setPageStep(5)
                self.SE_Q4_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q4_horizontalSlider.setObjectName("SE_Q4_horizontalSlider")
                self.SE_Q4_horizontal_question_ly.addWidget(self.SE_Q4_horizontalSlider)
                self.SE_4_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_4_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_4_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_4_spinBox.setFont(font)
                self.SE_4_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_4_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_4_spinBox.setMaximum(20)
                self.SE_4_spinBox.setObjectName("SE_4_spinBox")
                self.SE_Q4_horizontal_question_ly.addWidget(self.SE_4_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q4_horizontal_question_ly)
                self.SE_Q5_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q5_horizontal_question_lyt.setObjectName("SE_Q5_horizontal_question_lyt")
                self.SE_Q5_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q5_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q5_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q5_no_Label.setFont(font)
                self.SE_Q5_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q5_no_Label.setObjectName("SE_Q5_no_Label")
                self.SE_Q5_horizontal_question_lyt.addWidget(self.SE_Q5_no_Label)
                spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q5_horizontal_question_lyt.addItem(spacerItem8)
                self.SE_Q5_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q5_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q5_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q5_question.setFont(font)
                self.SE_Q5_question.setObjectName("SE_Q5_question")
                self.SE_Q5_horizontal_question_lyt.addWidget(self.SE_Q5_question)
                self.SE_Q5_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q5_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q5_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q5_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q5_horizontalSlider.setMaximum(20)
                self.SE_Q5_horizontalSlider.setPageStep(5)
                self.SE_Q5_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q5_horizontalSlider.setObjectName("SE_Q5_horizontalSlider")
                self.SE_Q5_horizontal_question_lyt.addWidget(self.SE_Q5_horizontalSlider)
                self.SE_5_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_5_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_5_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_5_spinBox.setFont(font)
                self.SE_5_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_5_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_5_spinBox.setMaximum(20)
                self.SE_5_spinBox.setObjectName("SE_5_spinBox")
                self.SE_Q5_horizontal_question_lyt.addWidget(self.SE_5_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q5_horizontal_question_lyt)
                self.SE_Q6_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q6_horizontal_question_lyt.setObjectName("SE_Q6_horizontal_question_lyt")
                self.SE_Q6_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q6_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q6_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q6_no_Label.setFont(font)
                self.SE_Q6_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q6_no_Label.setObjectName("SE_Q6_no_Label")
                self.SE_Q6_horizontal_question_lyt.addWidget(self.SE_Q6_no_Label)
                spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q6_horizontal_question_lyt.addItem(spacerItem9)
                self.SE_Q6_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q6_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q6_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q6_question.setFont(font)
                self.SE_Q6_question.setObjectName("SE_Q6_question")
                self.SE_Q6_horizontal_question_lyt.addWidget(self.SE_Q6_question)
                self.SE_Q6_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q6_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q6_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q6_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q6_horizontalSlider.setMaximum(20)
                self.SE_Q6_horizontalSlider.setPageStep(5)
                self.SE_Q6_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q6_horizontalSlider.setObjectName("SE_Q6_horizontalSlider")
                self.SE_Q6_horizontal_question_lyt.addWidget(self.SE_Q6_horizontalSlider)
                self.SE_6_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_6_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_6_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_6_spinBox.setFont(font)
                self.SE_6_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_6_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_6_spinBox.setMaximum(20)
                self.SE_6_spinBox.setObjectName("SE_6_spinBox")
                self.SE_Q6_horizontal_question_lyt.addWidget(self.SE_6_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q6_horizontal_question_lyt)
                self.SE_Q7_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q7_horizontal_question_lyt.setObjectName("SE_Q7_horizontal_question_lyt")
                self.SE_Q7_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q7_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q7_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q7_no_Label.setFont(font)
                self.SE_Q7_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q7_no_Label.setObjectName("SE_Q7_no_Label")
                self.SE_Q7_horizontal_question_lyt.addWidget(self.SE_Q7_no_Label)
                spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q7_horizontal_question_lyt.addItem(spacerItem10)
                self.SE_Q7_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q7_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q7_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q7_question.setFont(font)
                self.SE_Q7_question.setObjectName("SE_Q7_question")
                self.SE_Q7_horizontal_question_lyt.addWidget(self.SE_Q7_question)
                self.SE_Q7_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q7_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q7_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q7_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q7_horizontalSlider.setMaximum(20)
                self.SE_Q7_horizontalSlider.setPageStep(5)
                self.SE_Q7_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q7_horizontalSlider.setObjectName("SE_Q7_horizontalSlider")
                self.SE_Q7_horizontal_question_lyt.addWidget(self.SE_Q7_horizontalSlider)
                self.SE_7_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_7_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_7_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_7_spinBox.setFont(font)
                self.SE_7_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_7_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_7_spinBox.setMaximum(20)
                self.SE_7_spinBox.setObjectName("SE_7_spinBox")
                self.SE_Q7_horizontal_question_lyt.addWidget(self.SE_7_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q7_horizontal_question_lyt)
                self.SE_Q8_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q8_horizontal_question_lyt.setObjectName("SE_Q8_horizontal_question_lyt")
                self.SE_Q8_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q8_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q8_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q8_no_Label.setFont(font)
                self.SE_Q8_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q8_no_Label.setObjectName("SE_Q8_no_Label")
                self.SE_Q8_horizontal_question_lyt.addWidget(self.SE_Q8_no_Label)
                spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q8_horizontal_question_lyt.addItem(spacerItem11)
                self.SE_Q8_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q8_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q8_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q8_question.setFont(font)
                self.SE_Q8_question.setObjectName("SE_Q8_question")
                self.SE_Q8_horizontal_question_lyt.addWidget(self.SE_Q8_question)
                self.SE_Q8_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q8_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q8_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q8_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q8_horizontalSlider.setMaximum(20)
                self.SE_Q8_horizontalSlider.setPageStep(5)
                self.SE_Q8_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q8_horizontalSlider.setObjectName("SE_Q8_horizontalSlider")
                self.SE_Q8_horizontal_question_lyt.addWidget(self.SE_Q8_horizontalSlider)
                self.SE_8_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_8_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_8_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_8_spinBox.setFont(font)
                self.SE_8_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_8_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_8_spinBox.setMaximum(20)
                self.SE_8_spinBox.setObjectName("SE_8_spinBox")
                self.SE_Q8_horizontal_question_lyt.addWidget(self.SE_8_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q8_horizontal_question_lyt)
                self.SE_Q9_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q9_horizontal_question_lyt.setObjectName("SE_Q9_horizontal_question_lyt")
                self.SE_Q9_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q9_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q9_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q9_no_Label.setFont(font)
                self.SE_Q9_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q9_no_Label.setObjectName("SE_Q9_no_Label")
                self.SE_Q9_horizontal_question_lyt.addWidget(self.SE_Q9_no_Label)
                spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q9_horizontal_question_lyt.addItem(spacerItem12)
                self.SE_Q9_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q9_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q9_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q9_question.setFont(font)
                self.SE_Q9_question.setObjectName("SE_Q9_question")
                self.SE_Q9_horizontal_question_lyt.addWidget(self.SE_Q9_question)
                self.SE_Q9_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q9_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q9_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q9_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q9_horizontalSlider.setMaximum(20)
                self.SE_Q9_horizontalSlider.setPageStep(5)
                self.SE_Q9_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q9_horizontalSlider.setObjectName("SE_Q9_horizontalSlider")
                self.SE_Q9_horizontal_question_lyt.addWidget(self.SE_Q9_horizontalSlider)
                self.SE_9_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_9_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_9_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_9_spinBox.setFont(font)
                self.SE_9_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_9_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_9_spinBox.setMaximum(20)
                self.SE_9_spinBox.setObjectName("SE_9_spinBox")
                self.SE_Q9_horizontal_question_lyt.addWidget(self.SE_9_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q9_horizontal_question_lyt)
                self.SE_Q10_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q10_horizontal_question_lyt.setObjectName("SE_Q10_horizontal_question_lyt")
                self.SE_Q10_no_Label = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q10_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q10_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q10_no_Label.setFont(font)
                self.SE_Q10_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q10_no_Label.setObjectName("SE_Q10_no_Label")
                self.SE_Q10_horizontal_question_lyt.addWidget(self.SE_Q10_no_Label)
                spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q10_horizontal_question_lyt.addItem(spacerItem13)
                self.SE_Q10_question = QtWidgets.QLabel(self.SE_Tab_Page_1)
                self.SE_Q10_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q10_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q10_question.setFont(font)
                self.SE_Q10_question.setObjectName("SE_Q10_question")
                self.SE_Q10_horizontal_question_lyt.addWidget(self.SE_Q10_question)
                self.SE_Q10_horizontalSlider = QtWidgets.QSlider(self.SE_Tab_Page_1)
                self.SE_Q10_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q10_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q10_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q10_horizontalSlider.setMaximum(20)
                self.SE_Q10_horizontalSlider.setPageStep(5)
                self.SE_Q10_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q10_horizontalSlider.setObjectName("SE_Q10_horizontalSlider")
                self.SE_Q10_horizontal_question_lyt.addWidget(self.SE_Q10_horizontalSlider)
                self.SE_10_spinBox = QtWidgets.QSpinBox(self.SE_Tab_Page_1)
                self.SE_10_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_10_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_10_spinBox.setFont(font)
                self.SE_10_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_10_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_10_spinBox.setMaximum(20)
                self.SE_10_spinBox.setObjectName("SE_10_spinBox")
                self.SE_Q10_horizontal_question_lyt.addWidget(self.SE_10_spinBox)
                self.SE_Tab_Page_verticalLayout.addLayout(self.SE_Q10_horizontal_question_lyt)
                self.SelfEsteem_tabWidget.addTab(self.SE_Tab_Page_1, "")
                self.SE_Tab_Page_2 = QtWidgets.QWidget()
                self.SE_Tab_Page_2.setObjectName("SE_Tab_Page_2")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.SE_Tab_Page_2)
                self.verticalLayout_8.setContentsMargins(-1, 11, -1, -1)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.SE_widget = QtWidgets.QWidget(self.SE_Tab_Page_2)
                self.SE_widget.setObjectName("SE_widget")
                self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.SE_widget)
                self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_13.setObjectName("verticalLayout_13")
                self.SE_Q11_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q11_horizontal_question_lyt.setObjectName("SE_Q11_horizontal_question_lyt")
                self.SE_Q11_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q11_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q11_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q11_no_Label.setFont(font)
                self.SE_Q11_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q11_no_Label.setObjectName("SE_Q11_no_Label")
                self.SE_Q11_horizontal_question_lyt.addWidget(self.SE_Q11_no_Label)
                spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q11_horizontal_question_lyt.addItem(spacerItem14)
                self.SE_Q11_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q11_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q11_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q11_question.setFont(font)
                self.SE_Q11_question.setObjectName("SE_Q11_question")
                self.SE_Q11_horizontal_question_lyt.addWidget(self.SE_Q11_question)
                self.SE_Q11_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q11_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q11_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q11_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q11_horizontalSlider.setMaximum(20)
                self.SE_Q11_horizontalSlider.setPageStep(5)
                self.SE_Q11_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q11_horizontalSlider.setObjectName("SE_Q11_horizontalSlider")
                self.SE_Q11_horizontal_question_lyt.addWidget(self.SE_Q11_horizontalSlider)
                self.SE_11_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_11_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_11_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_11_spinBox.setFont(font)
                self.SE_11_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_11_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_11_spinBox.setMaximum(20)
                self.SE_11_spinBox.setObjectName("SE_11_spinBox")
                self.SE_Q11_horizontal_question_lyt.addWidget(self.SE_11_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q11_horizontal_question_lyt)
                self.SE_Q12_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q12_horizontal_question_lyt.setObjectName("SE_Q12_horizontal_question_lyt")
                self.SE_Q12_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q12_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q12_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q12_no_Label.setFont(font)
                self.SE_Q12_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q12_no_Label.setObjectName("SE_Q12_no_Label")
                self.SE_Q12_horizontal_question_lyt.addWidget(self.SE_Q12_no_Label)
                spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q12_horizontal_question_lyt.addItem(spacerItem15)
                self.SE_Q12_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q12_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q12_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q12_question.setFont(font)
                self.SE_Q12_question.setObjectName("SE_Q12_question")
                self.SE_Q12_horizontal_question_lyt.addWidget(self.SE_Q12_question)
                self.SE_Q12_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q12_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q12_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q12_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q12_horizontalSlider.setMaximum(20)
                self.SE_Q12_horizontalSlider.setPageStep(5)
                self.SE_Q12_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q12_horizontalSlider.setObjectName("SE_Q12_horizontalSlider")
                self.SE_Q12_horizontal_question_lyt.addWidget(self.SE_Q12_horizontalSlider)
                self.SE_12_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_12_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_12_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_12_spinBox.setFont(font)
                self.SE_12_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_12_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_12_spinBox.setMaximum(20)
                self.SE_12_spinBox.setObjectName("SE_12_spinBox")
                self.SE_Q12_horizontal_question_lyt.addWidget(self.SE_12_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q12_horizontal_question_lyt)
                self.SE_Q13_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q13_horizontal_question_lyt.setObjectName("SE_Q13_horizontal_question_lyt")
                self.SE_Q13_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q13_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q13_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q13_no_Label.setFont(font)
                self.SE_Q13_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q13_no_Label.setObjectName("SE_Q13_no_Label")
                self.SE_Q13_horizontal_question_lyt.addWidget(self.SE_Q13_no_Label)
                spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q13_horizontal_question_lyt.addItem(spacerItem16)
                self.SE_Q13_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q13_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q13_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q13_question.setFont(font)
                self.SE_Q13_question.setObjectName("SE_Q13_question")
                self.SE_Q13_horizontal_question_lyt.addWidget(self.SE_Q13_question)
                self.SE_Q13_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q13_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q13_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q13_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q13_horizontalSlider.setMaximum(20)
                self.SE_Q13_horizontalSlider.setPageStep(5)
                self.SE_Q13_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q13_horizontalSlider.setObjectName("SE_Q13_horizontalSlider")
                self.SE_Q13_horizontal_question_lyt.addWidget(self.SE_Q13_horizontalSlider)
                self.SE_13_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_13_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_13_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_13_spinBox.setFont(font)
                self.SE_13_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_13_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_13_spinBox.setMaximum(20)
                self.SE_13_spinBox.setObjectName("SE_13_spinBox")
                self.SE_Q13_horizontal_question_lyt.addWidget(self.SE_13_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q13_horizontal_question_lyt)
                self.SE_Q14_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q14_horizontal_question_lyt.setObjectName("SE_Q14_horizontal_question_lyt")
                self.SE_Q14_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q14_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q14_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q14_no_Label.setFont(font)
                self.SE_Q14_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q14_no_Label.setObjectName("SE_Q14_no_Label")
                self.SE_Q14_horizontal_question_lyt.addWidget(self.SE_Q14_no_Label)
                spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q14_horizontal_question_lyt.addItem(spacerItem17)
                self.SE_Q14_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q14_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q14_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q14_question.setFont(font)
                self.SE_Q14_question.setObjectName("SE_Q14_question")
                self.SE_Q14_horizontal_question_lyt.addWidget(self.SE_Q14_question)
                self.SE_Q14_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q14_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q14_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q14_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q14_horizontalSlider.setMaximum(20)
                self.SE_Q14_horizontalSlider.setPageStep(5)
                self.SE_Q14_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q14_horizontalSlider.setObjectName("SE_Q14_horizontalSlider")
                self.SE_Q14_horizontal_question_lyt.addWidget(self.SE_Q14_horizontalSlider)
                self.SE_14_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_14_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_14_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_14_spinBox.setFont(font)
                self.SE_14_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_14_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_14_spinBox.setMaximum(20)
                self.SE_14_spinBox.setObjectName("SE_14_spinBox")
                self.SE_Q14_horizontal_question_lyt.addWidget(self.SE_14_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q14_horizontal_question_lyt)
                self.SE_Q15_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q15_horizontal_question_lyt.setObjectName("SE_Q15_horizontal_question_lyt")
                self.SE_Q15_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q15_question.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q15_question.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q15_question.setFont(font)
                self.SE_Q15_question.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q15_question.setObjectName("SE_Q15_question")
                self.SE_Q15_horizontal_question_lyt.addWidget(self.SE_Q15_question)
                spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q15_horizontal_question_lyt.addItem(spacerItem18)
                self.SE_Q15_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q15_no_Label.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q15_no_Label.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q15_no_Label.setFont(font)
                self.SE_Q15_no_Label.setObjectName("SE_Q15_no_Label")
                self.SE_Q15_horizontal_question_lyt.addWidget(self.SE_Q15_no_Label)
                self.SE_Q15_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q15_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q15_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q15_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q15_horizontalSlider.setMaximum(20)
                self.SE_Q15_horizontalSlider.setPageStep(5)
                self.SE_Q15_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q15_horizontalSlider.setObjectName("SE_Q15_horizontalSlider")
                self.SE_Q15_horizontal_question_lyt.addWidget(self.SE_Q15_horizontalSlider)
                self.SE_15_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_15_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_15_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_15_spinBox.setFont(font)
                self.SE_15_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_15_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_15_spinBox.setMaximum(20)
                self.SE_15_spinBox.setObjectName("SE_15_spinBox")
                self.SE_Q15_horizontal_question_lyt.addWidget(self.SE_15_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q15_horizontal_question_lyt)
                self.SE_Q16_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q16_horizontal_question_lyt.setObjectName("SE_Q16_horizontal_question_lyt")
                self.SE_Q16_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q16_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q16_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q16_no_Label.setFont(font)
                self.SE_Q16_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q16_no_Label.setObjectName("SE_Q16_no_Label")
                self.SE_Q16_horizontal_question_lyt.addWidget(self.SE_Q16_no_Label)
                spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q16_horizontal_question_lyt.addItem(spacerItem19)
                self.SE_Q16_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q16_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q16_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q16_question.setFont(font)
                self.SE_Q16_question.setObjectName("SE_Q16_question")
                self.SE_Q16_horizontal_question_lyt.addWidget(self.SE_Q16_question)
                self.SE_Q16_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q16_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q16_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q16_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q16_horizontalSlider.setMaximum(20)
                self.SE_Q16_horizontalSlider.setPageStep(5)
                self.SE_Q16_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q16_horizontalSlider.setObjectName("SE_Q16_horizontalSlider")
                self.SE_Q16_horizontal_question_lyt.addWidget(self.SE_Q16_horizontalSlider)
                self.SE_16_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_16_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_16_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_16_spinBox.setFont(font)
                self.SE_16_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_16_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_16_spinBox.setMaximum(20)
                self.SE_16_spinBox.setObjectName("SE_16_spinBox")
                self.SE_Q16_horizontal_question_lyt.addWidget(self.SE_16_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q16_horizontal_question_lyt)
                self.SE_Q17_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q17_horizontal_question_lyt.setObjectName("SE_Q17_horizontal_question_lyt")
                self.SE_Q17_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q17_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q17_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q17_no_Label.setFont(font)
                self.SE_Q17_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q17_no_Label.setObjectName("SE_Q17_no_Label")
                self.SE_Q17_horizontal_question_lyt.addWidget(self.SE_Q17_no_Label)
                spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q17_horizontal_question_lyt.addItem(spacerItem20)
                self.SE_Q17_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q17_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q17_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q17_question.setFont(font)
                self.SE_Q17_question.setObjectName("SE_Q17_question")
                self.SE_Q17_horizontal_question_lyt.addWidget(self.SE_Q17_question)
                self.SE_Q17_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q17_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q17_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q17_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q17_horizontalSlider.setMaximum(20)
                self.SE_Q17_horizontalSlider.setPageStep(5)
                self.SE_Q17_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q17_horizontalSlider.setObjectName("SE_Q17_horizontalSlider")
                self.SE_Q17_horizontal_question_lyt.addWidget(self.SE_Q17_horizontalSlider)
                self.SE_17_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_17_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_17_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_17_spinBox.setFont(font)
                self.SE_17_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_17_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_17_spinBox.setMaximum(20)
                self.SE_17_spinBox.setObjectName("SE_17_spinBox")
                self.SE_Q17_horizontal_question_lyt.addWidget(self.SE_17_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q17_horizontal_question_lyt)
                self.SE_Q18_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q18_horizontal_question_lyt.setObjectName("SE_Q18_horizontal_question_lyt")
                self.SE_Q18_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q18_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q18_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q18_no_Label.setFont(font)
                self.SE_Q18_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q18_no_Label.setObjectName("SE_Q18_no_Label")
                self.SE_Q18_horizontal_question_lyt.addWidget(self.SE_Q18_no_Label)
                spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q18_horizontal_question_lyt.addItem(spacerItem21)
                self.SE_Q18_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q18_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q18_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q18_question.setFont(font)
                self.SE_Q18_question.setObjectName("SE_Q18_question")
                self.SE_Q18_horizontal_question_lyt.addWidget(self.SE_Q18_question)
                self.SE_Q18_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q18_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q18_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q18_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q18_horizontalSlider.setMaximum(20)
                self.SE_Q18_horizontalSlider.setPageStep(5)
                self.SE_Q18_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q18_horizontalSlider.setObjectName("SE_Q18_horizontalSlider")
                self.SE_Q18_horizontal_question_lyt.addWidget(self.SE_Q18_horizontalSlider)
                self.SE_18_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_18_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_18_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_18_spinBox.setFont(font)
                self.SE_18_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_18_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_18_spinBox.setMaximum(20)
                self.SE_18_spinBox.setObjectName("SE_18_spinBox")
                self.SE_Q18_horizontal_question_lyt.addWidget(self.SE_18_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q18_horizontal_question_lyt)
                self.SE_Q19_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q19_horizontal_question_lyt.setObjectName("SE_Q19_horizontal_question_lyt")
                self.SE_Q19_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q19_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q19_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q19_no_Label.setFont(font)
                self.SE_Q19_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q19_no_Label.setObjectName("SE_Q19_no_Label")
                self.SE_Q19_horizontal_question_lyt.addWidget(self.SE_Q19_no_Label)
                spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q19_horizontal_question_lyt.addItem(spacerItem22)
                self.SE_Q19_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q19_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q19_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q19_question.setFont(font)
                self.SE_Q19_question.setObjectName("SE_Q19_question")
                self.SE_Q19_horizontal_question_lyt.addWidget(self.SE_Q19_question)
                self.SE_Q19_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q19_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q19_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q19_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q19_horizontalSlider.setMaximum(20)
                self.SE_Q19_horizontalSlider.setPageStep(5)
                self.SE_Q19_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q19_horizontalSlider.setObjectName("SE_Q19_horizontalSlider")
                self.SE_Q19_horizontal_question_lyt.addWidget(self.SE_Q19_horizontalSlider)
                self.SE_19_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_19_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_19_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_19_spinBox.setFont(font)
                self.SE_19_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_19_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_19_spinBox.setMaximum(20)
                self.SE_19_spinBox.setObjectName("SE_19_spinBox")
                self.SE_Q19_horizontal_question_lyt.addWidget(self.SE_19_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q19_horizontal_question_lyt)
                self.SE_Q20_horizontal_question_lyt = QtWidgets.QHBoxLayout()
                self.SE_Q20_horizontal_question_lyt.setObjectName("SE_Q20_horizontal_question_lyt")
                self.SE_Q20_no_Label = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q20_no_Label.setMinimumSize(QtCore.QSize(60, 60))
                self.SE_Q20_no_Label.setMaximumSize(QtCore.QSize(60, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(14)
                self.SE_Q20_no_Label.setFont(font)
                self.SE_Q20_no_Label.setStyleSheet("QLabel {\n"
        "     color: rgb(31, 149, 239);\n"
        "    qproperty-alignment: AlignCenter;\n"
        "   \n"
        "    border: 3px solid rgb(31, 149, 239); /* This adds a 1px solid white border around the QLabel */\n"
        "    border-radius: 10px; /* Optional: if you want rounded corners */\n"
        "}\n"
        "")
                self.SE_Q20_no_Label.setObjectName("SE_Q20_no_Label")
                self.SE_Q20_horizontal_question_lyt.addWidget(self.SE_Q20_no_Label)
                spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.SE_Q20_horizontal_question_lyt.addItem(spacerItem23)
                self.SE_Q20_question = QtWidgets.QLabel(self.SE_widget)
                self.SE_Q20_question.setMinimumSize(QtCore.QSize(800, 50))
                self.SE_Q20_question.setMaximumSize(QtCore.QSize(800, 50))
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(16)
                self.SE_Q20_question.setFont(font)
                self.SE_Q20_question.setObjectName("SE_Q20_question")
                self.SE_Q20_horizontal_question_lyt.addWidget(self.SE_Q20_question)
                self.SE_Q20_horizontalSlider = QtWidgets.QSlider(self.SE_widget)
                self.SE_Q20_horizontalSlider.setMinimumSize(QtCore.QSize(351, 71))
                self.SE_Q20_horizontalSlider.setMaximumSize(QtCore.QSize(351, 71))
                self.SE_Q20_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border: 1px solid #999999;\n"
        "    height: 30px; /* Set the height of the groove */\n"
        "    background: white;\n"
        "    margin: 2px 0;\n"
        "    border-radius: 4px; /* Setting border radius for groove */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Handle color */\n"
        "    border: none; /* No border for handle */\n"
        "    width: 60px; /* Width of the handle */\n"
        "    margin: -2px 0; /* Expand outside the groove */\n"
        "    border-radius: 5px; /* Rounded corners for handle */\n"
        "    position: absolute; /* Necessary for proper handle positioning */\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal:hover {\n"
        "    background: rgb(45, 45, 45); /* Handle color when hovered */\n"
        "}\n"
        "\n"
        "/* Style for when the handle is pressed */\n"
        "QSlider::handle:horizontal:pressed {\n"
        "    background: rgb(31, 149, 239); /* You might want to change this color */\n"
        "}\n"
        "\n"
        "/* Ticks styling */\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: rgb(31, 149, 239); /* Color of the part before the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal {\n"
        "    background: white; /* Color of the part after the handle */\n"
        "    border-radius: 4px;\n"
        "}\n"
        "")
                self.SE_Q20_horizontalSlider.setMaximum(20)
                self.SE_Q20_horizontalSlider.setPageStep(5)
                self.SE_Q20_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.SE_Q20_horizontalSlider.setObjectName("SE_Q20_horizontalSlider")
                self.SE_Q20_horizontal_question_lyt.addWidget(self.SE_Q20_horizontalSlider)
                self.SE_20_spinBox = QtWidgets.QSpinBox(self.SE_widget)
                self.SE_20_spinBox.setMinimumSize(QtCore.QSize(90, 60))
                self.SE_20_spinBox.setMaximumSize(QtCore.QSize(90, 60))
                font = QtGui.QFont()
                font.setFamily("Roboto Bk")
                font.setPointSize(20)
                self.SE_20_spinBox.setFont(font)
                self.SE_20_spinBox.setStyleSheet("QSpinBox {\n"
        "    background-color: white;\n"
        "    color: black;\n"
        "    border: 2px solid black;\n"
        "    border-radius: 5px;\n"
        "\n"
        "    padding-left: 20px; /* Adjust left padding to center text */\n"
        "  \n"
        "    margin: 2px;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    /* Styling for the up-button */\n"
        "    subcontrol-origin: border; /* Position within the border */\n"
        "    subcontrol-position: top right; /* Position at the top right */\n"
        "    width: 15px; /* Width of the up-button */\n"
        "    border-left: 1px solid black; /* Border between the up-button and the spin box */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    /* Styling for the down-button */\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "    border-left: 1px solid black;\n"
        "}\n"
        "\n"
        "QSpinBox::up-arrow {\n"
        "    /* Arrow styling within the up-button */\n"
        "    width: 7px; /* Width of the arrow */\n"
        "    height: 7px; /* Height of the arrow */\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "QSpinBox::down-arrow {\n"
        "    /* Arrow styling within the down-button */\n"
        "    width: 7px;\n"
        "    height: 7px;\n"
        "    image: url(:/icon/icon/menu-4-32.ico);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: top right;\n"
        "    width: 15px;\n"
        "    border-bottom: 1px solid black; /* Add border between the up-button and down-button */\n"
        "}\n"
        "\n"
        "QSpinBox::down-button {\n"
        "    subcontrol-origin: border;\n"
        "    subcontrol-position: bottom right;\n"
        "    width: 15px;\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox::up-button:pressed {\n"
        "    /* Styling for the up-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::down-button:pressed {\n"
        "    /* Styling for the down-button when pressed */\n"
        "    background-color: lightgray;\n"
        "}\n"
        "\n"
        "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
        "    /* Styling for the buttons when hovered */\n"
        "    background-color: #e0e0e0;\n"
        "}")
                self.SE_20_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
                self.SE_20_spinBox.setMaximum(20)
                self.SE_20_spinBox.setObjectName("SE_20_spinBox")
                self.SE_Q20_horizontal_question_lyt.addWidget(self.SE_20_spinBox)
                self.verticalLayout_13.addLayout(self.SE_Q20_horizontal_question_lyt)
                self.verticalLayout_8.addWidget(self.SE_widget)
                self.SelfEsteem_tabWidget.addTab(self.SE_Tab_Page_2, "")
                self._gridLayout.addWidget(self.SelfEsteem_tabWidget, 1, 0, 1, 1)
                self.stackedWidget.addWidget(self.SelfEsteem_Page)