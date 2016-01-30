from visual import *
from random import *
scene1 = display(title='Balls',
     x=0, y=0, width=800, height=600,
     center=(0,3,0), background=color.black)
dt=0.01
spheres=[]
phase=[]
a=raw_input("how many spheres?")
while a==0 or not(a.isdigit()):
    a=raw_input("put a valid option...")
a=int(a)
for i in xrange(a):
    spheres.append(0)
    phase.append(0)
    spheres[-1]=sphere( pos=(0,-4,0), color=color.cyan)
    spheres[-1].v=vector(0,0,0)
box( pos=(0,-5,0), size=(200,0,200))
box( pos=(0,-4.9,0), size=(22,0,22), color=color.magenta)
arrow( pos=(7,0,0), axis=(1,0,0), color=color.blue)
arrow( pos=(7,0,0), axis=(0,1,0), color=color.green)
arrow( pos=(7,0,0), axis=(0,0,1), color=color.orange)
for i in xrange(-5,6):
    arrow( pos=(100,0,i*18), axis=(0,5,0), color=color.red)
    arrow( pos=(-100,0,i*18), axis=(0,5,0), color=color.red)
    arrow( pos=(i*18,0,100), axis=(0,5,0), color=color.red)
    arrow( pos=(i*18,0,-100), axis=(0,5,0), color=color.red)
arrow( pos=(90,15,0), axis=(-20,0,0), color=color.blue)
arrow( pos=(0,15,90), axis=(0,0,-20), color=color.blue)
arrow( pos=(-90,15,0), axis=(20,0,0), color=color.blue)
arrow( pos=(0,15,-90), axis=(0,0,20), color=color.blue)
arrow( pos=(90,15,90), axis=(-20,0,-20), color=color.blue)
arrow( pos=(-90,15,90), axis=(20,0,-20), color=color.blue)
arrow( pos=(90,15,-90), axis=(-20,0,20),  color=color.blue)
arrow( pos=(-90,15,-90), axis=(20,0,20), color=color.blue)
arrow( pos=(-5,20,-5), axis=(0,-5,0), color=color.green)
arrow( pos=(-5,20,5), axis=(0,-5,0), color=color.green)
arrow( pos=(5,20,-5), axis=(0,-5,0), color=color.green)
arrow( pos=(5,20,5), axis=(0,-5,0), color=color.green)




while 1:
    rate(200)
    for i in xrange(len(phase)):


        
        if phase[i]==0 or phase[i]==-1:
            spheres[i].v.y+=-5*dt
            spheres[i].x+=spheres[i].v.x*dt
            spheres[i].y+=spheres[i].v.y*dt
            spheres[i].z+=spheres[i].v.z*dt
            if abs(spheres[i].x)>100 or abs(spheres[i].z)>100:
                phase[i]=1


                
        elif phase[i]==1:
            spheres[i].v.y+=25*dt
            spheres[i].y+=spheres[i].v.y*dt
            if spheres[i].y>20:
                phase[i]=2
                spheres[i].v.y=0


                
        elif phase[i]==2:
            if abs(spheres[i].z)>10:
                spheres[i].z+=-spheres[i].z/abs(spheres[i].z)*6*dt
            if abs(spheres[i].x)>10:
                spheres[i].x+=-spheres[i].x/abs(spheres[i].x)*6*dt
            if not(abs(spheres[i].z)>10 or abs(spheres[i].x)>10):
                phase[i]=3



                
        else:
            spheres[i].v.y+=-5*dt
            spheres[i].y+=spheres[i].v.y*dt
            if spheres[i].y<-4:
                phase[i]=0

                
        if spheres[i].y<-4:
            spheres[i].v.y=-spheres[i].v.y
            spheres[i].y=-4
            if not(abs(spheres[i].z)>10 or abs(spheres[i].x)>10):
                spheres[i].v.y=randint(5,15)
                spheres[i].v.x=randint(-10,10)
                spheres[i].v.z=randint(-10,10)
                if spheres[i].v.x==0:
                    spheres[i].v.x=1
