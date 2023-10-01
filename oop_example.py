class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old, and my student ID is {self.student_id}.")

if __name__ == "__main__":
    person = Person("Alice", 30)
    student = Student("Bob", 20, "S12345")

    person.introduce()
    student.introduce()
