from visual import *
from visual.graph import *
from math import *

scene=display(title='Maza se Elathrio me sin(x)',
     x=0, y=0, width=800, height=600,
     center=(0,2,0), background=color.black)

funct=gcurve(color=color.orange)

#STATHERES
k=100
m=10
A=10
w=sqrt(k/m)
t=0
dt=0.01

#ANTIKEIMENA
edafos=box(pos=(0,0,0), size=(3*A,0,5))
ball=sphere(pos=(0,1,0), radius=1, color=color.red)
koyti=box(pos=(-A-5,1,0), size=(2,2,5), color=color.yellow)
elatirio=helix(pos=koyti.pos, length=A+5, color=color.orange, coils=10)

while 1:
    rate(100)
    ball.x=A*sin(w*t)
    elatirio.length=A+5+ball.x
    funct.plot(pos=(t,ball.x))
    t+=dt
