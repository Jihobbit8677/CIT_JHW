class Cal(object):
    def __init__(self,v1,v2):
        self.v1 = v2
        self.v2 = v1

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

c1 = Cal(50,30)
print(c1.subtract())




class C(object):
    def __init__(holo,v):
        holo.value = v
    def show(holo):
        print(holo.value)

c1 = C('hello')
c1.show()
c1.value = 30
c1.show()


class Person1:
    def __init__(self,name,age):
        self.namae = name
        self.age = age
    def hi(hihi):
        print(hihi.namae)

p1 = Person1('Jiho',23)


p1.hi()

print(p1.namae)
print(p1.age)


# class Person: #class()는 뭐임? (object)는?
#     def __init__(aha, name, age):
#         aha.name = name
#         aha.age = age
#
#     def myfunc(hoho):
#         print("Hello my name is " + hoho.name)
#
# p1 = Person("John", 36)
# p1.myfunc()
#
#
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
#
# s1 = Student('Mike','Woo')
# s1.printname()



class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)

x = Student('Mike' , 'Woo', 2024)
x.welcome()
