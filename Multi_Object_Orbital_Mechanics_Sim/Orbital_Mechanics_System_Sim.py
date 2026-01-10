import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

bodiesx = []
bodiesy = []
bodiesz = []
bodystat = []

#Data intake
moondata = pd.read_csv('Multi_Object_Orbital_Mechanics_Sim/horizons_body_data.csv', delimiter = ',', on_bad_lines='skip')
rows, columns = moondata.shape

#Create lists with planet data and store them in a list with the same index as row number in CSV
for r in range(0, rows):
    templist = []
    for c in range(1, columns):
        appender = float(moondata.iloc[r, c])
        templist.append(appender)
    bodystat.append(templist)

#Store the initial positions of the bodies in lists that have the same index as row in larger list
for a in range(0, rows):
    bodiesx.append([float(moondata.iloc[a, 2])])
    bodiesy.append([float(moondata.iloc[a, 3])])
    bodiesz.append([float(moondata.iloc[a, 4])])

G = (6.67430 * (10 ** -11))

#plot settings
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5 * (10 ** 11), 5 * (10 ** 11))
ax.set_ylim(-5 * (10 ** 11), 5 * (10 ** 11))
ax.set_zlim(-5 * (10 ** 11), 5 * (10 ** 11))
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Multi-Object Orbital Mechanic Sim")

#iterations until saved data
i = 1200

#for each savedata
for t in range(0, int(1200000/i)):


    #for each second between savedata
    for s in range(0, i):

        #for each object
        for o in range(0, rows):
            mass = bodystat[o][0]
            vel = [bodystat[o][4], bodystat[o][5], bodystat[o][6]]
            pos = [bodystat[o][1], bodystat[o][2], bodystat[o][3]]
            accel = [0, 0 ,0]

            #calcluate the acceleration from every other object
            for o1 in range(0, rows):
                if o1 != o:
                    mass1 = bodystat[o1][0]
                    vel1 = [bodystat[o1][4], bodystat[o1][5], bodystat[o1][6]]
                    pos1 = [bodystat[o1][1], bodystat[o1][2], bodystat[o1][3]]
                    dist = np.sqrt(((pos[0] - pos1[0]) ** 2) + ((pos[1] - pos1[1]) ** 2) + ((pos[2] - pos1[2]) ** 2))
                    if dist != 0:
                        field = (-G * mass1) / (dist ** 3)
                        accel[0] = accel[0] + (field * (pos[0] - pos1[0]))
                        accel[1] = accel[1] + (field * (pos[1] - pos1[1]))
                        accel[2] = accel[2] + (field * (pos[2] - pos1[2]))
                    else:
                        pass
                else:
                    pass
            
            #calculate the new velocity and position for each object
            bodystat[o][4] = float(vel[0] + 500 * accel[0])
            bodystat[o][5] = float(vel[1] + 500 * accel[1])
            bodystat[o][6] = float(vel[2] + 500 * accel[2])

            bodystat[o][1] = float(pos[0] + 500 * bodystat[o][4])
            bodystat[o][2] = float(pos[1] + 500 * bodystat[o][5])
            bodystat[o][3] = float(pos[2] + 500 * bodystat[o][6])
    
    #savedata
    for m in range(0, rows):
        bodiesx[m].append(bodystat[m][1])
        bodiesy[m].append(bodystat[m][2])
        bodiesz[m].append(bodystat[m][3])

for p in range(0, rows):
    xlist = bodiesx[p]
    ylist = bodiesy[p]
    zlist = bodiesz[p]
    ax.plot(xlist, ylist, zlist, c = 'b', marker='.')

#show
plt.show()