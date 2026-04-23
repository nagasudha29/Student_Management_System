
import json
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def display(self):
        pass



class Student(Person):
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}, Grade: {self.calculate_grade()}")

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }



class FileManager:
    FILE_NAME = "students.json"

    @staticmethod
    def save_data(data):
        with open(FileManager.FILE_NAME, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_data():
        try:
            with open(FileManager.FILE_NAME, "r") as f:
                return json.load(f)
        except:
            return []



class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()

    def add_student(self, student):
        self.students.append(student)
        print("✅ Student added successfully")

    def view_students(self):
        if not self.students:
            print("❌ No students found")
        for s in self.students:
            s.display()

    def search_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                s.display()
                return s
        print("❌ Student not found")
        return None

    def update_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.marks = int(input("Enter new marks: "))
            print("✅ Student updated")

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("✅ Student deleted")
                return
        print("❌ Student not found")

    def save_students(self):
        data = [s.to_dict() for s in self.students]
        FileManager.save_data(data)
        print("💾 Data saved successfully")

    def load_students(self):
        data = FileManager.load_data()
        for d in data:
            student = Student(d["id"], d["name"], d["age"], d["marks"])
            self.students.append(student)



class Admin:
    USERNAME = "admin"
    PASSWORD = "1234"

    @staticmethod
    def login():
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == Admin.USERNAME and password == Admin.PASSWORD:
            print("✅ Login successful")
            return True
        else:
            print("❌ Invalid login")
            return False



def main():
    print("🎓 Student Management System")

    if not Admin.login():
        return

    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = int(input("Enter Marks: "))
            student = Student(sid, name, age, marks)
            manager.add_student(student)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            sid = input("Enter ID to search: ")
            manager.search_student(sid)

        elif choice == "4":
            sid = input("Enter ID to update: ")
            manager.update_student(sid)

        elif choice == "5":
            sid = input("Enter ID to delete: ")
            manager.delete_student(sid)

        elif choice == "6":
            manager.save_students()

        elif choice == "7":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")
if __name__ == "__main__":
    main()
#git add .
#git commit -m "msg"
#git push 