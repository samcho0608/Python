# variable argument aka ... argument
def profile(name, age, *languages):
    print("이름: {0}\t나이: {1}\t사용 가능 언어: ".format(name, age), end = " ")
    for lang in languages:
        print(lang, end = " ")
    print()

profile("sam", 20, "java", "python", "kotlin", "C")
profile("daniel", 20, "java", "c")

# how to change the global variable within the function call
gun = 70

def checkpoint(sold):
    global gun
    gun -= sold
    print("Remaining guns: {0}".format(gun))

print(gun)
checkpoint(25)
print(gun)
