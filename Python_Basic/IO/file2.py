print("Using the while loop method: ")

score_file = open("score.txt", "r", encoding="utf8")

# to read till the end without knowing the actual length of the file
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()

print("\nUsing the list method: ")

# or you save the entire file as a list
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # save data in the form of list

for line in lines:
    print(line, end = "")
score_file.close()