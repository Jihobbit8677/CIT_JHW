grade = 135

if 90<=grade and grade<=100:
    print('A')
elif 80<=grade<90:
    print('B')
elif 70<=grade<80:
    print('C')
elif 0<=grade<70:
    print('F')
else:
    print('enter properly')

#희찬 썜 코드
grade = 135
tier = "" #empty string

if (grade > 100 or grade < 0):  #예외부터 날려 버리자!
    tier = "Wrong"
elif (grade > 90) :
    tier = "A"
elif (grade > 80) :
    tier = "B"
elif (grade > 70) :
    tier = "c"
else :
    tier = "F"

print(tier)


if(-3.342): #0아니면 True
    print("haha")

if("good"):
    print("hoho")

if(0):
    print("hehe")

if([]):
    print("hihi")

if({}):
    print("huhu")

if(""):
    print("hyhy")

if(" ") : #스페이스도 스트링 그 자체
    print("hewhew")
