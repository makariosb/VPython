from visual import *
dt=0.0016
def stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,a):
    head.pos= mb.pos + vector(0,mb.length/2.,0)
    rlt.pos= mb.pos + vector(0.1,-mb.length/2.,0)
    llt.pos= mb.pos + vector(-0.1,-mb.length/2.,0)
    rlb.pos= rlt.pos + rlt.axis
    llb.pos= llt.pos + llt.axis
    rat.pos= mb.pos
    lat.pos= mb.pos
    rab.pos= rat.pos + rat.axis
    lab.pos= lat.pos + lat.axis
    cracks[0].pos= rlb.pos
    cracks[1].pos= llb.pos
    cracks[2].pos= rab.pos
    cracks[3].pos= lab.pos
    cracks[4].pos= rlt.pos
    cracks[5].pos= llt.pos
    if a:
        rlt.length= 1.16**0.5
        rlb.length= 1.5
        llt.length= rlt.length
        llb.length= 1.5
        rat.length= 2.21**0.5
        rab.length= 1
        lat.length= rat.length
        lab.length= 1
    return(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks)
############################################################
for i in xrange(-50,51,10):
    for j in xrange(-50,51,10):                                                     #makes platform
        if (i/10+j/10)%2==1:
            box(pos=(i/2,-0.5,j),size=(5,0.5,10),color=color.red)
        else:
            box( pos=(i/2,-0.5,j) , size=(5,0.5,10) , color=color.blue )


            
arrow( pos=(7,0,0) , axis=(1,0,0) , color=color.blue , opacity=0.5 )
arrow( pos=(7,0,0) , axis=(0,1,0) , color=color.green , opacity=0.5)
arrow( pos=(7,0,0) , axis=(0,0,1) , color=color.orange , opacity=0.5)
mb=box( pos=(0,-1,0) , width=0.5 , length=2.2 , height=0.5 , axis=(0,1,0))  #mb: Main Body
head=sphere( pos=(mb.x,mb.y+mb.length/2.,mb.z) , radius=0.6)                                                #makes stickman
rlt=cylinder( pos=mb.pos+vector(0.1,-mb.length/2.,0) , axis=(0.4,-1,0), radius=0.25) #right leg top
rlb=cylinder( pos=rlt.pos+rlt.axis, axis=(0,-1.5,0) , radius=0.25)                   #right leg bot
llt=cylinder( pos=mb.pos+vector(-0.1,-mb.length/2.,0) , axis=(-0.4,-1,0), radius=0.25)#left leg top
llb=cylinder( pos=llt.pos+llt.axis , axis=(0,-1.5,0) , radius=0.25)                   #left leg bot
rat=cylinder( pos=mb.pos, axis=(1,-1.1,0), radius=0.25 , length=1.5)             #right arm top, and so on...
rab=cylinder( pos=rat.pos+rat.axis , radius=0.25 , axis=(0,-1,0))
lat=cylinder( pos=mb.pos , axis=(-1,-1.1,0), radius=0.25 , length=1.5)
lab=cylinder( pos=lat.pos+lat.axis , radius=0.25 , axis=(0,-1,0))
cracks=[]
for i in xrange(6):
    cracks.append(0)
    cracks[i]=sphere(radius=0.25)
