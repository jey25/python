
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


class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def calculate_human_age(self):
        return self.age*7

hans = Dog("Hans", "Sheperd", 7)
human_age = hans.calculate_human_age()
print(human_age)
