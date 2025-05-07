import sqlite3

# Function to insert student data
def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

# Function to insert course data
def add_course(cursor, course_name, instructor_name):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?, ?)", (course_name, instructor_name))
    except sqlite3.IntegrityError:
        print(f"{course_name} is already in the database.")

def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return
    
    cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Student {student} is already enrolled in course {course}.")
        return
    
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    
# Connect to the database
with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign keys
    cursor = conn.cursor()

    # Add sample students
    add_student(cursor, 'Alice', 20, 'Computer Science')
    add_student(cursor, 'Bob', 22, 'History')
    add_student(cursor, 'Charlie', 19, 'Biology')

    # Add sample courses
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")


    conn.commit()
    print("Sample data inserted successfully.")

    # Query Alice's record
    cursor.execute("SELECT * FROM Students WHERE name = 'Alice'")
    result = cursor.fetchall()
    for row in result:
        print(row)  
