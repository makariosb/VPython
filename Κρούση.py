from visual import *
scene=display(title='Kroush',
     x=0, y=0, width=800, height=800,
     center=(0,2,0), background=color.black)
ball1=sphere(pos=vector(-25,0,0),radius=1,color=color.green)
ball2=sphere(pos=vector(25,0,0),radius=1,color=color.red)
dt=0.001
v1,v2,m1,m2=input("v1,v2,m1,m2: ")
while 1:
    rate(1000)
    if abs(ball1.pos.x-ball2.pos.x)<=2:
        v3=(1.*(m1-m2)/(m1+m2))*v1+((2.*m2)/(m1+m2))*v2
        v4=(1.*(m2-m1)/(m1+m2))*v2+((2.*m1)/(m1+m2))*v1
        v1=v3
        v2=v4
        print v1,v2
    ball1.x=ball1.x+v1*dt
    ball2.x=ball2.x+v2*dt
