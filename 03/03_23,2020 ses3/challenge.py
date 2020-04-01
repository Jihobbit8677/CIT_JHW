#1~1만까지 소수 출력하는 코드

# cnt=1
# for i in range(2, n+1):
#     while cnt < n:
#         if cnt % i ==0:
#             print(cnt)
#         else:
#             cnt += 1



# for i in range(2, n+1):
#         if i==2:
#             print(2)#예외처리 먼저?
#         else:
#             for j in range(2,i):
#                 if i%j == 0:
#                     break
#                 else:
                     # print(i)
limit = 100
for i in range(2,limit+1):
    if (i == 2):
        print(i)
    else:
        for k in range(2,i):
            if(i%k == 0):
                break
            elif(k == i-1):
                print(i)


# for i in range(2,n+1):
#     if i == 2:
#         print(i)
#     else:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#             elif j==i-1:
#                 print(i)
#gg
#####해답
lower = 1
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num) #for,else사용



# for i in range(2,1001):
#     for j in range(2,i):
#         if i%j ==0:
#             print(j)


# number = 1000
# cnt = 0
#
# for i in range(2,number+1):
#     for k in range(2,number+1):
#         if i%k ==0:
#             break
#     if i==k:

# gg




##1,22,33,444~999999999~22,11출력하기###
n=10
for i in range(1,n):
    for x in range(i):
        print(i, end = "")

# for k in range(n-2,0,-1):
#     print(str(k)*k)
# #
# a = ['1','2','3','4','5','6','7','8','9','8','7','6','5','4','3','2','1']
# for i in a:
#     print(i*int(i))


#
#
# #1,2,3,4를 사용해서 만들 수 있는 모든 네자리 숫자 출력하기(중복허용)
# a=[1,2,3,4]
# for i in a:
#     for j in a:
#         for k in a:
#             for l in a:
#                 print(i,j,k,l)
#수형도 이미지! 시그마 중첩 이미지!


#369게임! 3,6,9가 들어가면 박수치기('짝') +@)3,6,9개수만큼 박수치기(367짝짝)
# def game369(i): #369 game안돼? 내장함수?
#     num = str(i)
#     if '3' or '6'or '9' in num:
#         print('짝')
#
# game369(23)
#구글링 한겨, 함수 쓸 생각을 아예 못 함. checker만드는 생각 자체를 못함 범위인줄
# def game369_upgrade(i):
#
# n=
# for i in range(2,n)

def game2_369(x):
    total = 0
    for i in str(x):
        if i in ['3','6','9']:
            total+=1
    res = total * '짝'
    print(res)
game2_369(369239)


a= input('Enter a number:')
for i in a: #int도 for문 가능
    cnt=0
    if i in ['3','6','9']:
        cnt+=1

        res = '짝'*cnt
        print(res)




#함수 안 쓰고 어떻게?



# n=
# print('짝' * n)


#숫자로만 구성된 임의의 리스트 오름순,내림순 정렬하기
# def order()
# a= [2,1,4,3]
# a.sort()
# print(a)
