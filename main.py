class StudentManagement:

    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Course Name: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        for student in self.students:
            print(student)

    def search_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == student_id:
                print("Student Found:", student)
                return

        print("Student Not Found!")


system = StudentManagement()

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")