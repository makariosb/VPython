from visual import *
from math import *
scene1 = display(title='Volh',
     x=0, y=0, width=1000, height=1000,
     center=(0,3,0), background=color.black)
rt=input("rt?: ")
d1=False
d2=False
d3=False
d4=False
dt=1./rt
arrow(pos=(7,0,0),axis=(1,0,0),color=color.blue)
arrow(pos=(7,0,0),axis=(0,1,0),color=color.green)
arrow(pos=(7,0,0),axis=(0,0,1),color=color.orange)
answer=raw_input("Do you want to throw the ball without the formula?(y or n): ")
if answer=="y":
    d1=True
    ball1=sphere(pos=(0,0,0), color=color.white, make_trail=True)
answer=raw_input("Do you want to use the formula?(y or n): ")
if answer=="y":
    d2=True
    ball2=sphere(pos=(0,0,0), color=color.red, make_trail=True)
answer2=raw_input("How about adding air friction? Do you want to throw the ball without the formula?(y or n): ")
if answer2=="y":
    d3=True
    ball3=sphere(pos=(0,0,0), color=color.yellow, make_trail=True)
answer2=raw_input("How about adding air friction? Do you want to to use the formula?(y or n): ")
if answer2=="y":
    d4=True
    ball4=sphere(pos=(0,0,0), color=color.blue, make_trail=True)
if d3==True or d4==True:
    k=1.3
    m=input("Write mass")
if d1==True or d2==True or d3==True or d4==True:
    V=input("Write velocity: ")
    f=input("Write in degrees: ")
Vy=V*sin(f*pi/180.)
Vx=V*cos(f*pi/180.)
Vy1,Vy2,Vy3,Vy4=Vy,Vy,Vy,Vy
Vx1,Vx2,Vx3,Vx4=Vx,Vx,Vx,Vx
t=0.0
g=9.81
Vc=m*g/k*1.
while 1:
    rate(rt)
    if d1 and ball1.y>=0:
        Vy1+=-g*dt
        ball1.pos+=vector(Vx1, Vy1, 0)*dt
    if d2 and ball2.y>=0:
        ball2.pos=vector(Vx2*t, Vy2*t-g/2*t**2, 0)
    if d3 and ball3.y>=0:
        ax=-1.*k*Vx3/m
        ay=-1.*k*Vy3/m-g
        Vx3+=ax*dt
        Vy3+=ay*dt
        ball3.pos+=vector(Vx3, Vy3, 0)*dt
    if d4 and ball4.y>=0:
        x4=(1-e**(-k/m*t))*m/k*Vx4
        y4=-Vc*t+m/k*(Vy4+Vc)*(1-e**(-k/m*t))
        ball4.pos=vector(x4, y4, 0)
    t+=dt
