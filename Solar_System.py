#File Name:p06_0812242.py
#Author:孫瑋澤
#Email Address:kobe891207@gmail.com
#Assignment Number:06
#Description:The program will print draw a diagram of solar system
#Last Change:2020/5/24
#Anything Special:
#畫出全部的行星


import math
import turtle

class Sun:
    #one constructor
    def __init__(self,iname,irad,im,itemp):
        self.name=iname
        self.radius=irad
        self.mass=im
        self.temp=itemp
        self.x=0
        self.y=0
        
        self.sturtle=turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    #mutator function
    def setName(self,newname):
        self.name=newname

    #accessor functions
    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getTemperature(self):
        return self.temp

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getVolume(self):
        v=4/3*math.pi*self.radius**3
        return v

    def getSurfaceArea(self):
        sa=4*math.pi*self.radius**2
        return sa

    def getDensity(self):
        d=self.mass/self.getVolume()
        return d
        
    #special finctions
    def __str__(self):
        return self.name
    
#----------------------------------- 創太陽
class Planet:
    #one constructor
    def __init__(self,iname,irad,im,idist,ivx,ivy,ic):
        self.name=iname
        self.radius=irad
        self.mass=im
        self.distance=idist
        self.x=idist
        self.y=0
        self.color=ic
        self.velx=ivx
        self.vely=ivy

        self.pturtle=turtle.Turtle()
        self.pturtle.shape("circle")
        self.pturtle.color(self.color)

        self.pturtle.up()
        self.pturtle.goto(self.x,self.y)
        self.pturtle.down()

    #accessor functions
    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def getVolume(self):
        v=4/3*math.pi*self.radius**3
        return v

    def getSurfaceArea(self):
        sa=4*math.pi*self.radius**2
        return sa

    def getDensity(self):
        d=self.mass/self.getVolume()
        return d
    
    #mutator functions
    def setName(self,newname):
        self.name=newname

    def setXVel(self,newvx):
        self.velx=newvx

    def setYVel(self,newvy):
        self.vely=newvy
    
    #special finctions
    def __str__(self):
        return self.name

    def moveTo(self,newx,newy):
        self.x=newx
        self.y=newy
        self.pturtle.goto(newx,newy)

#--------------------------------------創行星
class Moon:
    def __init__(self,iname,irad,im,idist,ivx,ivy,ic):
        self.name=iname
        self.radius=irad
        self.mass=im
        self.distance=idist
        self.x=idist
        self.y=0
        self.color=ic
        self.velx=ivx
        self.vely=ivy

        self.pturtle=turtle.Turtle()
        self.pturtle.shape("circle")
        self.pturtle.color(self.color)

        self.pturtle.up()
        self.pturtle.goto(self.x,self.y)
        self.pturtle.down()

    #accessor functions
    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def getVolume(self):
        v=4/3*math.pi*self.radius**3
        return v

    def getSurfaceArea(self):
        sa=4*math.pi*self.radius**2
        return sa

    def getDensity(self):
        d=self.mass/self.getVolume()
        return d
    
    #mutator functions
    def setName(self,newname):
        self.name=newname

    def setXVel(self,newvx):
        self.velx=newvx

    def setYVel(self,newvy):
        self.vely=newvy
    
    #special finctions
    def __str__(self):
        return self.name

    def moveTo(self,newx,newy):
        self.x=newx
        self.y=newy
        self.pturtle.goto(newx,newy)

#-----------------------------------------創衛星
class SolarSystem:
    def __init__(self,width,height):
        self.thesun=None
        self.theearth=None
        self.planets=[]
        self.moons=[]
        self.ssturtle=turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen=turtle.Screen()
        self.ssscreen.setworldcoordinates(-2.5,-2.5,2.5,2.5)

    def addPlanet(self,aplanet):
        self.planets.append(aplanet)

    def addSun(self,asun):
        self.thesun=asun

    def addEarth(self,aearth):
        self.theearth=aearth

    def addMoon(self,amoon):
        self.moons.append(amoon)
        
    def showPlanet(self):
        for aplanet in self.planets:
            print(aplanet)

    def showMoon(self):
        for amoon in self.moon:
            print(moon)

    def movePlanets(self):
        G=.1
        dt=.012

        for p in self.planets: #動行星
            #perform moveTo
            p.moveTo(p.getXPos()+dt*p.getXVel(),p.getYPos()+dt*p.getYVel())

            #compute the new distance from planet to the sun
            rx=self.thesun.getXPos()-p.getXPos()
            ry=self.thesun.getYPos()-p.getYPos()
            r=math.sqrt(rx**2+ry**2)

            #compute the new acceleration components
            accx=G*self.thesun.getMass()*rx/r**3
            accy=G*self.thesun.getMass()*ry/r**3

            #compute the new velocity components
            p.setXVel(p.getXVel()+dt*accx)
            p.setYVel(p.getYVel()+dt*accy)

        for p in self.moons: #動衛星
            #perform moveTo
            p.pturtle.up()
            p.moveTo(self.thesun.getXPos()+p.getXPos()+dt*p.getXVel(),self.thesun.getYPos()+p.getYPos()+dt*p.getYVel())

            #compute the new distance from planet to the planet
            rx=self.theearth.getXPos()-p.getXPos()
            ry=self.theearth.getYPos()-p.getYPos()
            r=math.sqrt(rx**2+ry**2)

            #compute the new acceleration components
            accx=G*self.theearth.getMass()*rx/r**3 
            accy=G*self.theearth.getMass()*ry/r**3

            #compute the new velocity components
            p.setXVel(p.getXVel()+dt*accx)
            p.setYVel(p.getYVel()+dt*accy)

    def freeze(self):
        self.ssscreen.exitonclick()

#----------------------------------------創太陽系
def creatSSandAnimate():
    ss=SolarSystem(2,2)

    sun=Sun("SUN",5000,10,5800) #太陽
    ss.addSun(sun)

    p=Planet("MERCURY",19.5,1000,0.25,0,2,"sienna") #水星
    ss.addPlanet(p)

    p=Planet("VENUS",45,4800,0.3,0,2.1,"orange") #金星
    ss.addPlanet(p)

    p=Planet("EARTH",47.5,5000,0.35,0,2.0,"dodgerblue") #地球
    ss.addPlanet(p)

    p=Planet("MARS",50,9000,0.5,0,1.63,"red") #火星
    ss.addPlanet(p)

    p=Planet("JUPITER",100,49000,0.7,0,1.4,"peru") #木星
    ss.addPlanet(p)

    p=Planet("SATURN",75,16000,1.1,0,1.1,"sandybrown") #土星
    ss.addPlanet(p)

    p=Planet("URANUS",60,6,1.5,0,0.95,"lightskyblue") #天王星
    ss.addPlanet(p)
    ss.addEarth(p)

    p=Moon("MOON",16,1,1.7,0,2.4,"gold") #衛星
    ss.addMoon(p)

    p=Planet("NEPTUNE",55,6000,1.9,0,0.85,"cornflowerblue") #海王星
    ss.addPlanet(p)
    
    numTimePeriods=3000

    for amove in range(numTimePeriods):
        turtle.delay(0)
        ss.movePlanets()

    ss.freeze()

#----------------------------------------- 移動
creatSSandAnimate()



