
students = []

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = int(grade)

    def info(self):
        print(f"Name: {self.name} | Age: {self.age} | Grade: {self.grade}")


while True:
    print("\n1 - Add student")
    print("2 - Show students")
    print("3 - Best student")
    print("4 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")

        student = Student(name, age, grade)
        students.append(student)

        print("Student added!")

    elif choice == "2":
        if not students:
            print("No students yet")
        else:
            for student in students:
                student.info()

    elif choice == "3":
        if not students:
            print("No students to compare")
        else:
            best = max(students, key=lambda x: x.grade)
            print("Best student:")
            best.info()

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice")