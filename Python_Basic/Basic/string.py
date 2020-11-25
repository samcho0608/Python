# in python '' and "" function basically the same

intro = """Hello
My name is
Sam Cho"""
print(intro)


social_security = "990608-1234567"
#  positive ind    0123456789
#  negative ind(-)      987654321

print("Gender: " + "남자" if (social_security[7] == "1") else "여자")
print("Birth Year: " + social_security[0:2])
print("Birth: " + social_security[:6])
print("From 7 to end: " + social_security[7:])
print("From 7th from the end till the end: " + social_security[-7:])

print(intro.lower())
print(intro.upper())
print(intro[0].isupper())
print(len(intro))
print(intro.replace("Hello", "Bye"))

first_newline = intro.index("\n")
print(first_newline)
print(intro.index("\n", first_newline + 1))
print(intro.find("\n"))

# index vs find
# if error found, find outputs -1 while index calls an error and stops the interpreter

print(intro.count("\n"))
print("I ate %d apples" % 20)
print("Apple starts with the letter %c" % "A")

# Types of string format method
# 1.
print("I like %s and %s" % ("blue", "green"))
# 2.
print("I like {} and {}".format("blue", "green"))
# 3.
print("I like {1} and {0}".format("blue", "green"))
# 4.
print("I like {last} and {first}".format(first = "blue", last = "green"))
# 5.(v3.6~)
color = "green"
age = 22
print(f"I am {age} years old and {color} is my favorite color.")


# '\r': Escape character functioning like the "home" button
# Brings the cursor to the front
print("Red Apple\rPine")

# '\b': backspace
print("k\bnight")


# Quiz

website = "http://facebook.com"
website = "http://google.com"
# get rid of the https://
# get rid of anything after the first period
# form the pw with first 3 characters, the number of characters, the number of e's in the string, and "!"

first_condition = website[len("http://"):]
second_condition = first_condition[:first_condition.index(".")]
print(second_condition[:3], len(second_condition), second_condition.count("e"),"!", sep="")