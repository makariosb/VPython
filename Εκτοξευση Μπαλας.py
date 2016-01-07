from visual import *
from visual.graph import *
scene1 = display(title='Ripsh Mpalas',
     x=0, y=0, width=800, height=600,
     center=(0,3,0), background=color.black)
##funct=gcurve(color=color.orange)

#ANTIKEIMENA
edafos=box(pos=(0,0,0), length=100, height=0, width=6)
ball=sphere(pos=(0,1,0), radius=1, color=color.red, make_trail=true)
##Tvelos=arrow(pos=ball.pos, axis=(-3,0,0))
##Rvelos=arrow(pos=ball.pos-(0,0.5), axis=(-2,0,0))
##T=text(text='T',pos=(ball.pos.x-2,ball.pos.y+1,ball.pos.z))
##R=text(text='R',pos=(ball.pos.x-3,ball.pos.y-0.7,ball.pos.z), height=0.5)

#STATHERES
m=10
g=9.8
b=0.28
Ms=0.39
t=0
dt=0.01
I=vector(1,0,0)
ball.v=vector(20,0,0)

while True:
    rate(100)
    F=-b*ball.v-Ms*m*g*I
    a=F/m
    dv=a*dt
    ball.v=ball.v+dv
    dx=ball.v*dt
    ball.pos=ball.pos+dx
##    funct.plot(pos=(t,ball.v.x))
    t+=1
    if ball.v.x<=0:
        break
