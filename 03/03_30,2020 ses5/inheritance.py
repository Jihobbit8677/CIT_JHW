# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sayhi(nam):
#         print('hi, my name is '+ nam.name )
#
#
# class Professor(Person):
#     def __init__(self, department, nm, age):
#         super().__init__(nm, age)
#         self.dpt = department
#
#     def profSayHi(s):
#         print("hi, I am professsor " + s.name + " from " + s.dpt + " department.")
#
# jack = Professor("CS", "jack", 54)
# jack.profSayHi()
# jack.sayhi()
#
# p1 = Person('jiho','25')
# p1.sayhi()






# 설문조사 프로그램

class BasicInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printBI(self):
        print(self.name, self.age)
        print('--------------------------------------')

class Survey(BasicInfo):
    def __init__(self, name, age, pref):
        super().__init__(name, age)
        self.pref = pref

    def printPref(self):
        print(self.pref)
        print('--------------------------------------')


nm = input('Enter ur name:')
ag = input('Enter ur age:')
prf = input('Enter ur preference:')
s1 = Survey(nm, ag, prf)
s1.printBI()
s1.printPref()





class MyClass(object)
