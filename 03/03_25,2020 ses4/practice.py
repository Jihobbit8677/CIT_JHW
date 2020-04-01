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



# def fiboiter(num):
#     a1=1
#     a2=2
#     cnt=1
#     while num != cnt : #카운트 쌓아 나간다,while문으로 iterate하기
#         temp = second #변수 꽁쳐두기
#         second = second + first
#         first = temp
#         cnt += 1
#     return first



def fiboiter(num):
    first = 1
    second = 2
    cnt=1
    while num != cnt:
        tmp = first
        first = second
        second = second + tmp
        cnt+=1
    return second ###scope issue!
print(fiboiter(7))
