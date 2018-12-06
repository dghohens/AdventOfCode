"""--- Part Two ---
Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total.
(In all other cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would
be 99 * 45 = 4455.)
"""

import re
from collections import Counter as counter

infile = open('input4.txt')
fcontent = infile.read().split('\n')
fcontent = sorted(fcontent[:-1])
date_regex = re.compile(r'-(\d\d-\d\d) ')
guard_regex = re.compile(r'Guard #(\d+) ')
sleep_regex = re.compile(r'00:(\d\d)] falls asleep')
wake_regex = re.compile(r'00:(\d\d)] wakes up')

date_dict = {}
guard_dict = {}

for i in range(len(fcontent)):
    if guard_regex.findall(fcontent[i]) != []:
        guard_match = guard_regex.findall(fcontent[i])[0]
        guard_dict.setdefault(guard_match, [])
        for j in range(1, 9):
            try:
                if guard_regex.findall(fcontent[i + j]) != []:
                    break
                if sleep_regex.findall(fcontent[i + j]) != []:
                    sleeptime = int(sleep_regex.findall(fcontent[i + j])[0])
                    waketime = int(wake_regex.findall(fcontent[i + j + 1])[0])
                    for k in range(sleeptime, waketime):
                        guard_dict[guard_match].append(k)
            except IndexError:
                pass

for i in guard_dict:
    print(i)
    print(counter(guard_dict[i]))
