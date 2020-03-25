fibo1=1
fibo2=2
limit=10000
cnt=fibo1+fibo2

while cnt <limit:

    fibo1=fibo2
    fibo2=cnt
    cnt=fibo1+fibo2
    print(cnt)
