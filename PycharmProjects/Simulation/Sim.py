import turtle as tur
import math

V = float(input("초기 속도를 입력하세요:"))
Theta = float(input("발사 각도를 입력하세요:"))

t = 0
g = 9.8
sin = math.sin(math.radians(Theta))
cos = math.cos(math.radians(Theta))

tur.shape("circle")
while True:
    t += 1
    x = V*cos*t
    y = V*sin*t - g*t**2/2
    tur.goto(x, y)





