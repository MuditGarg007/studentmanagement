import mysql.connector

# Establish a database connection
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="school_management"
        )
        return connection
    except:
        return none

# Function to add a new student
def add_student(student_id, name, course, grade):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "INSERT INTO students (student_id, name, course, grade) VALUES (%s, %s, %s, %s)"
            data = (student_id, name, course, grade)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Student added successfully!")
    finally:
        if connection:
            connection.close()

# Function to update a student's information
def update_student(student_id, new_name, new_course, new_grade):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "UPDATE students SET name=%s, course=%s, grade=%s WHERE student_id=%s"
            data = (new_name, new_course, new_grade, student_id)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Student information updated successfully!")
    finally:
        if connection:
            connection.close()

# Function to delete a student
def delete_student(student_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "DELETE FROM students WHERE student_id=%s"
            data = (student_id,)
            cursor.execute(sql_query, data)
            connection.commit()
            print("Student deleted successfully!")
    finally:
        if connection:
            connection.close()

# Function to retrieve student information by student ID
def get_student_info(student_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM students WHERE student_id=%s"
            data = (student_id,)
            cursor.execute(sql_query, data)
            student = cursor.fetchone()
            if student:
                return student
            else:
                print("Student not found.")
    finally:
        if connection:
            connection.close()

# Function to list all students
def list_students():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM students"
            cursor.execute(sql_query)
            students = cursor.fetchall()
            return students
    finally:
        if connection:
            connection.close()

# Function to find students by a specific course
def find_students_by_course(course):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM students WHERE course=%s"
            data = (course,)
            cursor.execute(sql_query, data)
            students = cursor.fetchall()
            return students
    finally:
        if connection:
            connection.close()

# Function to find students by a specific grade
def find_students_by_grade(grade):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM students WHERE grade=%s"
            data = (grade,)
            cursor.execute(sql_query, data)
            students = cursor.fetchall()
            return students
    finally:
        if connection:
            connection.close()

def main():
    connect_to_database()
    while True:
    print("Select an option:")
    print("1. Add a student")
    print("2. Update student information")
    print("3. Delete a student")
    print("4. Retrieve student information by ID")
    print("5. List all students")
    print("6. Find students by course")
    print("7. Find students by grade")
    print("8. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        course = input("Enter student course: ")
        grade = input("Enter student grade: ")
        add_student(student_id, name, course, grade)

    elif choice == "2":
        student_id = input("Enter student ID to update: ")
        new_name = input("Enter new name: ")
        new_course = input("Enter new course: ")
        new_grade = input("Enter new grade: ")
        update_student(student_id, new_name, new_course, new_grade)

    elif choice == "3":
        student_id = input("Enter student ID to delete: ")
        delete_student(student_id)

    elif choice == "4":
        student_id = input("Enter student ID to retrieve information: ")
        student_info = get_student_info(student_id)
        if student_info:
            print("Student Information:")
            print("ID:", student_info[0])
            print("Name:", student_info[1])
            print("Course:", student_info[2])
            print("Grade:", student_info[3])

    elif choice == "5":
        students = list_students()
        if students:
            print("List of Students:")
            for student in students:
                print("ID:", student[0])
                print("Name:", student[1])
                print("Course:", student[2])
                print("Grade:", student[3])

    elif choice == "6":
        course = input("Enter course to find students: ")
        students = find_students_by_course(course)
        if students:
            print("Students in Course", course)
            for student in students:
                print("ID:", student[0])
                print("Name:", student[1])
                print("Course:", student[2])
                print("Grade:", student[3])

    elif choice == "7":
        grade = input("Enter grade to find students: ")
        students = find_students_by_grade(grade)
        if students:
            print("Students with Grade", grade)
            for student in students:
                print("ID:", student[0])
                print("Name:", student[1])
                print("Course:", student[2])
                print("Grade:", student[3])

    elif choice == "8":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
main()

