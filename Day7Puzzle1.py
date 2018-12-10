"""--- Day 7: The Sum of Its Parts ---
You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too
hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that
washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's
Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm;
take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see,
believe it or not, this box contains something that will solve all of Santa's transportation problems - at least,
that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language
it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more
parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin
(your puzzle input). Each step is designated by a single letter. For example, suppose you have the following
instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----
Your first goal is to determine the order in which the steps should be completed. If more than one step is ready,
choose the step which is first alphabetically. In this example, the steps would be completed as follows:

Only C is available, and so it is done first.
Next, both A and F are available. A is first alphabetically, so it is done next.
Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically
of the three.
After that, only D and F are available. E is not available because only some of its prerequisites are complete.
Therefore, D is completed next.
F is the only choice, so it is done next.
Finally, E is completed.
So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?
"""

infile = open('input7.txt')
fcontent = infile.read().split('\n')[:-1]
required_step = [i[5] for i in fcontent]
dependent_step = [i[36] for i in fcontent]
alphastring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
orderedsteps = []
possiblesteps = []


def remove_dependencies(list_of_steps, met_dependency):
    for i in list_of_steps:
        if i[5] == met_dependency:
            list_of_steps = poplist(list_of_steps, i)
    return list_of_steps


def poplist(list_to_pop, value_to_pop):
    try:
        print(list_to_pop)
        list_to_pop = list_to_pop.pop(list_to_pop.index(value_to_pop))
    except ValueError:
        pass
    return list_to_pop


def checkord(possiblelist):
    ordnum = 100
    nextstep = ''
    for i in possiblelist:
        if ord(i) < ordnum:
            ordnum = ord(i)
            nextstep = i
    return nextstep


# Populate possible steps, then add the lowest ordvalue to ordered steps
for z in fcontent:
    for j in fcontent:
        for i in alphastring:
            if i not in dependent_step and i not in orderedsteps and i not in possiblesteps:
                possiblesteps.append(i)
        newstep = checkord(possiblesteps)
        orderedsteps.append(newstep)
        possiblesteps = poplist(possiblesteps, newstep)
        fcontent = remove_dependencies(fcontent, newstep)
        required_step = [i[5] for i in fcontent]
        dependent_step = [i[36] for i in fcontent]
        if newstep == '':
            break
        #print(orderedsteps)
        #print(fcontent)
        #print(possiblesteps)
        #print(dependent_step)


'''
for z in range(len(fcontent)):
    foundstep = False
    for i in alphastring:
        if foundstep:
            break
        if i not in dependent_step:
            if i not in orderedsteps:
                orderedsteps.append(i)
                foundstep = True
                break
        for y in fcontent:
            if i in orderedsteps:
                break
            if y[36] == i and y[5] in orderedsteps:
                orderedsteps.append(i)
                foundstep = True
                break



for z in range(len(fcontent)):
    for i in alphastring:
        # Next, populate the list of possible steps
        if i in orderedsteps:
            indices = [i for i, x in enumerate(required_step) if x == i]
            for j in indices:
                possiblesteps.append(dependent_step[j])
        # Go through each possible step, add it to the ordered steps iff it's a lower ord value than everything else
        else:
            pass
'''
#print(orderedsteps)
#print(possiblesteps)
