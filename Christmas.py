import turtle as t  #as就是取个别名，后续调用的t都是turtle
from turtle import *
import random as r
import time

screensize(bg='black')
t.color('green')
t.penup() #拿起画笔
t.setx(15)
t.sety(280)
t.pendown() #放下画笔
t.fillcolor('green')
t.begin_fill()
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

t.color('green')
t.penup() #拿起画笔
t.setx(11)
t.sety(220)
t.pendown() #放下画笔
t.fillcolor('green')
t.begin_fill()
t.left(120)
t.forward(150)
t.left(120)
t.forward(150)
t.left(120)
t.forward(150)
t.end_fill()

t.color('green')
t.penup() #拿起画笔
t.setx(11)
t.sety(160)
t.pendown() #放下画笔
t.fillcolor('green')
t.begin_fill()
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()
#树桩
t.color('brown')
t.penup()
t.setx(0)
t.sety(-11)
t.pendown()
t.fillcolor('brown')
t.begin_fill()
t.left(150)
t.fd(80)
t.left(90)
t.fd(30)
t.left(90)
t.fd(80)
t.end_fill()
t.penup()

#star
# t.color('yellow')
n=100.0
forward(3*n)
color("orange", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
t.setx(13.5)
t.sety(280)
t.pendown()
begin_fill()
left(126)

for i in range(5):  # 画五角星
    forward(n / 5)
    right(144)  # 五角星的角度
    forward(n / 5)
    left(72)  # 继续换角度
end_fill()
right(126)
speed('fastest')
def drawsnow():  # 定义画雪花的方法
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    for i in range(200):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penupﬁ
        t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360 / dens))  # 转动角度


drawsnow()  # 调用画雪花的方法
t.done()  # 完成,否则会直接关闭










