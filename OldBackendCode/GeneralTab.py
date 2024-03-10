from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QRadioButton, QHBoxLayout, QPushButton, QFileDialog, QDateEdit
from PyQt5.QtCore import QDate

class GeneralTab(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = QVBoxLayout(self)

        self.layout.addWidget(QLabel('Name'))
        self.name_input = QLineEdit(self)
        self.name_input.textChanged.connect(self.updateProfileData)
        self.layout.addWidget(self.name_input)

        self.layout.addWidget(QLabel('Age'))
        self.age_input = QLineEdit(self)
        self.age_input.textChanged.connect(self.updateProfileData)
        self.layout.addWidget(self.age_input)

        self.layout.addWidget(QLabel('Sex'))
        sex_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male", self)
        self.female_radio = QRadioButton("Female", self)
        self.male_radio.toggled.connect(self.updateProfileData)
        self.female_radio.toggled.connect(self.updateProfileData)
        sex_layout.addWidget(self.male_radio)
        sex_layout.addWidget(self.female_radio)
        self.layout.addLayout(sex_layout)

        self.layout.addWidget(QLabel('School'))
        self.school_input = QLineEdit(self)
        self.school_input.textChanged.connect(self.updateProfileData)
        self.layout.addWidget(self.school_input)

        self.layout.addWidget(QLabel('Image'))
        image_layout = QHBoxLayout()
        self.image_path = QLineEdit(self)
        self.image_path.textChanged.connect(self.updateProfileData)
        self.browse_button = QPushButton('Browse...', self)
        self.browse_button.clicked.connect(self.browse_image)
        image_layout.addWidget(self.image_path)
        image_layout.addWidget(self.browse_button)
        self.layout.addLayout(image_layout)

        self.layout.addWidget(QLabel('Date'))
        self.date_input = QDateEdit(self)
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.dateChanged.connect(self.updateProfileData)
        self.layout.addWidget(self.date_input)

    def browse_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "Image files (*.jpg *.gif *.png)")
        self.image_path.setText(fname)

    def updateProfileData(self):
        self.mainWindow.profile_data['name'] = self.name_input.text()
        self.mainWindow.profile_data['age'] = self.age_input.text()
        self.mainWindow.profile_data['sex'] = 'Male' if self.male_radio.isChecked() else 'Female' if self.female_radio.isChecked() else ''
        self.mainWindow.profile_data['school'] = self.school_input.text()
        self.mainWindow.profile_data['image_path'] = self.image_path.text()
        self.mainWindow.profile_data['date'] = self.date_input.date().toString("yyyy-MM-dd")
