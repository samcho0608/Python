# Dict
# key to get the value
myDict = {1:"apple", 2:"pear"}
print(myDict)

# List
# basically an array and stack
myList = [1,2,3,4,5,6,7]
print(myList)

# Tuple
# no change
myTuple = (1,2,3,4,4)
print(myTuple)

# used to assign multiple values into multiple variables
# e.g.
(name, age, gender) = ("조성민", 22, "남")
print(name, age, gender)

# Set
# no repetition and order
mySet = {1,2,3,3,3,4}
print(mySet)

# use & for intersection, | for union, and - for difference
america = {"Andy", "Daniel", "Debbie", "Shawn", "Mina", "Jiho"}
lakcm = {"Debbie", "Shawn"}

print(america & lakcm)
print(america | lakcm)
print(america - lakcm)