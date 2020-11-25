# dictionary can be formed with {}
# attains a pair of data where one is a key for the other

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

# outputs an error when input an unregistered key
# print(cabinet[5])
# on the other hand the "get" function just outputs None, instead of calling error
print(cabinet.get(5))

# if the input value is not registered as a key, 
# outputs the second input as the output instead of None
print(cabinet.get(5, "open spot"))

# however, it doesn't register first and second input pair
# as part of the dictionary
print(cabinet)

# to check if smth is registered in dict
print(3 in cabinet)
print(5 in cabinet)

# how to add a new value to dict
cabinet["Debs"] = "해인"
print(cabinet)

# how to rid of a value
del cabinet["Debs"]
print(cabinet)

# how to print only keys
print(cabinet.keys())

# how to print only vals
print(cabinet.values())

# how to print both
print(cabinet.items())

# Note: the above three functions output
# their own special classes
# e.g. <class 'dict_items'>

# To clear
cabinet.clear()
print(cabinet)