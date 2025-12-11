import sqlite3

conn=sqlite3.connect('school.db')
c=cur=conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS grades(
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT,
    mark INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
""")
conn.commit()

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    c.execute("INSERT INTO students(name, age,grade) VALUES (?,?,?)", (name, age,grade))
    conn.commit()
    print("Student added successfully!\n")
# c.execute("ALTER TABLE STUDENTS ADD COLUMN batch TEXT ;")

add_student()

def add_grade():
    student_id = int(input("Enter Student ID: "))
    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))
    c.execute("INSERT INTO grades(student_id, subject, mark) VALUES (?,?,?)",
              (student_id, subject, mark))
    conn.commit()
    print("Grade added!\n")

# add_grade()

def view_students():
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    for student in students:
        print(student)
    print("\n")

# view_students()

def view_grades():
    c.execute("SELECT * FROM grades")
    grades = c.fetchall()
    for grade in grades:
        print(grade)
    print("\n")

# view_grades()

def delete_student():
    student_id = int(input("Enter Student ID: "))
    c.execute("DELETE FROM students WHERE student_id = 1"
              "")
    conn.commit()
    print("Student deleted successfully!\n")

# delete_student()

def aded_student():
    c.execute("SELECT * FROM grades WHERE grade_id = 1")
    grades = c.fetchall()
    for grade in grades:
        print(grade)




add_student()

while True:
    print("Student Grading")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Students")
    print("4. View Grades")
    print("5. Delete Student")

    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        view_students()
    elif choice == "4":
        view_grades()
    elif choice=="5":
        delete_student()
    else:
        print("Invalid choice\n")

menu()
conn.close()





























