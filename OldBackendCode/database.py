import sqlite3

def init_db():
    conn = sqlite3.connect('student_profiles.db')
    c = conn.cursor()

    c.execute("PRAGMA table_info(profiles)")
    columns = [info[1] for info in c.fetchall()]

    required_columns = {'id', 'name', 'age', 'sex', 'school', 'stress_test_score', 'depression_test_score', 'self_esteem_test_score', 'image_path', 'comments'}
    if not required_columns.issubset(set(columns)):
        c.execute("DROP TABLE IF EXISTS profiles")
        c.execute('''CREATE TABLE profiles (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    sex TEXT,
                    school TEXT,
                    stress_test_score INTEGER,
                    depression_test_score INTEGER,
                    self_esteem_test_score INTEGER,
                    image_path TEXT,
                    comments TEXT)''')
    else:
        if 'comments' not in columns:
            c.execute("ALTER TABLE profiles ADD COLUMN comments TEXT")

    conn.commit()

    # Check if the table is empty before inserting sample data
    c.execute("SELECT COUNT(*) FROM profiles")
    if c.fetchone()[0] == 0:
        insert_sample_data(c)

    conn.commit()
    conn.close()

def insert_sample_data(c):
    sample_data = [
        ('John Doe', 25, 'Male', 'Springfield High', 10, 5, 8, 'path/to/image1.png', 'Very motivated.'),
('Jane Smith', 30, 'Female', 'Shelbyville High', 7, 6, 9, 'path/to/image2.png', 'Needs follow up.'),
('Jake Blues', 28, 'Male', 'Springfield College', 6, 7, 5, 'path/to/image3.png', 'Excellent progress.'),
('Elwood Blues', 29, 'Male', 'Shelbyville College', 8, 8, 7, 'path/to/image4.png', 'Struggling with stress.'),
('Jessie Doe', 27, 'Female', 'Springfield University', 9, 4, 6, 'path/to/image5.png', 'Shows great improvement.'),
('Alex King', 24, 'Male', 'North Springfield High', 5, 9, 8, 'path/to/image6.png', 'Very anxious.'),
('Eva Joy', 22, 'Female', 'South Shelbyville High', 8, 5, 7, 'path/to/image7.png', 'Positive attitude.'),
('Marco Polo', 26, 'Male', 'East Springfield College', 7, 8, 6, 'path/to/image8.png', 'Difficulty focusing.'),
('Lucy Heart', 29, 'Female', 'West Shelbyville College', 6, 6, 9, 'path/to/image9.png', 'Very confident.'),
('Omar Little', 28, 'Male', 'Central Springfield University', 9, 7, 5, 'path/to/image10.png', 'Lacks self-esteem.'),
        # Add more sample data...
    ]
    for row in sample_data:
        c.execute("INSERT INTO profiles (name, age, sex, school, stress_test_score, depression_test_score, self_esteem_test_score, image_path, comments) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

if __name__ == "__main__":
    init_db()
