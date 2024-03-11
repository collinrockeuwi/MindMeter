import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.create_tables()
    
    def fetch_all_students(self):
        self.conn.cursor().execute("SELECT * FROM Students")
        return self.conn.cursor().fetchall()

    def fetch_all_tests(self):
        self.conn.cursor().execute("SELECT * FROM Tests")
        return self.conn.cursor().fetchall()

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        try:
            c = self.conn.cursor()
            # Create the Students Table
            c.execute('''CREATE TABLE IF NOT EXISTS Students (
                            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name TEXT NOT NULL,
                            Age INTEGER,
                            School TEXT,
                            Sex TEXT
                        )''')
            # Create the Tests Table
            c.execute('''CREATE TABLE IF NOT EXISTS Tests (
                            TestID INTEGER PRIMARY KEY AUTOINCREMENT,
                            StudentID INTEGER,
                            StressTestScore INTEGER,
                            DepressionTestScore INTEGER,
                            SelfEsteemTestScore INTEGER,
                            DetailsFilePath TEXT,
                            DateTaken TEXT,
                            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
                        )''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_student(self, name, age, school, sex):
        try:
            c = self.conn.cursor()
            c.execute('INSERT INTO Students (Name, Age, School, Sex) VALUES (?, ?, ?, ?)', (name, age, school, sex))
            self.conn.commit()
            return c.lastrowid
        except sqlite3.Error as e:
            print(f"Error inserting student: {e}")
            return None

    def insert_test_results(self, student_id, stress_test_score, depression_test_score, self_esteem_test_score, details_file_path, date_taken):
        try:
            c = self.conn.cursor()
            c.execute('INSERT INTO Tests (StudentID, StressTestScore, DepressionTestScore, SelfEsteemTestScore, DetailsFilePath, DateTaken) VALUES (?, ?, ?, ?, ?, ?)',
                      (student_id, stress_test_score, depression_test_score, self_esteem_test_score, details_file_path, date_taken))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting test results: {e}")

    def query_test_results(self, student_id):
        try:
            c = self.conn.cursor()
            c.execute('''SELECT TestID, StudentID, StressTestScore, DepressionTestScore, SelfEsteemTestScore, DetailsFilePath, DateTaken FROM Tests WHERE StudentID = ?''', (student_id,))
            return c.fetchall()
        except sqlite3.Error as e:
            print(f"Error querying test results: {e}")
            return []

    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")

def print_student_results(db, student_id):
    results = db.query_test_results(student_id)
    for result in results:
        print(f"TestID: {result[0]}, StudentID: {result[1]}, Stress: {result[2]}, Depression: {result[3]}, Self-Esteem: {result[4]}, File: {result[5]}, Date: {result[6]}")

if __name__ == "__main__":
    db = DatabaseManager('student_tests.db')
    
    # Insert sample students
    student_id1 = db.insert_student('Alice Wonderland', 15, 'Wonderland High', 'F')
    student_id2 = db.insert_student('Bob Builder', 16, 'Builder Prep', 'M')
    
    # Insert test results for Alice
    db.insert_test_results(student_id1, 85, 78, 92, '/path/to/alice_details.txt', '2024-03-01')
    # Alice takes the tests again at a later date
    db.insert_test_results(student_id1, 88, 82, 94, '/path/to/alice_details_2.txt', '2024-05-01')
    
    # Insert test results for Bob
    db.insert_test_results(student_id2, 80, 75, 88, '/path/to/bob_details.txt', '2024-03-02')
    # Bob takes the tests again at a later date
    db.insert_test_results(student_id2, 85, 79, 90, '/path/to/bob_details_2.txt', '2024-05-02')

    # Print results to demonstrate
    print("Alice Wonderland's Test Results:")
    print_student_results(db, student_id1)
    print("\nBob Builder's Test Results:")
    print_student_results(db, student_id2)

    db.close()
