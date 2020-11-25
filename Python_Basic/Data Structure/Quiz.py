# 1명은 치킨, 3명은 커피
# 1~20 중 무작위로
# 중복 불가
# random module의 shuffle과 sample을 사용

# shuffle(CLASSNAME) returns randomly sorted CLASSNAME
# sample(CLASSNAME, NUM) returns randomly chosen sample of number NUM from CLASSNAME

from random import sample, shuffle

numList = list(range(1,21))
shuffle(numList)
winners = sample(numList, 4)
print("치킨쿠폰: {chicken}\n커피쿠폰: {coffee}".format(chicken=winners[0], coffee=winners[1:]))