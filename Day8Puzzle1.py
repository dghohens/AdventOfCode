"""--- Day 8: Memory Maneuver ---
The sleigh is much easier to pull than you'd expect for something its weight.
Unfortunately, neither you nor the Elves know which way the North Pole is from here.

You check your wrist device for anything that might help. It seems to have some kind of navigation system!
Activating the navigation system produces more bad news: "Failed to start navigation system.
ould not read software license file."

The navigation system's license file consists of a list of numbers (your puzzle input). The numbers define a
data structure which, when processed, produces some kind of tree that can be used to calculate the license number.

The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes
in the tree (or contains nodes that contain nodes, and so on).

Specifically, a node consists of:

A header, which is always exactly two numbers:
The quantity of child nodes.
The quantity of metadata entries.
Zero or more child nodes (as specified in the header).
One or more metadata entries (as specified in the header).
Each child node is itself a node that has its own header, child nodes, and metadata. For example:

2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----
In this example, each node of the tree is also marked with an underline starting with a letter
for easier identification. In it, there are four nodes:

A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
C, which has 1 child node (D) and 1 metadata entry (2).
D, which has 0 child nodes and 1 metadata entry (99).
The first check done on the license file is to simply add up all of the metadata entries. In this example,
that sum is 1+1+2+10+11+12+2+99=138.

What is the sum of all metadata entries?
"""

infile = open('input8.txt')
fcontent = [int(i) for i in infile.read().split()]
print(fcontent)

metadata_content = []

def subnodes(full_list):
    modlist = [i for i in full_list]
    metas = []
    while len(modlist) != 0:
        for i in range(0, len(modlist), 2):
            # If no subnodes within the node, remove the node and add its metadata to the metas list
            try:
                if modlist[i] == 0:
                    for j in range(1, modlist[i + 1] + 1):
                        metas.append(modlist[i + j + 1])
                    # Count subnodes down by one
                    modlist[i-2] -= 1
                    # Remove subnode
                    modlist = modlist[:i] + modlist[i + modlist[i+1] + 2:]
                    print(modlist)
                    print(metas)
                    break
            except IndexError:
                pass
    return metas


def metadata(meta_list):
    total = 0
    for i in meta_list:
        total += i
    return total


def main():
    metalist = subnodes(fcontent)
    print(metalist)
    metatotal = metadata(metalist)
    print(metatotal)
    pass

main()
