import re

R_CUBES = 12
G_CUBES = 13
B_CUBES = 14

total = 0
power = 0

with open("day2/input") as f:
    for l in f:
        l = l.strip()
        # print(l)
        m = re.match("Game (\d+)", l)
        if m is not None:
            gameid = int(m.group(1))
            # print(gameid)
        else:
            raise Exception(f"The fuck has happened?\nLine: {l[0]}\n Match: {m}")

        l = l.split(":")
        sets = l[1].split(";")
        # print(sets)


        # Define max extracted number for each game
        maxgreen = 0
        maxblue = 0
        maxred = 0

        for s in sets:
            m = re.search("(\d+) blue", s)
            if m is not None:
                if int(m.group(1)) > maxblue:
                    maxblue = int(m.group(1))
            m = re.search("(\d+) green", s)
            if m is not None:
                if int(m.group(1)) > maxgreen:
                    maxgreen = int(m.group(1))
            m = re.search("(\d+) red", s)
            if m is not None:
                if int(m.group(1)) > maxred:
                    maxred = int(m.group(1))

        # print(maxblue)
        # print(maxgreen)
        # print(maxred)
        power += maxblue * maxgreen * maxred

        if (maxblue <= B_CUBES) and (maxgreen <= G_CUBES) and (maxred <= R_CUBES):
            total += gameid

print(f"Total: {total}")
print(f"PowerSum: {power}")