cracks[0].pos=rlb.pos
cracks[1].pos=llb.pos
cracks[2].pos=rab.pos
cracks[3].pos=lab.pos
cracks[4].pos=rlt.pos
cracks[5].pos=llt.pos
#rlt=box(pos=(mb.x+0.5/2**0.5,mb.y-mb.length/2.-0.5/2**0.5,mb.z),width=0.5,length=1,height=0.5,axis=(1,-1,0))
#rlb=box(pos=(mb.x+1./2**0.5,mb.y-mb.length/2.-1./2**0.5-0.75,mb.z),width=0.5,length=1.5,height=0.5,axis=(0,-1,0))
#llt=box(pos=(mb.x-0.5/2**0.5,mb.y-mb.length/2.-0.5/2**0.5,mb.z),width=0.5,length=1,height=0.5,axis=(1,1,0))
#llb=box(pos=(mb.x-1./2**0.5,mb.y-mb.length/2.-1./2**0.5-0.75,mb.z),width=0.5,length=1.5,height=0.5,axis=(0,-1,0))
#rat=box(pos=(mb.x+0.75/1.25**0.5,mb.y,mb.z),width=0.5,length=1.5,height=0.5,axis=(1,-0.5,0))
#rab=box(pos=(mb.x+1.5/1.25**0.5,mb.y-0.375/1.25**0.5-0.5,mb.z),width=0.5,length=1,height=0.5,axis=(0,-1,0))
#lat=box(pos=(mb.x-0.75/1.25**0.5,mb.y,mb.z),width=0.5,length=1.5,height=0.5,axis=(-1,-0.5,0))
#lab=box(pos=(mb.x-1.5/1.25**0.5,mb.y-0.375/1.25**0.5-0.5,mb.z),width=0.5,length=1,height=0.5,axis=(0,-1,0))


phase=0
while rlb.y+rlb.axis.y<=0 or llb.y+llb.axis.y<=0:
    mb.y+=dt
    head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks= stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,0)
while 1:
    rate(1000)
    while rlb.y+rlb.axis.y<=0 or llb.y+llb.axis.y<=0:
        mb.y+=dt
        head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks= stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,0)
    while rlb.y+rlb.axis.y>0.0005 and llb.y+llb.axis.y>0.0005:
        mb.y+=-dt
        head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks= stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,0)
    if phase==0:
        first=llb.z+llb.axis.z
        rorl=0
        rlt.axis.z+=dt
        llt.axis.z+=-dt/5.
        llb.axis.z+=-dt/5.
        if cracks[0].y>rlt.y-rlt.length/2.:
            phase=1
    elif phase==1:
        first=llb.z+llb.axis.z
        rorl=0
        rlt.axis.z+=-dt/3.
        rlb.axis.z+=dt/2.
        llt.axis.z+=-dt/5.
        llb.axis.z+=-dt/5.4
        if rlb.axis.z>rlt.axis.z-0.1:
            phase=2
    elif phase==2:
        first=rlb.z+rlb.axis.z
        rorl=1
        rlt.axis.z+=-dt/2.1
        rlb.axis.z+=-dt/2.3
        llt.axis.z+=dt
        llb.axis.z+=-1.3*dt
        if cracks[1].y>llt.y-llb.length/2.:
            phase=3
    elif phase==3:
        first=rlb.z+rlb.axis.z
        rorl=1
        rlt.axis.z+=-dt/1.3
        rlb.axis.z+=-dt
        llb.axis.z+=3*dt
        if llb.axis.z>0.3:
            rlt.axis.z=rlb.axis.z
            phase=4
    else:
        first=llb.z+llb.axis.z
        rorl=0
        rlt.axis.z+=1.2*dt
        if rlb.axis.z<0:
            rlb.axis.z+=dt/2.
        if llt.axis.z>-0.2601643:
            llt.axis.z+=-dt/1.4
        if llb.axis.z>-0.2601643:
            llb.axis.z+=-dt/1.7
        if cracks[0].y>rlt.y-rlt.length/2.:
            llt.axis.z=-0.260164334706
            llb.axis.z=-0.260164334706
            rlb.axis.z=0
            phase=1
    head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks= stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,1)
    mb.z+=(first-(1-rorl)*(llb.z+llb.axis.z)-rorl*(rlb.z+rlb.axis.z))
    head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks= stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,1)
    if mb.z>45:
        mb.z=-45
        head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks= stable(head,rlt,rlb,llt,llb,rat,rab,lat,lab,cracks,mb,1)
