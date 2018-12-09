"""--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected.
Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous?
It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from
the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y
locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of
coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance,
each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend
forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations,
and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the
largest area is 17.

What is the size of the largest area that isn't infinite?
"""

from scipy.spatial import distance


infile = open('input6.txt')
fcontent = infile.read().split('\n')[:-1]
spatialdict = {}
print(fcontent)
points = [tuple([int(x) for x in i.split(',')]) for i in fcontent]
print(points)

'''Build a huge array of space, check each x,y location to determine what point is closest. Return the points,
along with how many locations on the array are closest.
Need to make the input a list of lists (with ints in the sublists) for scipy to work.
'''
for x in range(-500,1000):
    for y in range(-500,1000):
        closest_dist = 100000
        closest_point = []
        tie = False
        for i in points:
            spatialdict.setdefault(i,0)
            testdist = distance.cityblock([x,y],i)
            if testdist < closest_dist:
                closest_dist = testdist
                closest_point = i
            elif testdist == closest_dist:
                tie = True
                break
            if not tie:
                spatialdict[closest_point] += 1
    print(x)

print(spatialdict)
