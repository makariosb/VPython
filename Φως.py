from visual import *
scene1=display(title='Fws',
     x=0, y=0, width=800, height=800,
     center=(0,0,0), background=(0,0,0))
dt=0.01
def orbitaround(centre,pos,vel,dt,a):
    R=distanceto(centre,pos)
    ax=a*(centre.x-pos.x)/R
    ay=a*(centre.y-pos.y)/R
    az=a*(centre.z-pos.z)/R
    vel.x+=ax*dt
    vel.y+=ay*dt
    vel.z+=az*dt
    pos.x+=vel.x*dt
    pos.y+=vel.y*dt
    pos.z+=vel.z*dt
    return(pos,vel)
def distanceto(centre,pos):
    R=((pos.x-centre.x)**2+(pos.y-centre.y)**2+(pos.z-centre.z)**2)**0.5
    return R
box(size=(100,2,100))
asteri= sphere(pos=(-250,0,0),radius=35,color=color.yellow)
fws= local_light(pos=asteri.pos,color=color.yellow)
tetris=box(pos=(-20,9,30),size=(4,16,4), color=color.blue)
tetrislight=local_light(pos=tetris.pos, color=color.blue)
tetris2=box(pos=(20,9,30),size=(4,16,4), color=color.orange)
tetris2light=local_light(pos=tetris2.pos, color=tetris2.color)
u1=vector(300,380,-100)
nanos=sphere(pos=(0,0,-80),color=color.red)
allofws= local_light(pos=nanos.pos,radius=10,color=color.red)
a1=(abs(u1)**2)*1.0/(250)
u2=vector(0,200,0)
a2=(abs(u2)**2)*1.0/(80)
lampa= box(pos=(0,5,-10),size=(10,3,10), color=color.green)
lampafws=local_light(pos=lampa.pos, color=color.green)
while 1:
    rate(50)
    asteri.pos,u1=orbitaround(vector(0,0,0),asteri.pos,u1,dt,a1)
    fws.pos=asteri.pos
    nanos.pos,u2=orbitaround(vector(0,0,0),nanos.pos,u2,dt,a2)
    allofws.pos=nanos.pos
