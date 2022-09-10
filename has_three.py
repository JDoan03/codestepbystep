# Write a function named has_three that accepts a list of strings as a
# parameter and returns True if any string value occurs at least 3 times
# in the list. For example, in the list ["to", "be", "or", "be", "to",
# "be", "hamlet"], the word "be" occurs 3 times, so your function would
# return True if passed that list. Use a dict as auxiliary storage to help
# solve the problem. Do not modify the list that is passed in.


def has_three(listString):

    if len(listString) == 0 or len(listString) == 1 or len(listString) == 2:
        return False

    mainDict = {}
    for x in listString:
        if x not in mainDict:
            mainDict[x] = 1
        else:
            mainDict[x] = mainDict.get(x) + 1

    for x in mainDict.values():
        if x >= 3:
            return True
        else:
            return False