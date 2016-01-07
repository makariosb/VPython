from visual import *
from visual.graph import *
scene1 = display(title='Maza se Elathrio',
     x=0, y=0, width=800, height=600,
     center=(0,3,0), background=color.black)
funct=gcurve(color=color.orange)

#ANTIKEIMENA
edafos=box(pos=(0,0,0), length=20, height=0, width=6)
ball=sphere(pos=(0,1,0), radius=1, color=color.red, make_trail=true)
elatirio=helix(pos=(-10,1,0), axis=(ball.y,0,0),coils=10, radius=1, length=10,color=color.yellow)
kouti=box(pos=(-11,1,0), size=(2,2,6), color=color.blue)
#STATHERES
m=10
k=100
t=0
dt=0.01
ball.v=vector(20,0,0)

while True:
    rate(100)
    F=-k*ball.pos
    a=F/m
    dv=a.x*dt
    ball.v.x=ball.v.x+dv
    dx=ball.v.x*dt
    ball.x=ball.x+dx
#    funct.plot(pos=(t,ball.v.x))
    elatirio.length=10+ball.x
    t+=1
    
#Makarios Christakis 2015-2016
