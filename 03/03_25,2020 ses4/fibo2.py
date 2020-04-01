 a = int(input('Enter n: '))


def fibo(num):
    if num==1: #예외부터 날린다!
        return 1
    elif num==2:
        return 2
    else:
        res = fibo(num-1) + fibo(num-2)
        return res

# print (fibo(a) )


def fiboiter(num) :
    first = 1
    second = 2
    cnt = 1
    while num != cnt : #카운트 쌓아 나간다,while문으로 iterate하기
        temp = second #변수 꽁쳐두기 b/c second는 덮어 씌어질꺼니까
        second = second + first
        first = temp
        cnt += 1
    return first

print (fiboiter(a))
