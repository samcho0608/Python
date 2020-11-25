
# create list with []
subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# How to find the index of a certain element
seho = "조세호"
print("%s는 %d 호차에 탑승하고 있습니다." % (seho, subway.index(seho)))

# append
subway.append("하하")
print(subway)

# insert
subway.insert(1, "정형돈")
print(subway)

# list as stack
print(subway.pop())
print(subway)

# counting the number of certain element
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# sort
num_list = [5,2,3,4,1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

# may contain different data types

mix_list = [True, 20, "bro"]

# concatenating two different lists
mix_list.extend(subway)
print(mix_list)