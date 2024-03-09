from PyQt5.QtWidgets import QHeaderView, QMenu, QAction
from PyQt5.QtCore import Qt

class CustomHeaderView(QHeaderView):
    def __init__(self, orientation, databaseTab, parent=None):
        super().__init__(orientation, parent)
        self.databaseTab = databaseTab  # Reference to the DatabaseTab instance
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)
        # Initialize filters as before
        self.sexFilter = {'Male': True, 'Female': True}

    def contextMenu(self, point):
        # Import DatabaseTab inside the method to avoid circular import
       # from DatabaseTab import DatabaseTab

        index = self.logicalIndexAt(point)
        menu = QMenu(self)

        if index == 0:  # Name column
            searchAction = menu.addAction("Search by Name")
            searchAction.triggered.connect(self.databaseTab.fuzzySearchByName)
            # Add sorting actions for the Name column
            self.addSortingActions(menu, index)
        elif index == 3:  # School column
            searchAction = menu.addAction("Search by School")
            searchAction.triggered.connect(self.databaseTab.fuzzySearchBySchool)
            # Add sorting actions for the School column
            self.addSortingActions(menu, index)
        elif index == 2:  # Sex column
            self.addSexFilterActions(menu)
        else:
            # Add sorting actions for other columns except Sex
            self.addSortingActions(menu, index)

        if index in [1, 4, 5, 6]:  # Assuming these indexes match Age, Stress Test, Depression Test, Self-Esteem Test
            rangeFilterAction = menu.addAction("Filter by Range")
            rangeFilterAction.triggered.connect(lambda: self.databaseTab.filterByRange(index))
        menu.exec_(self.mapToGlobal(point))

    def addSortingActions(self, menu, index):
        sortAscAction = menu.addAction("Sort Ascending")
        sortDescAction = menu.addAction("Sort Descending")

        # Connect actions directly without re-executing the menu
        sortAscAction.triggered.connect(lambda: self.sortIndicatorChanged(index, Qt.AscendingOrder))
        sortDescAction.triggered.connect(lambda: self.sortIndicatorChanged(index, Qt.DescendingOrder))

    def addSexFilterActions(self, menu):
        maleAction = menu.addAction("Male")
        maleAction.setCheckable(True)
        maleAction.setChecked(self.sexFilter['Male'])
        maleAction.toggled.connect(lambda: self.toggleSexFilter('Male', maleAction))

        femaleAction = menu.addAction("Female")
        femaleAction.setCheckable(True)
        femaleAction.setChecked(self.sexFilter['Female'])
        femaleAction.toggled.connect(lambda: self.toggleSexFilter('Female', femaleAction))

    def toggleSexFilter(self, sex, action):
        self.sexFilter[sex] = action.isChecked()
        # Call updateSexFilter on the databaseTab reference, which points to the DatabaseTab instance
        self.databaseTab.updateSexFilter(self.sexFilter)

    def sortIndicatorChanged(self, index, order):
        self.databaseTab.tableWidget.sortByColumn(index, order)
