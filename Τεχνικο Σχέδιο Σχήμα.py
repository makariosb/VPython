from visual import *
scene1=display(title='Sxima',
     x=0, y=0, width=800, height=800,
     center=(0,50,0), background=(0,0,0))

circle=shapes.circle(radius=25)
square=shapes.rectangle(width=40,height=8,pos=(0,21))
extrusion(pos=[(-34,80,0),(-45,80,0)],shape=circle-square)
extrusion(pos=[(34,80,0),(45,80,0)],shape=circle-square)

cylinder(pos=(35,80,0),axis=(-10,0,0),radius=25)
cylinder(pos=(-35,80,0),axis=(10,0,0),radius=25)

c1=shapes.rectangle(width=10,height=50,pos=(20,0))
c2=shapes.rectangle(width=10,height=50,pos=(-20,0))
c3=shapes.rectangle(width=50,height=15,pos=(0,-19))
extrusion(pos=[(-35,80,0),(35,80,0)],shape=circle-c1-c2-c3)#60

box(pos=(0,8.5,0),size=(50,17,70))
box(pos=(17,23,0),size=(16,12,70))
box(pos=(-17,23,0),size=(16,12,70))
box(pos=(17,16.5+29,0),size=(16,33,30))
box(pos=(-17,16.5+29,0),size=(16,33,30))
box(pos=(0,67,0),size=(50,10,30))

while 1:
    rate(1)
