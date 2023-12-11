import sys
import math

try:
    velocity = int(sys.argv[1])
    print("Object Velocity is: " + str(velocity))
    angle = int(sys.argv[2])
    print("The angle of the object is: " + str(angle))
    # print("If angle is over 90 or below 0 simulation will likely crash")
    vertSpeed = (velocity * (math.sin(math.radians(angle))))
    horSpeed = velocity * (math.cos(math.radians(angle)))
    initialVertSpeed = vertSpeed
    horizontalPosition = 0.0000001
    verticalPosition = 0.0000001
    time = 0
    maxHeight = 0
    while verticalPosition > 0:
        time += 0.01
        horizontalPosition += (horSpeed/100)
        verticalPosition += (vertSpeed/100)
        vertSpeed += (-(9.8/100))
        if verticalPosition > maxHeight:
            maxHeight = verticalPosition
    print("The object went " + str(round(horizontalPosition, 3)) + " meters forwards and " + str(round(maxHeight,3)) + " meters at highest over the course of " + str(round(time,3)) + " seconds.")
except:
    print("Make sure to format comamand as pypy3 Projectile.py *velocity* *angle from ground*")

