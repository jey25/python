
# # 2024-11-06 Class 생성
# class Circle():
    
#     pi = 3.14
    
#     def __init__(self, radius=1) -> None:
#         self.radius = radius
        
#     def area(self):
#         return self.radius*self.radius*self.pi
    
#     def perimeter(self):
#         return self.radius*2*Circle.pi

# mycircle = Circle(radius=4)
# print(mycircle.area())
# print(mycircle.perimeter())


# class Dog():
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
    
#     def calculate_human_age(self):
#         return self.age*7

# hans = Dog("Hans", "Sheperd", 7)
# human_age = hans.calculate_human_age()
# print(human_age)


# # 상속에 대한 연습
# class Person():
    
#     def __init__(self, first_name, last_name) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
        
#     def hello(self):
#         print("Hello")
        
#     def report(self):
#         print(f"{self.first_name} {self.last_name}")

# class Agent(Person):
    
#     # 부모 클래스의 속성에 추가 속성을 더 부여하는 방법
#     def __init__(self, first_name, last_name, code_name) -> None:
#         Person.__init__(self, first_name, last_name)
#         self.code_name = code_name
    
#     # 부모 클래스의 메서드를 오버라이트
#     def report(self):
#         print("Here")
    
#     def reveal(self, passcode):
#         if passcode == 123:
#             print("Pass")
#         else:
#             self.report()

# x = Agent("jang", "ey", "x")
# x.reveal(12)
# print(x.code_name)


# # 상속 테스트
# class Animal():
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def greet(self):
#         print("hi, {self.name}{self.species}")


# class Cat(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name, "Cat")
    
#     def sound(self):
#         print("cuff")
        
# class Dog(Animal):
    
#     def __init__(self, name):
#         Animal.__init__(self, name, "Dog")
        
#     def sound(self):
#         print("ruff")

# # 특수 메서드
# class Book():
    
#     def __init__(self, title, author, pages) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __str__(self) -> str:
#         return f"{self.title}{self.author}"
    
#     def __len__(self):
#         return self.pages
    
# book = Book("test", "jang", 120)
# print(book)
# print(len(book))


# class Students:
    
#     def __init__(self, names):
#         self.names = names
    
#     def __len__(self):
#         return len(self.names)
    
#     def __str__(self):
#         return f"{self.names}"
        
# students = Students(["A", "B", "C"])
# print(students)
# print(len(students))


