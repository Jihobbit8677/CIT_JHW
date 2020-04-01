a = int( input("Enter:") )
# res = 1
#
# while a : #0 아니면 True
#     res = a * res
#     a-=1
#
# print(res)

def getFac1(num):
    res = 1
    while num : #0 아니면 True
        res = num * res
        num-=1
    return res

def getFac2(num):
    if num == 1:
        return 1
    else:
        return num * getFac2(num-1) #이것이 바로 recursion!!!

print (getFac1(a))
print (getFac2(a))
