from random import *

print (random()) ## random real number between 0 and 1
 #사람이 5번 이길때까지 진행되는 가위바위보 프로그램 만들기

#
# num = random()
#
# machine_choice = ''
# if (0 <= num < 1/3):
#     machine_choice = 'paper'
# elif (1/3 <= num < 2/3):
#     machine_choice = 'rock'
# elif (2/3 <= num < 1):
#     machine_choice = 'scissors'
#
# mc = machine_choice


# a = input('Let\'s play rock,paper,scissors!\nEnter:')
cnt = 0
while (cnt < 5):

    a = input('Let\'s play rock,paper,scissors!\nEnter:')

    if (a == "rock"):
        a = 0
    elif ( a == "paper"):
        a = 1
    elif ( a== "scissors"):
        a = 2
    else :
        print ("wrong input, try again!")
        continue


    num = random()
    machine_choice = ''
    if (0 <= num < 1/3):
        machine_choice = 0
    elif (1/3 <= num < 2/3):
        machine_choice = 1
    elif (2/3 <= num < 1):
        machine_choice = 2
    mc = machine_choice

    if(a =='scissors' and mc =='paper' ):
        print('U WIN!')
        cnt+=1
    elif(a > mc):
        print('U WIN!')
        cnt+=1
    elif(a == mc):
        print('draw')
    else:
        pass


# 결과 양식
# 컴퓨터 : rock, 당신 : scissors, 결과 : 패배









# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
#몬드리안 그림 그려보기  square이용
