class Student:
    def __init__(self, name: str, age: int, grade: float) -> None:
        self.__name = name
        self.__age = age
        self.__grade = grade
        
    @property
    def name(self):
        return self.__name
    
    @name.setter #the function to must be a property
    def name(self, name: str):
        self.__name = name
        
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age: int):
        self.__age = age
        
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade: float):
        self.__grade = grade
        

jean = Student("jean", 29, 4.3)
#print(jean._Student__name)

print(jean.age)
jean.age = 19
print(jean.age)

print(jean.name)
jean.name = "jean paul"
print(jean.name)

print(jean.grade)
jean.grade = 1.9
print(jean.grade)
