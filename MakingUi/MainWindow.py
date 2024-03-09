from PyQt5 import QtCore, QtGui, QtWidgets        
#has side bar




#Top bar options
class MainWindow:
    def __init__(self, parent):
        self.setupMainWindowpage(parent)


    def setupMainWindowpage(self, PsycheEval_MainWindow):
        PsycheEval_MainWindow.setObjectName("PsycheEval_MainWindow")
        PsycheEval_MainWindow.resize(1920, 1080)
        PsycheEval_MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.MainWindow_grid_lyt = QtWidgets.QWidget(PsycheEval_MainWindow)
        self.MainWindow_grid_lyt.setObjectName("MainWindow_grid_lyt")
        self.MainWindow_gridLayout = QtWidgets.QGridLayout(self.MainWindow_grid_lyt)
        self.MainWindow_gridLayout.setContentsMargins(0, -1, -1, -1)
        self.MainWindow_gridLayout.setHorizontalSpacing(0)
        self.MainWindow_gridLayout.setObjectName("MainWindow_gridLayout")
        self.expanded_icon_widget = QtWidgets.QWidget(self.MainWindow_grid_lyt)
        self.expanded_icon_widget.setMinimumSize(QtCore.QSize(281, 0))
        self.expanded_icon_widget.setMaximumSize(QtCore.QSize(281, 16777215))
        self.expanded_icon_widget.setStyleSheet("QWidget{\n"
"\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton {\n"
"    color: white;\n"
"    text-align: left;\n"
"    height:70px;\n"
"    border: 1px;\n"
"    padding-left: 10px;\n"
"    border-top-left-radius: 10px; /* Round top left corner */\n"
"    border-bottom-left-radius: 10px; /* Round bottom left corner */\n"
"    background-color: rgb(31, 149, 239); /* Normal background color */\n"
"    font-size: 30px; /* Set the font size here */\n"
"    /* Other styles */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(45, 45, 45); /* Darker background color on hover */\n"
"    color: rgb(220, 220, 220); /* Slightly lighter text color on hover */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
" \n"
"     background-color: rgb(45, 45, 45); /* Darker background color on checked */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"")
        PsycheEval_MainWindow.showMaximized()
        self.expanded_icon_widget.setObjectName("expanded_icon_widget")
        self.expanded_icon_widget_gridLayout = QtWidgets.QGridLayout(self.expanded_icon_widget)
        self.expanded_icon_widget_gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.expanded_icon_widget_gridLayout.setObjectName("expanded_icon_widget_gridLayout")
        self.expanded_icon_verticalLayout = QtWidgets.QVBoxLayout()
        self.expanded_icon_verticalLayout.setObjectName("expanded_icon_verticalLayout")
        self.Logo = QtWidgets.QSplitter(self.expanded_icon_widget)
        self.Logo.setOrientation(QtCore.Qt.Horizontal)
        self.Logo.setObjectName("Logo")
        self.logo_label = QtWidgets.QLabel(self.Logo)
        self.logo_label.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.logo_mainlabel = QtWidgets.QLabel(self.Logo)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.logo_mainlabel.setFont(font)
        self.logo_mainlabel.setObjectName("logo_mainlabel")
        self.expanded_icon_verticalLayout.addWidget(self.Logo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.expanded_icon_verticalLayout.addItem(spacerItem)
        self.expanded_icon_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.expanded_icon_verticalLayout_2.setSpacing(40)
        self.expanded_icon_verticalLayout_2.setObjectName("expanded_icon_verticalLayout_2")
        self.expanded_icon_General_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_General_pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_General_pushButton.setIcon(icon)
        self.expanded_icon_General_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_General_pushButton.setCheckable(True)
        self.expanded_icon_General_pushButton.setAutoExclusive(True)
        self.expanded_icon_General_pushButton.setObjectName("expanded_icon_General_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_General_pushButton)
        self.expanded_icon_Stress_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_Stress_pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_Stress_pushButton.setIcon(icon1)
        self.expanded_icon_Stress_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_Stress_pushButton.setCheckable(True)
        self.expanded_icon_Stress_pushButton.setAutoExclusive(True)
        self.expanded_icon_Stress_pushButton.setObjectName("expanded_icon_Stress_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_Stress_pushButton)
        self.expanded_icon_Depression_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_Depression_pushButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/product-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_Depression_pushButton.setIcon(icon2)
        self.expanded_icon_Depression_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_Depression_pushButton.setCheckable(True)
        self.expanded_icon_Depression_pushButton.setAutoExclusive(True)
        self.expanded_icon_Depression_pushButton.setObjectName("expanded_icon_Depression_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_Depression_pushButton)
        self.expanded_icon_SelfEsteem_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_SelfEsteem_pushButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/user-48-white.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_SelfEsteem_pushButton.setIcon(icon3)
        self.expanded_icon_SelfEsteem_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_SelfEsteem_pushButton.setCheckable(True)
        self.expanded_icon_SelfEsteem_pushButton.setAutoExclusive(True)
        self.expanded_icon_SelfEsteem_pushButton.setObjectName("expanded_icon_SelfEsteem_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_SelfEsteem_pushButton)
        self.expanded_icon_Preview_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_Preview_pushButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_Preview_pushButton.setIcon(icon4)
        self.expanded_icon_Preview_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_Preview_pushButton.setCheckable(True)
        self.expanded_icon_Preview_pushButton.setAutoExclusive(True)
        self.expanded_icon_Preview_pushButton.setObjectName("expanded_icon_Preview_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_Preview_pushButton)
        self.expanded_icon_Database_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_Database_pushButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/search-13.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_Database_pushButton.setIcon(icon5)
        self.expanded_icon_Database_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_Database_pushButton.setCheckable(True)
        self.expanded_icon_Database_pushButton.setAutoExclusive(True)
        self.expanded_icon_Database_pushButton.setObjectName("expanded_icon_Database_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_Database_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.expanded_icon_verticalLayout_2.addItem(spacerItem1)
        self.expanded_icon_Exit_pushButton = QtWidgets.QPushButton(self.expanded_icon_widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.expanded_icon_Exit_pushButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64-white.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expanded_icon_Exit_pushButton.setIcon(icon6)
        self.expanded_icon_Exit_pushButton.setIconSize(QtCore.QSize(50, 50))
        self.expanded_icon_Exit_pushButton.setObjectName("expanded_icon_Exit_pushButton")
        self.expanded_icon_verticalLayout_2.addWidget(self.expanded_icon_Exit_pushButton)
        self.expanded_icon_verticalLayout.addLayout(self.expanded_icon_verticalLayout_2)
        self.expanded_icon_widget_gridLayout.addLayout(self.expanded_icon_verticalLayout, 0, 0, 1, 1)
        self.MainWindow_gridLayout.addWidget(self.expanded_icon_widget, 0, 1, 1, 1)
        self.small_icon_widget = QtWidgets.QWidget(self.MainWindow_grid_lyt)
        self.small_icon_widget.setMinimumSize(QtCore.QSize(131, 0))
        self.small_icon_widget.setMaximumSize(QtCore.QSize(131, 16777215))
        self.small_icon_widget.setStyleSheet("QWidget{\n"
"\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    text-align: centre;\n"
"    height: 100px;\n"
"    border: none;\n"
"    \n"
"    border-radius: 10px; \n"
"    \n"
"    background-color: rgb(31, 149, 239); /* Normal background color */\n"
"    font-size: 14px; /* Set the font size here */\n"
"    /* Other styles */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(45, 45, 45); /* Darker background color on hover */\n"
"    color: rgb(220, 220, 220); /* Slightly lighter text color on hover */\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
" \n"
"    \n"
"     background-color: rgb(45, 45, 45); /* Darker background color on checked */\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    qproperty-alignment: AlignCenter; /* This will center the text */\n"
"}\n"
"\n"
"\n"
"")
        self.small_icon_widget.setObjectName("small_icon_widget")
        self.small_icon_widget_verticalLayout = QtWidgets.QVBoxLayout(self.small_icon_widget)
        self.small_icon_widget_verticalLayout.setObjectName("small_icon_widget_verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.small_icon_widget_verticalLayout.addItem(spacerItem2)
        self.General_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.General_pushButton.setText("")
        self.General_pushButton.setIcon(icon)
        self.General_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.General_pushButton.setCheckable(True)
        self.General_pushButton.setAutoExclusive(True)
        self.General_pushButton.setObjectName("General_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.General_pushButton)
        self.Stress_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.Stress_pushButton.setText("")
        self.Stress_pushButton.setIcon(icon1)
        self.Stress_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.Stress_pushButton.setCheckable(True)
        self.Stress_pushButton.setAutoExclusive(True)
        self.Stress_pushButton.setObjectName("Stress_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.Stress_pushButton)
        self.Depression_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.Depression_pushButton.setText("")
        self.Depression_pushButton.setIcon(icon2)
        self.Depression_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.Depression_pushButton.setCheckable(True)
        self.Depression_pushButton.setAutoExclusive(True)
        self.Depression_pushButton.setObjectName("Depression_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.Depression_pushButton)
        self.SelfEsteem_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.SelfEsteem_pushButton.setText("")
        self.SelfEsteem_pushButton.setIcon(icon3)
        self.SelfEsteem_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.SelfEsteem_pushButton.setCheckable(True)
        self.SelfEsteem_pushButton.setAutoExclusive(True)
        self.SelfEsteem_pushButton.setObjectName("SelfEsteem_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.SelfEsteem_pushButton)
        self.Preview_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.Preview_pushButton.setText("")
        self.Preview_pushButton.setIcon(icon4)
        self.Preview_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.Preview_pushButton.setCheckable(True)
        self.Preview_pushButton.setAutoExclusive(True)
        self.Preview_pushButton.setObjectName("Preview_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.Preview_pushButton)
        self.Database_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.Database_pushButton.setText("")
        self.Database_pushButton.setIcon(icon5)
        self.Database_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.Database_pushButton.setCheckable(True)
        self.Database_pushButton.setAutoExclusive(True)
        self.Database_pushButton.setObjectName("Database_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.Database_pushButton)
        self.Exit_pushButton = QtWidgets.QPushButton(self.small_icon_widget)
        self.Exit_pushButton.setText("")
        self.Exit_pushButton.setIcon(icon6)
        self.Exit_pushButton.setIconSize(QtCore.QSize(100, 100))
        self.Exit_pushButton.setObjectName("Exit_pushButton")
        self.small_icon_widget_verticalLayout.addWidget(self.Exit_pushButton)
        self.MainWindow_gridLayout.addWidget(self.small_icon_widget, 0, 0, 1, 1)