# def count(x):
#     for i in x:
#         print(i)
#
# count('string')

# a = int(input('Enter a number:'))
# res=1
# while a:
#     res = a * res
#     a-=1
#
# print(res)



# def getFac1(num):
#     while num:
#         # res=1 #초항 while문 밖에 적어줘야지 리셋 안된다!
#         res = num * res
#         num-=1
#         return res
#
#
#
# def getFac1(num):
#     res = 1
#     while num : #0 아니면 True
#         res = num * res
#         num-=1
#     return res
#
# print(getFac1(5))
#
# def getFac2(num):
#     tmp = num * getFac1(num-1)
#     return tmp
#
# print(getFac2(6))



def fibo(num):
    if num == 1:
        return 1 #예외부터 날리고 시작한다!
    elif num==2:
        return 2
    else:
        res = fibo(num-1) + fibo(num-2)
        return res

print(fibo(7))
