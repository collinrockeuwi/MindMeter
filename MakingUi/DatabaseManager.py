import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.create_tables()
        #self.insert_sample_data()
    
 
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
                            Sex TEXT,
                            DateRegistered TEXT
                        )''')

            # Create separate tables for each test type with constraints
            c.execute('''CREATE TABLE IF NOT EXISTS StressTests (
                            TestID INTEGER PRIMARY KEY AUTOINCREMENT,
                            StudentID INTEGER,
                            Question1 INTEGER CHECK (Question1 BETWEEN 1 AND 5),
                            Question2 INTEGER CHECK (Question2 BETWEEN 1 AND 5),
                            Question3 INTEGER CHECK (Question3 BETWEEN 1 AND 5),
                            Question4 INTEGER CHECK (Question4 BETWEEN 1 AND 5),
                            Question5 INTEGER CHECK (Question5 BETWEEN 1 AND 5),
                            Question6 INTEGER CHECK (Question6 BETWEEN 1 AND 5),
                            Question7 INTEGER CHECK (Question7 BETWEEN 1 AND 5),
                            Question8 INTEGER CHECK (Question8 BETWEEN 1 AND 5),
                            Question9 INTEGER CHECK (Question9 BETWEEN 1 AND 5),
                            Question10 INTEGER CHECK (Question10 BETWEEN 1 AND 5),
                            TotalScore INTEGER,
                            DateTaken TEXT,
                            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
                        )''')

            c.execute('''CREATE TABLE IF NOT EXISTS SelfEsteemTests (
                            TestID INTEGER PRIMARY KEY AUTOINCREMENT,
                            StudentID INTEGER,
                            Question1 INTEGER,
                            Question2 INTEGER,
                            Question3 INTEGER,
                            Question4 INTEGER,
                            Question5 INTEGER,
                            Question6 INTEGER,
                            Question7 INTEGER,
                            Question8 INTEGER,
                            Question9 INTEGER,
                            Question10 INTEGER,
                            Question11 INTEGER,
                            Question12 INTEGER,
                            Question13 INTEGER,
                            Question14 INTEGER,
                            Question15 INTEGER,
                            Question16 INTEGER,
                            Question17 INTEGER,
                            Question18 INTEGER,
                            Question19 INTEGER,
                            Question20 INTEGER,
                            TotalScore INTEGER,
                            DateTaken TEXT,
                            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
                        )''')

            c.execute('''CREATE TABLE IF NOT EXISTS DepressionTests (
                            TestID INTEGER PRIMARY KEY AUTOINCREMENT,
                            StudentID INTEGER,
                            Question1 INTEGER CHECK (Question1 BETWEEN 1 AND 5),
                            Question2 INTEGER CHECK (Question2 BETWEEN 1 AND 5),
                            Question3 INTEGER CHECK (Question3 BETWEEN 1 AND 5),
                            Question4 INTEGER CHECK (Question4 BETWEEN 1 AND 5),
                            Question5 INTEGER CHECK (Question5 BETWEEN 1 AND 5),
                            Question6 INTEGER CHECK (Question6 BETWEEN 1 AND 5),
                            Question7 INTEGER CHECK (Question7 BETWEEN 1 AND 5),
                            Question8 INTEGER CHECK (Question8 BETWEEN 1 AND 5),
                            Question9 INTEGER CHECK (Question9 BETWEEN 1 AND 5),
                            Question10 INTEGER CHECK (Question10 BETWEEN 1 AND 5),
                            Question11 INTEGER CHECK (Question11 BETWEEN 1 AND 5),
                            Question12 INTEGER CHECK (Question12 BETWEEN 1 AND 5),
                            Question13 INTEGER CHECK (Question13 BETWEEN 1 AND 5),
                            Question14 INTEGER CHECK (Question14 BETWEEN 1 AND 5),
                            Question15 INTEGER CHECK (Question15 BETWEEN 1 AND 5),
                            TotalScore INTEGER,
                            DateTaken TEXT,
                            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
                        )''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

   

