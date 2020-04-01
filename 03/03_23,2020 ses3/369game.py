# Answers to the Challenges

# 369

limit = 200
num = 1

while num < limit :
    dividerEXP = 1
    chak = 0
    while num >  10 ** (dividerEXP-1) :
        verifier = (num % (10 ** dividerEXP)) - (num%10**(dividerEXP-1))
        if (verifier % 3 == 0 and verifier != 0 ):
            chak +=1
        dividerEXP +=1
    if (not chak):
        print(num)
    else :
        while (chak != 0):
            print("짝", end="")
            chak -= 1
        print("")

    num += 1


while num < limit:
    divider EXP = 1
    chak = 0
    while num > 10 ** (dividerEXP-1):


# sorting
# https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
