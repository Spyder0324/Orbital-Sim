import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Object:
    def __init__(self, mass, vx, vy, vz, posx, posy, posz):
        self.mass = mass
        self.velocity = [vx, vy, vz]
        self.pos = [posx, posy, posz]

    def distance(self, object):
        return np.sqrt(((self.pos[0] - object.pos[0]) ** 2) + ((self.pos[1] - object.pos[1]) ** 2) + ((self.pos[2] - object.pos[2]) ** 2))
    
    def relpos(self, object):
        return [self.pos[0] - object.pos[0], self.pos[1] - object.pos[1], self.pos[2] - object.pos[2]]
    
    def force(self, object, dist, rpos, const):
        if dist != 0:
            accelfield = (-const * object.mass * self.mass) / (dist ** 3)
            return [(accelfield * rpos[0]), (accelfield * rpos[1]), (accelfield * rpos[2])]
        elif dist == 0:
            return [0, 0, 0]
        
    def accel(self, force):
        return [force[0]/self.mass, force[1]/self.mass, force[2]/self.mass]

#Starting Data
Earth = Object((5.9722 * (10 ** 24)), 0, 0, 0, 0, 0, 0)
Moon = Object((7.347 * (10 ** 22)), -6.813463842041659 * (10 ** 1), -9.946635131185040 * (10 ** 2), -8.589252557038984 * (10 ** 1), -3.911992852612219 * (10 ** 8), 2.905795690898377 * (10 ** 6), -1.179630558323180 * (10 ** 7))
#distance = 356650000
G = (6.67430 * (10 ** -11))

#iterations til save
i = 2048

MEDist = Moon.distance(Earth)
MErpos = Moon.relpos(Earth)
MEForce = Moon.force(Earth, MEDist, MErpos, G)
MEAccel = Moon.accel(MEForce)

xlist = [Earth.pos[0], Moon.pos[0]]
ylist = [Earth.pos[1], Moon.pos[1]]
zlist = [Earth.pos[2], Moon.pos[2]]

for s in range(0, int(2400000/i)):
    for s in range(0, i):
        Moon.velocity[0] = Moon.velocity[0] + (MEAccel[0])
        Moon.velocity[1] = Moon.velocity[1] + (MEAccel[1])
        Moon.velocity[2] = Moon.velocity[2] + (MEAccel[2])

        Moon.pos[0] = Moon.pos[0] + (Moon.velocity[0])
        Moon.pos[1] = Moon.pos[1] + (Moon.velocity[1])
        Moon.pos[2] = Moon.pos[2] + (Moon.velocity[2])

        MEDist = Moon.distance(Earth)
        MErpos = Moon.relpos(Earth)
        MEForce = Moon.force(Earth, MEDist, MErpos, G)
        MEAccel = Moon.accel(MEForce)

    xlist.append(Moon.pos[0])
    ylist.append(Moon.pos[1])
    zlist.append(Moon.pos[2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5.8 * (10 ** 8), 5.8 * (10 ** 8))
ax.set_ylim(-5.8 * (10 ** 8), 5.8 * (10 ** 8))
ax.set_zlim(-5.8 * (10 ** 8), 5.8 * (10 ** 8))
ax.set_box_aspect([1, 1, 1])
ax.plot(xlist, ylist, zlist, c = 'b', marker='o')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Basic Orbital Mechanic Sim")
plt.show()