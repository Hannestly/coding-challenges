'''
Given a list of possibly overlapping intervals, return a new list of
intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''


def reduce(inputlist):
    reducedlist = []
    for i in inputlist:

        if bool(reducedlist) == False:
            reducedlist.append(i)
        else:

            x1, x2 = i
            size = len(reducedlist)
            for e in range(size):
                y1, y2 = reducedlist[e]

                if x1 > y1 and x1 < y2 and x2 > y2:
                    reducedlist.pop(e)
                    reducedlist.append((y1, x2))
                    break

                elif x1 < y1 and x2 > y1 and x2 < y2:
                    reducedlist.pop(e)
                    reducedlist.append((x1, y2))
                    break
                elif x1 < y1 and x2 > y2:
                    reducedlist.pop(e)
                    reducedlist.append(i)
                    break
                if e == size-1:
                    reducedlist.append(i)
    return reducedlist


inputlist = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(reduce(inputlist))
