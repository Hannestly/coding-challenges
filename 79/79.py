"""
Given an array of integers, write a function to determine whether the 
array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, 
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, 
since we can't modify any one element to get a non-decreasing array.
"""


def checkdec(inputlist):
    def subcheck(templist):
        for i in range(len(templist)-1):
            if templist[i] <= templist[i+1]:
                return True
        return False

    for i in range(len(inputlist)):
        templist = inputlist[:i] + inputlist[i+1:]
        if subcheck(templist) == True:
            return True

    return False


inputlist = [10, 5, 7]
print(checkdec(inputlist))
