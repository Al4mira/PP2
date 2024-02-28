import re

def pattern_match(myfile):
    with open(myfile, encoding='UTF-8' ) as file:
        for line in file:
            if re.search("аб*", line):
                return "Line matches the pattern"
            else:
                return "Line doesn't match the pattern"

myfile = "row.txt"
pattern_match(myfile)

