import sys
import math

try:
    velocity = float(sys.argv[1])
    print("Object Velocity is: " + str(velocity))
    angle = float(sys.argv[2])
    
    if angle >= 90:
        print("You're an idiot")
        print("RUN")
        sys.exit()    
    print("The angle of the object is: " + str(angle))
    # print("If angle is over 90 or below 0 simulation will likely crash")
    vertSpeed = (velocity * (math.sin(math.radians(angle))))
    horSpeed = velocity * (math.cos(math.radians(angle)))
    maxTime = vertSpeed/9.8*2
    timesASecond = 130/vertSpeed


    maxHeight = float((float(vertSpeed)/4.0)*maxTime)
    initialVertSpeed = vertSpeed
    horizontalPosition = 0
    verticalPosition = 0
    time = 0
    print("   Time   |   Horizontal   |   Height   |   Velocity   ")
    while (verticalPosition+0.1) > 0:
        time += (1/timesASecond)
        horizontalPosition += (horSpeed/timesASecond)
        verticalPosition = ((initialVertSpeed*time) + ((0.5)*(-9.8)*(time ** 2.0)))
        vertSpeed += (-(9.8/timesASecond))
        overallVelocity = math.sqrt((horSpeed ** 2) + (vertSpeed ** 2))
        print(str(round(time, 5)) +  "            " + str(round(horizontalPosition, 3)) + "         " + str(round(verticalPosition, 3)) + "      " + str(round(overallVelocity, 3)))
    print("The object went " + str(round((horSpeed*maxTime), 3)) + " meters forwards and " + str(round(maxHeight,3)) + " meters at highest over the course of " + str(round(maxTime,3)) + " seconds.")
except:
    print("Make sure to format comamand as pypy3 Projectile.py *velocity* *angle from ground* *How many times a second*")

