class Person:
    name = ""
    age = ""
    nationality = ""

    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setAge(self,age):
        self.age = age

    def getAge(self):
        return self.age
    
    def setNationality(self,nationality):
        self.nationality = nationality
    
    def getNationality(self):
        return self.nationality
    

class Teacher(Person):
    def print_teacher(self):
        print("I am a Teacher !")

class Student(Person):
    def print_Student(self):
        print("I am Student !")


def printDetails(obj):
    print(f"My Name is {obj.getName()}")
    print(f"I am {obj.getAge()} old  ")
    print(f"My Nationality is {obj.getNationality()}")

person1 = Teacher()
person1.setName("David")
person1.setAge(35)
person1.setNationality("Indian")
printDetails(person1)
person1.print_teacher()

print("--------------------------------- \n")
person2 = Student()
person2.setName("vasu")
person2.setAge(18)
person2.setNationality("Indian")
printDetails(person2)
person2.print_Student()