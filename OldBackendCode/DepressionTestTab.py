from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtCore import pyqtSignal

class DepressionTestTab(QWidget):
    scoresUpdated = pyqtSignal()

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.layout = QVBoxLayout(self)

        self.questions = [
            'Feeling down, depressed, or hopeless',
            'Little interest or pleasure in doing things',
            'Trouble falling or staying asleep, or sleeping too much',
            'Feeling tired or having little energy',
            'Poor appetite or overeating',
            'Feeling bad about yourself - or that you are a failure or have let yourself or your family down',
            'Trouble concentrating on things, such as reading the newspaper or watching television',
            'Moving or speaking so slowly that other people could have noticed',
            'Thoughts that you would be better off dead, or of hurting yourself',
            'If you have experienced any of the above symptoms, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?'
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
        self.mainWindow.profile_data['depression_test_score'] = total_score
        self.scoresUpdated.emit()
