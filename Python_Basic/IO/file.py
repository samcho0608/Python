
# how to create a file and write into that file
score_file = open("score.txt", "w", encoding="utf8") 
# w for write
# if done once again on the same file, the program overwrites
print("math : 0", file=score_file)
print("english : 50", file=score_file)
score_file.close()

# to not overwrite but append, use the "a" parameter
score_file = open("score.txt", "a", encoding="utf8") # w for write
score_file.write("science: 80")
score_file.write("\nCS: 100")
score_file.close()

# to only read the file, use the "r" parameter
score_file = open("score.txt", "r", encoding= "utf8")
# reads the entire file
print(score_file.read())
# read the line at the top only and move the cursor
# to the beginning of the next line
print(score_file.readline())
score_file.close()

