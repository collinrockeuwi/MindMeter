from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
                             QToolBar, QAction, QHeaderView, QMenu, QInputDialog, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from fuzzywuzzy import process
import sqlite3
from ProfileDetailDialog import ProfileDetailDialog
from CustomHeaderView import CustomHeaderView


class DatabaseTab(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow  # Store the reference to the main window
        self.layout = QVBoxLayout(self)
        self.dialog_open = False  # Track the dialog state

        # Initialize filters
        self.currentSexFilter = {'Male': True, 'Female': True}
        self.rangeFilters = {}

        # Create and configure the toolbar
        self.toolbar = QToolBar("Database Toolbar")
        self.layout.addWidget(self.toolbar)

        # Add a reset action with an icon
        resetAction = QAction(QIcon('C:/Users/colli/source/repos/databaseui2/icons/reset_icon.png'), "Reset", self)
        resetAction.triggered.connect(self.resetTable)
        self.toolbar.addAction(resetAction)

        # Add a settings action with an icon
        settingsAction = QAction(QIcon('C:/Users/colli/source/repos/databaseui2/icons/settings_icon.png'), "Settings", self)
        settingsAction.triggered.connect(self.openSettingsDialog)
        self.toolbar.addAction(settingsAction)

        # Create the table widget and set the custom header view
        self.tableWidget = QTableWidget()
        header = CustomHeaderView(Qt.Horizontal, self, self.tableWidget)
        self.tableWidget.setHorizontalHeader(header)
        self.layout.addWidget(self.tableWidget)

        # Populate the table
        self.createTable()

        # Show the widget
        self.show()


        
    def createTable(self):
        columnHeaders = ['Name', 'Age', 'Sex', 'School', 'Stress Test', 'Depression Test', 'Self-Esteem Test', 'Image']
        self.tableWidget.setColumnCount(len(columnHeaders))
        self.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        # Clear existing data
        self.tableWidget.setRowCount(0)

        # Fetch and populate data
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()
        c.execute("SELECT name, age, sex, school, stress_test_score, depression_test_score, self_esteem_test_score, image_path FROM profiles")
        records = c.fetchall()
        conn.close()

        self.tableWidget.setRowCount(len(records))
        for row_idx, row_data in enumerate(records):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                if col_idx in [4, 5, 6]:  # Numeric columns
                    item.setData(Qt.DisplayRole, col_data)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(row_idx, col_idx, item)

        self.tableWidget.setSortingEnabled(True)
        
        self.tableWidget.cellClicked.connect(self.onCellClicked)




    def onCellClicked(self, row, column):
        # Check if the name column was clicked and the item is not None
        if column == 0 and self.tableWidget.item(row, column) is not None:  # Assuming the name is in the first column
            name = self.tableWidget.item(row, column).text()
            self.openProfileDetails(name)

    def openProfileDetails(self, profile_name):
        # Check if the dialog already exists, if not, create it
        if not self.profileDialog:
            self.profileDialog = ProfileDetailDialog(profile_name, self)
            self.profileDialog.dataUpdated.connect(self.refreshTable)
            self.profileDialog.closed.connect(self.resetTable)
        else:
            # Update the profile name and fetch the new data
            self.profileDialog.profile_name = profile_name
            self.profileDialog.setWindowTitle(profile_name + " - Profile Details")
            self.profileDialog.fetch_and_display()

        self.profileDialog.exec_()


        
    def refreshTableWithFilter(self, sexFilter=None):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.clearContents()

        # Mapping between display names and database column names
        column_mapping = {
            "Stress Test": "stress_test_score",
            "Depression Test": "depression_test_score",
            "Self-Esteem Test": "self_esteem_test_score"
        }

        # Initialize conditions and params at the start
        query_base = "SELECT name, age, sex, school, stress_test_score, depression_test_score, self_esteem_test_score, image_path FROM profiles"
        conditions = []
        params = []
        # Apply sex filter if specified
        if sexFilter:
            if sexFilter.get('Male'):
                conditions.append("sex = ?")
                params.append('Male')
            if sexFilter.get('Female'):
                conditions.append("sex = ?")
                params.append('Female')

        # Apply range filters
        for index, (low, high) in self.rangeFilters.items():
            column_display_name = self.tableWidget.horizontalHeaderItem(index).text()
            columnName = column_mapping.get(column_display_name, column_display_name).lower()
            if low > 0:
                conditions.append(f"{columnName} >= ?")
                params.append(low)
            if high > 0:
                conditions.append(f"{columnName} <= ?")
                params.append(high)

        if conditions:
            query = f"{query_base} WHERE {' AND '.join(conditions)}"
        else:
            query = query_base

        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()
        c.execute(query, params)
        records = c.fetchall()
        conn.close()

        self.populateTable(records)
        self.tableWidget.setSortingEnabled(True)

                    
    def openProfileDetails(self, profile_name):
        if not self.dialog_open:
            self.profileDialog = ProfileDetailDialog(profile_name, self)
            self.profileDialog.dataUpdated.connect(self.refreshTable)
            self.profileDialog.closed.connect(self.resetTable)
            self.profileDialog.closed.connect(lambda: setattr(self, 'dialog_open', False))
            self.dialog_open = True
        else:
            # Update the profile name and fetch the new data
            self.profileDialog.profile_name = profile_name
            self.profileDialog.setWindowTitle(profile_name + " - Profile Details")
            self.profileDialog.fetch_and_display()

        self.profileDialog.exec_()
        
    def updateSexFilter(self, sexFilter):
        self.currentSexFilter = sexFilter
        # Assuming refreshTableWithFilter is a method that refreshes the table based on the current filters
        self.refreshTableWithFilter(self.currentSexFilter)
        
    def fuzzySearchByName(self):
        text, ok = QInputDialog.getText(self, 'Fuzzy Search by Name', 'Enter name:')
        if ok and text:
            self.refreshTableWithFuzzyNameFilter(text)
            
    def fuzzySearchBySchool(self):
        text, ok = QInputDialog.getText(self, 'Fuzzy Search by School', 'Enter school:')
        if ok and text:
            self.refreshTableWithFuzzySchoolFilter(text)

    def refreshTableWithFuzzyNameFilter(self, searchText):
        # Open a new database connection
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()

        # Fetch all names from the database
        c.execute("SELECT name FROM profiles")
        all_names = [row[0] for row in c.fetchall()]

        # Close the database connection after fetching names
        conn.close()

        # Use fuzzywuzzy to find the best matches for the given searchText
        best_matches = process.extract(searchText, all_names, limit=None)  # Consider all possible matches

        # Extract names and scores, filter out low scores if necessary
        filtered_matches = [(name, score) for name, score in best_matches if score > 50]  # Adjust score threshold as needed

        # Sort matches by score in descending order
        filtered_matches.sort(key=lambda x: x[1], reverse=True)

        # Extract just the names for fetching detailed records
        matched_names = [match[0] for match in filtered_matches]

        # Open a new connection to fetch detailed records for the matched names
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()

        placeholders = ', '.join('?' for _ in matched_names)
        query = f"SELECT * FROM profiles WHERE name IN ({placeholders})"
        c.execute(query, matched_names)
        records = c.fetchall()

        # Close the database connection after fetching records
        conn.close()

        # Pass names with their scores for sorting to populateTable
        self.populateTable(records, [name for name, _ in filtered_matches])

        # Re-enable sorting
        self.tableWidget.setSortingEnabled(True)
        
    def refreshTableWithFuzzySchoolFilter(self, searchText):
        # Open a new database connection
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()

        # Fetch all schools from the database
        c.execute("SELECT DISTINCT school FROM profiles")
        all_schools = [row[0] for row in c.fetchall()]

        # Close the database connection after fetching schools
        conn.close()

        # Prioritize exact matches first, which can improve accuracy for direct matches
        exact_matches = [school for school in all_schools if school.lower() == searchText.lower()]

        if exact_matches:
            matched_schools = exact_matches
        else:
            # Use fuzzywuzzy to find the best matches for the given searchText
            best_matches = process.extract(searchText, all_schools, limit=None)  # Consider all possible matches

            # Extract schools and scores, filter out low scores if necessary
            filtered_matches = [(school, score) for school, score in best_matches if score > 50]  # Adjust score threshold as needed

            # Sort matches by score in descending order
            filtered_matches.sort(key=lambda x: x[1], reverse=True)

            # Extract just the schools for fetching detailed records
            matched_schools = [match[0] for match in filtered_matches]

        # Fetch detailed records for the matched schools from the database
        self.fetchAndPopulateSchoolRecords(matched_schools)

    def fetchAndPopulateSchoolRecords(self, matched_schools):
        conn = sqlite3.connect('student_profiles.db')
        c = conn.cursor()
        placeholders = ', '.join(['?'] * len(matched_schools))
        query = f"SELECT * FROM profiles WHERE school IN ({placeholders})"
        c.execute(query, matched_schools)
        records = c.fetchall()
        conn.close()

        # Pass schools with their scores for sorting to populateTable
        # Assuming school names were used for sorting, adjust if needed
        self.populateTable(records, matched_schools)
        
    def filterByRange(self, columnIndex):
        # Prompt user for low and high range values
        low, ok1 = QInputDialog.getInt(self, "Range Filter", "Enter low value (leave 0 for no limit):", 0)
        high, ok2 = QInputDialog.getInt(self, "Range Filter", "Enter high value (leave 0 for no limit):", 0)

        if ok1 or ok2:
            # Update rangeFilters dictionary
            self.rangeFilters[columnIndex] = (low, high)
            self.refreshTableWithFilter()
            
    def populateTable(self, records, sort_keys=None, sort_field_index=None):
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.clearContents()

        # Adjust to use sort_keys and sort_field_index if provided
        if sort_keys is not None and sort_field_index is not None:
            record_to_sort_key = {record[sort_field_index]: record for record in records}
            ordered_records = [record_to_sort_key[key] for key in sort_keys if key in record_to_sort_key]
            records = ordered_records

        self.tableWidget.setRowCount(len(records))

        for row_idx, row_data in enumerate(records):
            for col_idx, col_data in enumerate(row_data):
                if isinstance(col_data, int):
                    # For numeric columns, ensure correct numeric sorting
                    item = QTableWidgetItem()
                    item.setData(Qt.DisplayRole, col_data)
                else:
                    # For text and other data types
                    item = QTableWidgetItem(str(col_data))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make cells non-editable but selectable
                self.tableWidget.setItem(row_idx, col_idx, item)

        self.tableWidget.setSortingEnabled(True)

        
    '''def addResetButton(self):
        self.resetButton = QPushButton("Reset Table", self)
        self.resetButton.clicked.connect(self.resetTable)
        self.resetButton.move(10, 10)  # Adjust position as needed'''
        
    def resetTable(self):
        # Clear all filters and search criteria
        self.currentSexFilter = {'Male': True, 'Female': True}
        self.rangeFilters.clear()  # Clear the rangeFilters of DatabaseTab, not MainWindow
        self.createTable()  # Call the method that refreshes the table with updated data

        # Clear search field if it exists
        if hasattr(self, 'searchLineEdit'):  # Check if searchLineEdit is an attribute of DatabaseTab
            self.searchLineEdit.clear()

        # Repopulate the table to its default state
        self.refreshTableWithFilter()

    def resetTableFromProfile(self):
        # Clear all filters and search criteria
        self.currentSexFilter = {'Male': True, 'Female': True}
        self.rangeFilters.clear()  # Clear the rangeFilters of DatabaseTab, not MainWindow

        # Clear search field if it exists
        if hasattr(self, 'searchLineEdit'):  # Check if searchLineEdit is an attribute of DatabaseTab
            self.searchLineEdit.clear()

        # Repopulate the table to its default state
        self.createTable()

    def openSettingsDialog(self):
            # Implement this method to open a dialog for settings
            pass

    def refreshTable(self):
        print("Refreshing table...")
        self.createTable()
        print("Table refreshed.")
