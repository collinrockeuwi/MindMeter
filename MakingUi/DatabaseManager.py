import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.create_tables()
        #self.insert_sample_data()

        # Call the function to print scores and information for a specific name during setup
        self.print_student_scores_by_name("Jenet Jack")
    
 
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
                            DateOfBirth TEXT,
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
    def insert_student(self, name, date_of_birth, age, school, sex, date_registered):
        try:
            c = self.conn.cursor()
            c.execute('INSERT INTO Students (Name, DateOfBirth, Age, School, Sex, DateRegistered) VALUES (?, ?, ?, ?, ?, ?)', 
                    (name, date_of_birth, age, school, sex, date_registered))
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
        # Insert sample students with Date of Birth
        students = [
            ("Alice George", "2003-01-01", 20, "School A", "Female", "2023-01-01"),
            ("Bob Jones", "2002-02-02", 21, "School B", "Male", "2023-01-02"),
            ("Charlie Jackson", "2001-03-03", 22, "School C", "Male", "2023-01-03"),
            ("Diana Leslie", "2000-04-04", 23, "School D", "Female", "2023-01-04"),
            ("Ethan James", "1999-05-05", 24, "School E", "Male", "2023-01-05"),
            ("Fiona Singh", "1998-06-06", 25, "School F", "Female", "2023-01-06"),
            ("George Rione", "1997-07-07", 26, "School G", "Male", "2023-01-07"),
            ("Hannah Montana", "1996-08-08", 27, "School H", "Female", "2023-01-08"),
            ("Ian Jakes", "1995-09-09", 28, "School I", "Male", "2023-01-09"),
            ("Julia Mohammed", "1994-10-10", 29, "School J", "Female", "2023-01-10")
        ]
        for student in students:
            self.insert_student(*student)

        # Insert sample test scores for each student with different scores
        stress_scores_list = [
    [3, 2, 4, 3, 2, 4, 3, 2, 4, 3],  # Scores for Alice
    [2, 3, 4, 2, 3, 4, 2, 3, 4, 2],  # Scores for Bob
    [1, 3, 2, 4, 1, 3, 2, 4, 1, 3],  # Scores for Charlie
    [4, 2, 3, 1, 4, 2, 3, 1, 4, 2],  # Scores for Diana
    [3, 4, 1, 3, 4, 1, 3, 4, 1, 3],  # Scores for Ethan
    [2, 1, 4, 2, 1, 4, 2, 1, 4, 2],  # Scores for Fiona
    [1, 4, 3, 1, 4, 3, 1, 4, 3, 1],  # Scores for George
    [3, 1, 2, 4, 3, 1, 2, 4, 3, 1],  # Scores for Hannah
    [4, 3, 1, 2, 4, 3, 1, 2, 4, 3],  # Scores for Ian
    [2, 4, 3, 1, 2, 4, 3, 1, 2, 4],  # Scores for Julia
]
        self_esteem_scores_list = [
    [4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5],  # Scores for Alice
    [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4],  # Scores for Bob
    [4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3],  # Scores for Charlie
    [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4],  # Scores for Diana
    [5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4],  # Scores for Ethan
    [4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3],  # Scores for Fiona
    [3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5],  # Scores for George
    [5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3],  # Scores for Hannah
    [4, 5, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4],  # Scores for Ian
    [3, 4, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3, 5, 4, 3],  # Scores for Julia
]
        depression_scores_list = [
    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],  # Scores for Alice
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],  # Scores for Bob
    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],  # Scores for Charlie
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],  # Scores for Diana
    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],  # Scores for Ethan
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],  # Scores for Fiona
    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],  # Scores for George
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],  # Scores for Hannah
    [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2],  # Scores for Ian
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],  # Scores for Julia
]

        for i in range(1, 11):  # Assuming there are 10 students
            stress_scores = stress_scores_list[i - 1]
            self_esteem_scores = self_esteem_scores_list[i - 1]
            depression_scores = depression_scores_list[i - 1]

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
                            s.Name,s.DateOfBirth, s.Age, s.Sex, s.School, 
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


    def print_student_scores_by_name(self, name):
        try:
            c = self.conn.cursor()
            # Fetch student information
            c.execute('''SELECT Name, DateOfBirth, Age, School, Sex, DateRegistered
                        FROM Students
                        WHERE Name = ?''', (name,))
            student_info = c.fetchone()
            if student_info:
                print(f"Student Information for {name}:")
                print(f"Name: {student_info[0]}")
                print(f"Date of Birth: {student_info[1]}")
                print(f"Age: {student_info[2]}")
                print(f"School: {student_info[3]}")
                print(f"Sex: {student_info[4]}")
                print(f"Date Registered: {student_info[5]}")
                print("\nScores:")
            else:
                print(f"No information found for {name}")
                return

            # Fetch and print stress scores
            c.execute('''SELECT DateTaken, TotalScore, Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10
                        FROM StressTests
                        JOIN Students ON StressTests.StudentID = Students.StudentID
                        WHERE Students.Name = ?''', (name,))
            print("Stress Scores:")
            for score in c.fetchall():
                print(f"Date Taken: {score[0]}, Total Score: {score[1]}, Scores: {score[2:]}")

            # Fetch and print depression scores
            c.execute('''SELECT DateTaken, TotalScore, Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10, Question11, Question12, Question13, Question14, Question15
                        FROM DepressionTests
                        JOIN Students ON DepressionTests.StudentID = Students.StudentID
                        WHERE Students.Name = ?''', (name,))
            print("Depression Scores:")
            for score in c.fetchall():
                print(f"Date Taken: {score[0]}, Total Score: {score[1]}, Scores: {score[2:]}")

            # Fetch and print self-esteem scores
            c.execute('''SELECT DateTaken, TotalScore, Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10, Question11, Question12, Question13, Question14, Question15, Question16, Question17, Question18, Question19, Question20
                        FROM SelfEsteemTests
                        JOIN Students ON SelfEsteemTests.StudentID = Students.StudentID
                        WHERE Students.Name = ?''', (name,))
            print("Self-Esteem Scores:")
            for score in c.fetchall():
                print(f"Date Taken: {score[0]}, Total Score: {score[1]}, Scores: {score[2:]}")

        except sqlite3.Error as e:
            print(f"Error querying scores: {e}")



    def update_student(self, student_id, name, date_of_birth, age, school, sex, date_registered):
        try:
            c = self.conn.cursor()
            c.execute('''UPDATE Students SET Name=?, DateOfBirth=?, Age=?, School=?, Sex=?, DateRegistered=? WHERE StudentID=?''',
                    (name, date_of_birth, age, school, sex, date_registered, student_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating student: {e}")


    def get_test_dates_by_student_id(self, student_id, test_table):
        try:
            c = self.conn.cursor()
            # Exclude tests where all scores are None
            c.execute(f'''SELECT DateTaken FROM {test_table} 
                        WHERE StudentID = ? 
                        AND (Question1 IS NOT NULL OR Question2 IS NOT NULL OR Question3 IS NOT NULL OR Question4 IS NOT NULL OR Question5 IS NOT NULL)
                        ORDER BY DateTaken''', (student_id,))
            return [row[0] for row in c.fetchall()]
        except sqlite3.Error as e:
            print(f"Error fetching test dates: {e}")
            return []


    def get_test_details_by_date(self, student_id, date_taken, test_table):
        try:
            c = self.conn.cursor()
            query = f'SELECT * FROM {test_table} WHERE StudentID = ? AND DateTaken = ?'
            c.execute(query, (student_id, date_taken))
            test_details = c.fetchone()
            if test_details:
                # Assuming the first two columns are TestID and StudentID
                test_scores = test_details[2:-2]  # Excluding TestID, StudentID, TotalScore, DateTaken
                total_score = test_details[-2]  # Assuming the second to last column is TotalScore
                return {'scores': test_scores, 'total_score': total_score}
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error fetching test details by date: {e}")
            return None



    def fetch_general_info_by_name(self, student_name):
        # Connect to the database
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Query to fetch general information for the given student name, including the StudentID
        query = '''SELECT StudentID, Name, DateOfBirth, Age, School, Sex, DateRegistered
                FROM Students
                WHERE Name = ?'''
        cursor.execute(query, (student_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Close the database connection
        conn.close()

        # Debug print the raw result
        print("Raw fetched data:", result)

        # Return the result as a dictionary or None if no record is found
        if result:
            # Use the column names as they appear in the SELECT statement
            columns = ["StudentID", "Name", "DateOfBirth", "Age", "School", "Sex", "DateRegistered"]
            return dict(zip(columns, result))
        else:
            return None




if __name__ == "__main__":
    db = DatabaseManager('student_tests.db')
    # Sample usage...
