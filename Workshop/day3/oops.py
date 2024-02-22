class Person:
    def __init__(self,name,nationality):
        self.name=name
        self.nationality=nationality


person1= Person("Shivakant","India")

print(person1.name)
print(person1.nationality)


#inharitance

class Student(Person):

    def __init__(self, name, nationality):
       pass
    def name(self):
     print("this is Student")

class Cse(Student):

    def __init__(self, name, nationality):
       pass
    def name(self):
     print("this is Cse")
class Teacher(Person):

    def __init__(self, name, nationality):
       pass
    def name(self):
     print("this is Teacher")


s1=Student("shiva","luc")
print(s1.name())

c1=Cse()



