import re 
# re : regex library

p = re.compile("ca.e") # sets the regex that we will use to match
# . : a single character
# ^ : beginning of the string
# $ : end of the character

def print_match(m):
    if m:
        print("m.group():", m.group())  # matched string(e.g. regex: ca.e, input : careless, m.group(): care)
        print("m.string", m.string) # the input string(e.g. careless)
        print("m.start():", m.start()) # the first index of the matched string
        print("m.end():", m.end())  # the last index of the matched string(uninclusive)
        print("m.span():", m.span())    # tuple of the first and last index of the matched string
    else:
        print("not matched")



# m = p.match("good case")   # match : checks if the input string matches from the beginning
# print_match(m)
# print(m.group()) # if not matched, raises error

# m = p.search("final case")    # search : checks if there is a match anywhere within the given string(only the first match)
# print_match(m)

# lst = p.findall("good care cafe case")   # findall : return a list of all matched strings
# print(lst)