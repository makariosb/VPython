from visual import *
from math import *
def apostasi(pos1,pos2):
    R= ((pos1.x-pos2.x)**2+(pos1.z-pos2.z)**2)**0.5
    return R
rt=input("rate?")
abc=input("how many spheres on the side?")
A=1.4
l=13
w=1.5
t=0.0
dt=1./rt
k=2.*pi/l
spheres=[]
for i in xrange(-abc,abc+1):
    spheres.append([])
    for j in xrange(-abc,abc+1):
        spheres[i+abc].append(0)
        spheres[i+abc][j+abc]=sphere(pos=(i*2,0,j*2), color=color.cyan)
while 1:
    rate(rt)
    for i in xrange(-abc,abc+1):
        for j in xrange(-abc,abc+1):
            r=apostasi(spheres[i][j].pos,vector(0,0,0))
            if w*t-k*r>0:
                spheres[i][j].y=A*sin(w*t-k*r)
            else:
                spheres[i][j].y=0
    t+=dt