#for different test insertions
    def insert_student(self, name, age, school, sex, date_registered):
            try:
                c = self.conn.cursor()
                c.execute('INSERT INTO Students (Name, Age, School, Sex, DateRegistered) VALUES (?, ?, ?, ?, ?)', (name, age, school, sex, date_registered))
                self.conn.commit()
                return c.lastrowid
            except sqlite3.Error as e:
                print(f"Error inserting student: {e}")
                return None

    
    def insert_self_esteem_test(self, student_id, scores, total_score, date_taken):
        try:
            c = self.conn.cursor()
            # Ensure that 'scores' has 20 values for the 20 questions
            if len(scores) != 20:
                raise ValueError("Expected 20 scores for SelfEsteemTest")

            c.execute('''INSERT INTO SelfEsteemTests (StudentID, Question1, Question2, Question3, Question4, Question5,
                                                    Question6, Question7, Question8, Question9, Question10, Question11,
                                                    Question12, Question13, Question14, Question15, Question16, Question17,
                                                    Question18, Question19, Question20, TotalScore, DateTaken)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (student_id, *scores, total_score, date_taken))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting self-esteem test: {e}")

    def insert_stress_test(self, student_id, scores, total_score, date_taken):
        try:
            c = self.conn.cursor()
            # Ensure that 'scores' has 10 values for the 10 questions
            if len(scores) != 10:
                raise ValueError("Expected 10 scores for StressTest")

            c.execute('''INSERT INTO StressTests (StudentID, Question1, Question2, Question3, Question4, Question5,
                                                Question6, Question7, Question8, Question9, Question10, TotalScore, DateTaken)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (student_id, *scores, total_score, date_taken))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting stress test: {e}")

    def insert_depression_test(self, student_id, scores, total_score, date_taken):
        try:
            c = self.conn.cursor()
            # Ensure that 'scores' has 15 values for the 15 questions
            if len(scores) != 15:
                raise ValueError("Expected 15 scores for DepressionTest")

            c.execute('''INSERT INTO DepressionTests (StudentID, Question1, Question2, Question3, Question4, Question5,
                                                    Question6, Question7, Question8, Question9, Question10, Question11,
                                                    Question12, Question13, Question14, Question15, TotalScore, DateTaken)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (student_id, *scores, total_score, date_taken))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting depression test: {e}")

    
#Get specific test based on student id
    def query_tests_by_student(self, student_id):
        try:
            c = self.conn.cursor()
            c.execute('''SELECT * FROM StressTests WHERE StudentID = ?''', (student_id,))
            stress_tests = c.fetchall()
            c.execute('''SELECT * FROM SelfEsteemTests WHERE StudentID = ?''', (student_id,))
            self_esteem_tests = c.fetchall()
            c.execute('''SELECT * FROM DepressionTests WHERE StudentID = ?''', (student_id,))
            depression_tests = c.fetchall()
            return {
                'stress_tests': stress_tests,
                'self_esteem_tests': self_esteem_tests,
                'depression_tests': depression_tests
            }
        except sqlite3.Error as e:
            print(f"Error querying tests: {e}")
            return {}
        

     #comparison based on dates   
    def get_stress_test_scores_by_student_and_dates(self, student_id, date1=None, date2=None):
        try:
            c = self.conn.cursor()
            if date1 and date2:
                c.execute('''SELECT * FROM StressTests WHERE StudentID = ? AND (DateTaken = ? OR DateTaken = ?) ORDER BY DateTaken''', (student_id, date1, date2))
            elif date1:
                c.execute('''SELECT * FROM StressTests WHERE StudentID = ? AND DateTaken = ?''', (student_id, date1))
            else:
                c.execute('''SELECT * FROM StressTests WHERE StudentID = ? ORDER BY DateTaken''', (student_id,))
            return c.fetchall()
        except sqlite3.Error as e:
            print(f"Error querying stress test scores: {e}")
            return []
        
    def compare_stress_test_scores(db, student_id, date1, date2):
        scores = db.get_stress_test_scores_by_student_and_dates(student_id, date1, date2)
        if len(scores) == 2:
            print(f"Comparing scores for {date1} and {date2}:")
            print(f"Date: {scores[0]['DateTaken']}, Total Score: {scores[0]['TotalScore']}")
            print(f"Date: {scores[1]['DateTaken']}, Total Score: {scores[1]['TotalScore']}")
            # Add additional comparison logic here if needed
        else:
            print("One or both of the specified dates do not have test scores.")


    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")

   
   #sample datra
    def insert_sample_data(self):
        # Insert sample students
        students = [
            ("Alice", 20, "School A", "Female", "2023-01-01"),
            ("Bob", 21, "School B", "Male", "2023-01-02"),
            ("Charlie", 22, "School C", "Male", "2023-01-03"),
            ("Diana", 23, "School D", "Female", "2023-01-04"),
            ("Ethan", 24, "School E", "Male", "2023-01-05"),
            ("Fiona", 25, "School F", "Female", "2023-01-06"),
            ("George", 26, "School G", "Male", "2023-01-07"),
            ("Hannah", 27, "School H", "Female", "2023-01-08"),
            ("Ian", 28, "School I", "Male", "2023-01-09"),
            ("Julia", 29, "School J", "Female", "2023-01-10")
        ]
        for student in students:
            self.insert_student(*student)

        # Insert sample test scores for each student
        for i in range(1, 11):
            stress_scores = [3, 4, 2, 5, 3, 4, 2, 5, 3, 4]
            self_esteem_scores = [4, 4, 3, 5, 4, 4, 3, 5, 4, 4, 3, 5, 4, 4, 3, 5, 4, 4, 3, 5]  # Ensure this list has 20 elements
            depression_scores = [2, 3, 2, 4, 3, 3, 2, 4, 3, 3, 2, 4, 3, 3, 2]  # Ensure this list has 15 elements

            stress_total_score = sum(stress_scores)
            self_esteem_total_score = sum(self_esteem_scores)
            depression_total_score = sum(depression_scores)

            date_taken = f"2023-02-{i:02d}"

            self.insert_stress_test(i, stress_scores, stress_total_score, date_taken)
            self.insert_self_esteem_test(i, self_esteem_scores, self_esteem_total_score, date_taken)
            self.insert_depression_test(i, depression_scores, depression_total_score, date_taken)

#Database Tab query
    def fetch_student_test_summary(self):
        try:
            c = self.conn.cursor()
            c.execute('''SELECT 
                            s.Name, s.Age, s.Sex, s.School, 
                            MAX(st.TotalScore) AS MaxStressScore, 
                            MAX(dt.TotalScore) AS MaxDepressionScore, 
                            MAX(se_tests.TotalScore) AS MaxSelfEsteemScore
                        FROM Students s
                        LEFT JOIN StressTests st ON s.StudentID = st.StudentID
                        LEFT JOIN DepressionTests dt ON s.StudentID = dt.StudentID
                        LEFT JOIN SelfEsteemTests se_tests ON s.StudentID = se_tests.StudentID
                        GROUP BY s.StudentID''')
            return c.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching student test summary: {e}")
            return []





if __name__ == "__main__":
    db = DatabaseManager('student_tests.db')
    # Sample usage...
