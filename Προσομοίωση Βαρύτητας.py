from visual import *
from random import *
from math import pi
def distanceto(pos1,pos2,r1,r2):
    R= ((pos1.x-pos2.x)**2+(pos1.y-pos2.y)**2+(pos1.z-pos2.z)**2)**0.5
    if R<r1+r2:
        R=100.
    return R

#########################
spheres=[]
spheres_va=[]
G=raw_input("how many spheres?")
while G==0 or G==1 or not(G.isdigit()):
    G=raw_input("put a valid option...")
G=int(G)-1


d=raw_input("trail?")
while d<>"yes" and d<>"no":
    d=raw_input("yes or no?")
if d=="yes":
    d=1
else:
    d=0

    
for i in xrange(G):
    
    spheres.append(0)
    dt=5*random()
    while dt<0.4:
        dt=5*random()
    dt=float(str(dt)[0:4])
    spheres[i]=sphere( pos=(randint(-30,30),randint(-30,30),randint(-30,30)) , radius=dt , color=(random(),random(),random()) , make_trail=d , retain=300 )
    spheres_va.append([])
    
spheres.append(0)
spheres[-1]=sphere( pos=(0,0,0) , radius=7 , color=(random(),random(),random()) )
spheres_va.append([])
dt=0.02
G=0.06

for i in xrange(len(spheres)):
    spheres_va[i].append(vector(0,0,0)) #j=0: velocity
    spheres_va[i].append(vector(0,0,0)) #j=1: acceleration



while 1:
    rate(150)
    for i in xrange(len(spheres)):
        for j in xrange(len(spheres)):
            if i<>j:

                d=860/spheres[j].radius**2.
                V=pi*4*spheres[j].radius**3/3
                mass=d*V
                R= distanceto( spheres[i].pos , spheres[j].pos , spheres[i].radius , spheres[j].radius )
                a= G*mass/R**2
                spheres_va[i][1]= a*(spheres[j].pos-spheres[i].pos)/R
                spheres_va[i][0]+= spheres_va[i][1]*dt

                
        spheres[i].pos+= spheres_va[i][0]*dt
   # scene.forward=spheres[-1].pos
