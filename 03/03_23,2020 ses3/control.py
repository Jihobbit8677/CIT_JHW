# cnt = 5
#
# while cnt > 0 :
#     print(cnt)
#     cnt = cnt - 1
#
# print("launch!") #ctrl+c 루프 강제종료

# for cnt in [5,4,3,2,1]:
#     print(cnt)
#
# print("launch!")

cnt=0
divider = 7
limit = 10000

while cnt<= limit:
    cnt += divider
    if (cnt <limit):
        print(cnt)

cnt = 0#cnt초기화

while cnt<= limit :
    if(cnt % divider == 0):
        print(cnt)
    cnt += 1 #더 많은 프로세스를 실행, 허나 더 간단한 프로세스? 더 빠르다!
