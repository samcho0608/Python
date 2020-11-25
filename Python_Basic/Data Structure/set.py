# 집합 (set)
# 중복 불가, 순서 x

# create set with {}
my_set = {1,2,3,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# intersection
print(java & python) # java and python
print(java.intersection(python))

# union
print(java | python) # java or python
print(java.union(python))

# difference
print(java - python) # java but not python
print(java.difference(python))

# addition and removal of an element to/from a set
python.add("김태호")
print(python)

python.remove("김태호")
print(python)