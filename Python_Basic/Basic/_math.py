print(abs(-5))
print(pow(4,2))
print(max(2,4))
print(min(10,2))
print(round(0.98))
print(round(3.12))

from math import ceil, floor, sqrt
print(floor(0.05))
print(ceil(3.14))
print(sqrt(16))

from random import randrange, randint, random
print(random()) # randomly chosen number within the range [0.0,1.0)
print(random() * 10) # randomly chosen number within the range [0.0,10.0)
print(int(random() * 10)) # randomly chosen integer within the range [0,10)
print(int(random() * 10) + 1) # randomly chosen integer within the range [1,10]

print(randrange(1, 46)) # randomly chosen integer within the range [1,46)
print(randint(1,45)) # randomly chosen integer within the range [1, 45]