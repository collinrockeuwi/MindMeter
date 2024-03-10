from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt, pyqtSignal

class SelfEsteemTestTab(QWidget):
    scoresUpdated = pyqtSignal()

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = QVBoxLayout(self)

        self.questions = [
            'I feel that I am a person of worth, at least on an equal plane with others.',
            'I feel that I have a number of good qualities.',
            'All in all, I am inclined to feel that I am a failure.',
            'I am able to do things as well as most other people.',
            'I feel I do not have much to be proud of.',
            'I take a positive attitude toward myself.'
        ]

        for question in self.questions:
            self.layout.addWidget(QLabel(question))
            slider = QSlider(Qt.Horizontal, self)
            slider.setMinimum(1)
            slider.setMaximum(5)
            slider.valueChanged.connect(self.updateScores)
            slider.question = question
            self.layout.addWidget(slider)

        self.scores = {question: 1 for question in self.questions}

    def updateScores(self, value):
        slider = self.sender()
        self.scores[slider.question] = value
        total_score = sum(self.scores.values())
        self.mainWindow.profile_data['self_esteem_test_score'] = total_score
        self.scoresUpdated.emit()
