"""--- Part Two ---
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should.
Your goal is to figure out which unit type is causing the most problems, remove all instances of it
(regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully
reacting the result?
"""

infile = open('input5.txt')
fcontent = infile.read()[:-1]


def reactor(polymer):
    check = True
    while check:
        startinglen = len(polymer)
        try:
            for i in range(len(polymer)+1):
                if polymer[i].lower() == polymer[i + 1].lower():
                    if polymer[i].isupper() and polymer[i + 1].islower():
                        polymer = polymer[0:i] + polymer[i+2:]
                    elif polymer[i].islower() and polymer[i + 1].isupper():
                        polymer = polymer[0:i] + polymer[i + 2:]
        except IndexError:
            pass
        if len(polymer) == startinglen:
            check = False
    return(polymer)


poly1 = reactor(fcontent)
print(len(poly1))
alpha_string='abcdefghijklmnopqrstuvwxyz'


for i in alpha_string:
    testpoly = poly1
    try:
        for j in range(len(testpoly)):
            if testpoly[j].lower() == i:
                if j == 0:
                    testpoly = testpoly[1:]
                else:
                    testpoly = testpoly[0:j] + testpoly[j + 1:]
    except IndexError:
        pass
    print(i, len(reactor(testpoly)))
