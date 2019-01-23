myUniqueList = []
myLeftovers = []

def add_to_myUniqueList(item):
    if item in myUniqueList:
        myLeftovers.append(item)
        return False
    else:
        myUniqueList.append(item)
        return True
print(add_to_myUniqueList(1))
print(add_to_myUniqueList(1))
print(add_to_myUniqueList(5))
print(add_to_myUniqueList(5))
print(add_to_myUniqueList("ball"))
print(add_to_myUniqueList(7))
print(add_to_myUniqueList(3.14))
print(add_to_myUniqueList(8))
print(add_to_myUniqueList(9))
print(add_to_myUniqueList(3))
print(add_to_myUniqueList(7))
print(add_to_myUniqueList(3))
print(add_to_myUniqueList("ball"))

#output the list
print(myUniqueList)
print(myLeftovers)