from turtle import * #앞으로 쓰는 함수는 터틀에서 가져온거야~

# for i in range(4):
#     forward(100)
#     left(90)
turtle.pos()
(440.00,-0.00)
#
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

# speed(1)
# for i in range(500): # this "for" loop will repeat these functions 500 times
#     forward(i)
#     left(91)
#
# done()

# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md
#몬드리안 그림 그려보기  square이용
