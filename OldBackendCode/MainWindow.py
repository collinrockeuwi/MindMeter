from PyQt5.QtWidgets import QMainWindow, QTabWidget
from GeneralTab import GeneralTab
from StressTestTab import StressTestTab
from DepressionTestTab import DepressionTestTab
from SelfEsteemTestTab import SelfEsteemTestTab
from PreviewTab import PreviewTab
from DatabaseTab import DatabaseTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Profile Management")
        self.resize(1080, 720)

        self.profile_data = {
            'name': '',
            'age': 0,
            'sex': '',
            'school': '',
            'image_path': '',
            'stress_test_score': 0,
            'depression_test_score': 0,
            'self_esteem_test_score': 0,
            'comments': ''
        }

        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)

        self.GeneralTab = GeneralTab(mainWindow=self)
        self.stressTestTab = StressTestTab(mainWindow=self)
        self.depressionTestTab = DepressionTestTab(mainWindow=self)
        self.selfEsteemTestTab = SelfEsteemTestTab(mainWindow=self)
        self.previewTab = PreviewTab(mainWindow=self)
        self.databaseTab = DatabaseTab(mainWindow=self)

        self.tabWidget.addTab(self.GeneralTab, "General")
        self.tabWidget.addTab(self.stressTestTab, "Stress Test")
        self.tabWidget.addTab(self.depressionTestTab, "Depression Test")
        self.tabWidget.addTab(self.selfEsteemTestTab, "Self Esteem Test")
        self.tabWidget.addTab(self.previewTab, "Preview")
        self.tabWidget.addTab(self.databaseTab, "Database")

        self.previewTab.dataSaved.connect(self.databaseTab.refreshTable)
        self.stressTestTab.scoresUpdated.connect(self.previewTab.updateReviewLabel)
        self.depressionTestTab.scoresUpdated.connect(self.previewTab.updateReviewLabel)
        self.selfEsteemTestTab.scoresUpdated.connect(self.previewTab.updateReviewLabel)
