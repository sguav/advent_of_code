import re
from operator import itemgetter

with open("day22/input", "r") as f:
    # Create list of lists with coordinates of bricks
    datalist = f.read().splitlines()
    # This will be the snapshot, as a 6-tuple of coordinates x0,y0,z0,x1,y1,z1
    snapshot = []
    for l in datalist:
        m = re.findall(r'\d+', l)
        # convert to int
        m = [int(d) for d in m]
        snapshot.append(m)

    # Sort the coordinates on the z0 axis, as that is the lowest a brick can be
    snapshot = sorted(snapshot, key=itemgetter(2))

    # 'profile' the volume of each brick
    # This makes it possible to see which bricks can fall
