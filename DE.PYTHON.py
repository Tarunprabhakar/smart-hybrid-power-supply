#A---->Solar pannel sensor
#B----->Battery low threshold sensor
#C----->Battery high threshold sensor
#D----->Windturbine sensor 
#L----->main power 
#M----->pannel power
#N----->wind power
#O----->Charging or not 
import random
import math
from datetime import datetime


#solar pannel sensor
#this function calculates sunlight intensity in that day gives output as 0 and 1
def solarsensor():
    nd = datetime.now().timetuple().tm_yday 
    s=math.sin(360*(nd-94))/365
    I=1-0.0335*s
    print("sun intensity:",I)
    if(I>1):
        I=1
    else:
        I=0
    return I    
#watttime=watthour/current
#battery sensor gives output for higer threshold and lower threshold of battery is met or not 
def batterysensor(wh,b):
    n=(90*wh)/100
    t=(10*wh)/100
    if(b>=n and b>t):
        b=1
        c=1
    elif(b<n and b>t):
        b=1
        c=0
    elif(b<n and b<=t):
        b=0
        c=0
    return b,c
x=int(input("enter watthour of battery"))
z=int(input("enter watt remaining in battery"))
k=batterysensor(x,z)
def windmill(q):
    if(q>15):
        g=1
    else:
        g=0
    return g
w=int(input("enter wind speed in km/h"))       
v=windmill(w) 
def de(a,b,c,d):
    anot=not a
    bnot=not b
    cnot=not c
    dnot=not d
    x=(anot&cnot&dnot)&1
    y=(a&(b|c))
    z=d&(bnot&cnot|b&(anot|c))
    z1=cnot&1
    return x,y,z,z1
l=solarsensor()
m=k[0]
n=k[1]
o=v
t=de(l,m,n,o)
print(t)
if(t[0]==1):
    print("The house is running in POWER GRID")
if(t[1]==1):
    print("The house is running in SOLAR PANNEL")
if(t[2]==1):
    print("The house is ruuning in WIND POWER")
if(t[3]==1):
    print("The battery is being CHARGED")
if(t[1]==1 and t[2]==1 and t[3]==0 and t[0]==0):
    print("You can use battery")  
if(t[0]==0):
    print("The main grid is off")
if(t[1]==0):
    print("There is not enough sunlight to run the house in solar power")
if(t[2]==0):
    print("The wind speed is very low to run the house in wind power")
if(t[3]==0):
    print("The battery is charged and ready to use ")                








