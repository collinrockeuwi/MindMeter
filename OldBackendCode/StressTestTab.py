from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtCore import pyqtSignal

class StressTestTab(QWidget):
    scoresUpdated = pyqtSignal()

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = QVBoxLayout(self)

        self.questions = [
            'Been upset because of something that happened unexpectedly?',
            'Felt that you were unable to control the important things in your life?',
            'Felt nervous and "stressed"?',
            'Felt confident about your ability to handle your personal problems?',
            'Felt that things were going your way?',
            'Found that you could not cope with all the things that you had to do?',
            'Been able to control irritations in your life?',
            'Felt that you were on top of things?',
            'Been angered because of things that were outside of your control?',
            'Felt difficulties were piling up so high that you could not overcome them?'
        ]

        for question in self.questions:
            self.layout.addWidget(QLabel(question))
            for i in range(1, 5):
                checkbox = QCheckBox(str(i), self)
                checkbox.question = question
                checkbox.score = i
                checkbox.stateChanged.connect(self.updateScores)
                self.layout.addWidget(checkbox)

        self.scores = {question: 0 for question in self.questions}

    def updateScores(self, state):
        checkbox = self.sender()
        if state == 2:
            self.scores[checkbox.question] = checkbox.score
        else:
            self.scores[checkbox.question] = 0

        total_score = sum(self.scores.values())
        self.mainWindow.profile_data['stress_test_score'] = total_score
        self.scoresUpdated.emit()
