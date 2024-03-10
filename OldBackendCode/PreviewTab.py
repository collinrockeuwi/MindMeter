from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
import sqlite3

class PreviewTab(QWidget):
    dataSaved = pyqtSignal()

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = QVBoxLayout(self)

        self.reviewLabel = QLabel()
        self.layout.addWidget(self.reviewLabel)
        self.updateReviewLabel()

        self.save_button = QPushButton("Save to Database", self)
        self.save_button.clicked.connect(self.saveDataToDatabase)
        self.layout.addWidget(self.save_button)

    def updateReviewLabel(self):
        profile_data = self.mainWindow.profile_data
        review_text = "Review your input before saving\n"
        review_text += f"Name: {profile_data['name']}\n"
        review_text += f"Age: {profile_data['age']}\n"
        review_text += f"Sex: {profile_data['sex']}\n"
        review_text += f"School: {profile_data['school']}\n"
        review_text += f"Stress Test Score: {profile_data['stress_test_score']}\n"
        review_text += f"Depression Test Score: {profile_data['depression_test_score']}\n"
        review_text += f"Self-Esteem Test Score: {profile_data['self_esteem_test_score']}\n"
        review_text += f"Comments: {profile_data['comments']}"
        self.reviewLabel.setText(review_text)

    def saveDataToDatabase(self):
        profile_data = self.mainWindow.profile_data
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()
        c.execute('''INSERT INTO profiles (name, age, sex, school, stress_test_score, depression_test_score, self_esteem_test_score, comments)
                     VALUES (:name, :age, :sex, :school, :stress_test_score, :depression_test_score, :self_esteem_test_score, :comments)''', profile_data)
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Success", "Profile saved successfully.")
        self.dataSaved.emit()
