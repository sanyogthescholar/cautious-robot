import math
from sys import exit as exit_
ghosts = [[1,0],[0,3]]
target = [0,1]

g_distances = []
for g in ghosts:
    g_distances.append(math.dist(g,target))

pac_man_distance = math.dist([0,0], target)
for i in g_distances:
    if i>=pac_man_distance:
        print("Pac-Man cannot escape!")
        exit_(0)
print("Pac-Man has escaped!")