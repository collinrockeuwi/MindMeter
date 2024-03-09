from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal
import sqlite3

class ProfileDetailDialog(QDialog):
    dataUpdated = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self, profile_name, parent=None):
        super().__init__(parent)
        self.profile_name = profile_name
        self.parent = parent  # Store a reference to the parent
        self.setWindowTitle(profile_name + " - Profile Details")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        self.image_path = None

        # Initialize UI components
        self.initUI()

        # Connect the closed signal to the resetTableFromProfile slot
        #self.closed.connect(self.parent.resetTableFromProfile)

    def initUI(self):
        self.stress_test_label = QLabel("Stress Test Score:")
        self.stress_test_input = QLineEdit(self)
        self.layout.addWidget(self.stress_test_label)
        self.layout.addWidget(self.stress_test_input)

        self.depression_test_label = QLabel("Depression Test Score:")
        self.depression_test_input = QLineEdit(self)
        self.layout.addWidget(self.depression_test_label)
        self.layout.addWidget(self.depression_test_input)

        self.self_esteem_test_label = QLabel("Self-Esteem Test Score:")
        self.self_esteem_test_input = QLineEdit(self)
        self.layout.addWidget(self.self_esteem_test_label)
        self.layout.addWidget(self.self_esteem_test_input)

        self.edit_image_btn = QPushButton("Edit Image", self)
        self.edit_image_btn.clicked.connect(self.edit_image)
        self.layout.addWidget(self.edit_image_btn)

        self.add_comments_label = QLabel("Comments:")
        self.add_comments_input = QLineEdit(self)
        self.layout.addWidget(self.add_comments_label)
        self.layout.addWidget(self.add_comments_input)

        self.delete_profile_btn = QPushButton("Delete Profile", self)
        self.delete_profile_btn.clicked.connect(self.delete_profile)
        self.layout.addWidget(self.delete_profile_btn)

        self.save_changes_btn = QPushButton("Save Changes", self)
        self.save_changes_btn.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_changes_btn)

        self.setLayout(self.layout)

        self.fetch_and_display()

    def save_changes(self):
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()
        c.execute('''SELECT stress_test_score, depression_test_score, self_esteem_test_score, comments
                     FROM profiles WHERE name = ?''', (self.profile_name,))
        row = c.fetchone()

        existing_stress_test, existing_depression_test, existing_self_esteem_test, existing_comments = row if row else (None, None, None, None)

        stress_test_score = self.stress_test_input.text() or existing_stress_test
        depression_test_score = self.depression_test_input.text() or existing_depression_test
        self_esteem_test_score = self.self_esteem_test_input.text() or existing_self_esteem_test
        comments = self.add_comments_input.text() or existing_comments

        c.execute('''UPDATE profiles SET
                     stress_test_score = ?,
                     depression_test_score = ?,
                     self_esteem_test_score = ?,
                     comments = ?
                     WHERE name = ?''',
                  (stress_test_score, depression_test_score, self_esteem_test_score, comments, self.profile_name))
        conn.commit()
        conn.close()
        self.dataUpdated.emit()
        self.accept()

        QMessageBox.information(self, 'Success', 'Changes saved successfully.')

    def edit_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            self.image_path = file_name

    def delete_profile(self):
        reply = QMessageBox.question(self, 'Confirm Delete',
                                     f"Are you sure you want to delete the profile for {self.profile_name}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            conn = sqlite3.connect('student_profiles.db')
            c = conn.cursor()
            c.execute('DELETE FROM profiles WHERE name = ?', (self.profile_name,))
            conn.commit()
            conn.close()
            self.accept()

    def fetch_and_display(self):
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()
        c.execute('''SELECT stress_test_score, depression_test_score, self_esteem_test_score, image_path, comments
                     FROM profiles WHERE name = ?''', (self.profile_name,))
        result = c.fetchone()
        conn.close()

        if result:
            stress_test_score, depression_test_score, self_esteem_test_score, image_path, comments = result
            self.stress_test_input.setText(str(stress_test_score))
            self.depression_test_input.setText(str(depression_test_score))
            self.self_esteem_test_input.setText(str(self_esteem_test_score))
            self.image_path = image_path
            self.add_comments_input.setText(comments)

    def closeEvent(self, event):
        ...
        # Remove the try-except block for disconnecting the signal
        super().closeEvent(event)

