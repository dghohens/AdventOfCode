"""--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any
other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
"""

import re

infile = open('input3.txt')
infile2 = open('claimconflicts.txt')
fcontent = infile.read().split('\n')
fcontent = fcontent[:-1]
claim_content = infile2.read().split('\n')
claim_content = claim_content[:-1]
claim_regex = re.compile(r'^#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)')

for i in fcontent:
    inmatch = claim_regex.findall(i)
    inmatch = inmatch[0]
    match = [int(a) for a in inmatch]
    nomatch = True
    for x in range(match[2]):
        if nomatch == False:
            break
        for y in range(match[3]):
            claim = str([match[0] + x, match[1] + y])
            if claim in claim_content:
                nomatch = False
                print(i)
                break
    if nomatch == True:
        print('Uncontested claim: ', i)
        break