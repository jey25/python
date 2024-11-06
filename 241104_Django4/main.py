
class Student():
    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa
        

stu1 = Student(name="jang", gpa=5)
stu2 = Student(name="Su", gpa=7)

print(stu2.gpa)