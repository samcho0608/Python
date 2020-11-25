print("python", "java", sep = ",", end="?")
print("which one is better?")

import sys
print("Python","Java", file = sys.stdout)
print("Python","Java", file = sys.stderr)

scores = {"math":0, "eng":100, "cs":100}
for subj, score in scores.items():
    # print(subj, score)
    print(subj.ljust(5),str(score).rjust(4), sep = ":")
    # ljust: save n amt of space and left align
    # rjust: ljust except right align

for num in range(1,21):
    print("대기 번호: " + str(num).zfill(3))
    # zfill: save n amt space and fill them up with 0's

answer = input("input smth: ")
print(answer, type(answer))
# input by default takes the type str
# cast the data type on input to specify the type

answer = int(input("input smth: "))
print(answer, type(answer))


# 빈 자리는 빈 공간으로, 오른쪽 정렬, 총 10자리 확보
print("{0: >10}".format(500))
# + if positive, - if negative
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# left align, fill in with _
print("{0:_<10}".format(500))
# place a comma every 3rd digit
print("{0:,}".format(1000000000))
# same as above except with the pos/neg sign
print("{0:+,}".format(1000000000))
# combination of the above
print("{0:^<+30,}".format(1000000000000))
# decimal point
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) # to hundredth place
