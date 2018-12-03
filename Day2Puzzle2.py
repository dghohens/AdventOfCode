"""--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example,
given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij
and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing
character from either ID, producing fgij.)
"""

infile = open('input2.txt')
fcontent = infile.read().split('\n')

fcontent = fcontent[:-1]

for i in range(len(fcontent)):
    for j in range(i, len(fcontent)):
        diffchar = 0
        if fcontent[i] == fcontent[j]:
            pass
        else:
            for m in range(len(fcontent[i])):
                if diffchar > 1:
                    break
                elif fcontent[i][m] != fcontent[j][m]:
                    diffchar += 1
            if diffchar == 1:
                print(fcontent[i], fcontent[j])
