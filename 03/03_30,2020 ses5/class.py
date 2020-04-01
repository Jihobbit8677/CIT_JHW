class Person:
  def __init__(sf, name, age):
    sf.namae = name
    sf.toshi = age

p1 = Person("John", 36)
p2 = Person ("Jiho", 24)

print(p1.namae)
print(p1.toshi)

class MyClass:
  x = 5

  def hi(dkfk): #파이썬은 안에 매개변수가 최소 1개 있어야만 한다.
      print("hi!")
      print( dkfk.x + 8)

a = MyClass()
a.x -= 9
a.hi()


class MyClass:
    x = 5

    def hi(ddf):
        print('hi!')
        print(ddf.x + 8)

c1 = MyClass()
c1.x -= 9
c1.hi()
