a = ['최희찬','우지호',32, False]

b= {'Apple':257, 'Amazon':False}

c = b['Apple']
print(c)

d= c + a[2]
print(d)

a[3] = True

print(a)
z = a[0] #꽁쳐 놓기
a[0]=a[1]
a[1]=z
print(a)
