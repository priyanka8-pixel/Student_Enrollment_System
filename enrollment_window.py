import mysql.connector
import tkinter as tk
from tkinter import messagebox

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="student_db"
    )

def enroll_student():
    student_id = id_entry.get()
    name = name_entry.get()
    father = father_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    course = course_entry.get()

    if student_id=="" or name=="" or father=="" or age=="" or gender=="" or course=="":
        messagebox.showerror("Error", "All fields required")
        return

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,CURDATE())",
        (student_id, name, father, age, gender, course)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Enrolled Successfully")


def view_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    if not data:
        messagebox.showinfo("Students", "No students found")
        return
    result = ""
    for row in data:
        result += f"ID:{row[0]} | Name:{row[1]} | Course:{row[5]}\n"

    messagebox.showinfo("Student List", result)


def delete_enrollment():
    student_id = delete_id_entry.get()
    if student_id == "":
        messagebox.showerror("Error", "Enter Student ID")
        return

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
    conn.commit()

    if cur.rowcount > 0:
        messagebox.showinfo("Success", "Enrollment Deleted")
    else:
        messagebox.showwarning("Warning", "ID not found")

    conn.close()

# TKINTER WINDOW

root = tk.Tk()
root.title("Student Enrollment System")
root.geometry("350x450")

tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Father Name").pack()
father_entry = tk.Entry(root)
father_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender").pack()
gender_entry = tk.Entry(root)
gender_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Button(root, text="Add Student", command=enroll_student).pack(pady=5)

tk.Label(root, text="Student ID to Delete").pack()
delete_id_entry = tk.Entry(root)
delete_id_entry.pack()

tk.Button(root, text="Delete Enrollment", command=delete_enrollment).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=10)

root.mainloop()
