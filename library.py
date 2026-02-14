# library.py
# This file contains all library logic

import random

class Library:
    def __init__(self, data):
        self.students = data["students"]
        self.teachers = data["teachers"]
        self.books = data["books"]

    # ---------- STUDENT ----------
    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        self.students[sid] = name
        print("Student added successfully")

    def show_students(self):
        print("\n--- Students ---")
        if not self.students:
            print("No students found")
        for sid, name in self.students.items():
            print(sid, name)

    # ---------- TEACHER ----------
    def add_teacher(self):
        tid = input("Enter Teacher ID: ")
        name = input("Enter Teacher Name: ")

        self.teachers[tid] = name
        print("Teacher added successfully")

    def show_teachers(self):
        print("\n--- Teachers ---")
        if not self.teachers:
            print("No teachers found")
        for tid, name in self.teachers.items():
            print(tid, name)

    # ---------- BOOK ----------
    def add_random_cs_book(self):
        cs_books = [
            "Python Programming",
            "Data Structures",
            "Operating Systems",
            "Database Systems",
            "Computer Networks",
            "Cyber Security",
            "Artificial Intelligence",
            "Web Development"
        ]

        book_id = "CS-" + str(random.randint(100, 999))
        book_name = random.choice(cs_books)

        self.books[book_id] = book_name
        print("Book added:", book_id, book_name)

    def show_books(self):
        print("\n--- Books ---")
        if not self.books:
            print("No books found")
        for bid, book in self.books.items():
            print(bid, book)
