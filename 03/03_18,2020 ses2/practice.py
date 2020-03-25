# print('mom\'s spaghetti')
# print('\"life is short\"\nhe said.') #\붙여주기, \n이용
# print(3!=4)
# print('app'<'banan')
#
# a={343:'apple'}
# print(a[343])

# print ( ['최희찬',21,'사과','IBM',True] )
#
# print ( {'IBM':"quantumn",'Apple':257,'Amazon':False} )
#
# print(['최희찬',21,'사과','IBM',True][1] + {'IBM':"quantumn",'Apple':257,'Amazon':False}['Apple'])
# a={'IBM':"quantumn",'Apple':257,'Amazon':False}
# print(a.keys())



# a = ['최희찬','우지호',32, False]
#
# b= {'Apple':257, 'Amazon':False}
#
# a[3]= True
#
# c=a[0]
# a[0]=a[1]
# a[1]=c
#
# print(a)



gr = input('Enter ur grade')
grade = int(gr)
tier=''

if grade<0 or grade>100:
    tier='enter properly'
elif grade>90:
    tier='A'
elif grade>80:
    tier='B'
elif grade>70:
    tier="c"
else:
    tier='dumbass'

print(tier)
