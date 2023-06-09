import sqlite3

# Connect to the database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

def create_tables():
    # Create Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT,
        student_email TEXT
    )
    """)

    # Create Attendance table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Attendance (
        attendance_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        date DATE,
        status TEXT,
        FOREIGN KEY (student_id) REFERENCES Students(student_id)
    )
    """)

def mark_attendance(date, total_students):
    for student_id in range(1, total_students + 1):
        status = input(f"Enter attendance status for Student ID {student_id} (P/A): ")
        if status.lower() == "p":
            status = "Present"
        elif status.lower() == "a":
            status = "Absent"
        else:
            status = "Unknown"
        cursor.execute("INSERT INTO Attendance (student_id, date, status) VALUES (?, ?, ?)", (student_id, date, status))
    
    conn.commit()
    print("Attendance marked successfully!")

def get_attendance_by_student(student_id):
    cursor.execute("""
    SELECT a.date, a.status
    FROM Attendance a
    WHERE a.student_id = ?
    """, (student_id,))
    attendance = cursor.fetchall()
    if len(attendance) > 0:
        print(f"Attendance records for Student ID {student_id}:")
        for record in attendance:
            print(f"Date: {record[0]}, Status: {record[1]}")
    else:
        print(f"No attendance records found for Student ID {student_id}")

def main():
    create_tables()

    while True:
        print("\nAttendance Management System")
        print("1. Mark Attendance")
        print("2. View Attendance by Student")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            date = input("Enter Date (YYYY-MM-DD): ")
            total_students = int(input("Enter the total number of students: "))
            mark_attendance(date, total_students)
            print("Attendance marked successfully!")

        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            get_attendance_by_student(student_id)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
