# main.py
# Main program file

import json
from admin import Admin
from library import Library

# -------- LOAD DATA  --------
try:
    with open("library_data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {
        "students": {},
        "teachers": {},
        "books": {}
    }

library = Library(data)
admin = Admin()

# -------- ADMIN LOGIN --------
print("=== ADMIN LOGIN ===")
user = input("Enter username: ")
pwd = input("Enter password: ")

if admin.login(user, pwd):

    print("Login successful")

    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Add Teacher")
        print("4. Show Teachers")
        print("5. Add Random CS Book")
        print("6. Show Books")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_student()

        elif choice == "2":
            library.show_students()

        elif choice == "3":
            library.add_teacher()

        elif choice == "4":
            library.show_teachers()

        elif choice == "5":
            library.add_random_cs_book()

        elif choice == "6":
            library.show_books()

        elif choice == "7":
            with open("library_data.json", "w") as file:
                json.dump(data, file)
            print("Data saved. Program closed.")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong username or password")
a