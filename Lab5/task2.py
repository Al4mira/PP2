import re

def match_pattern(filename):
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            if re.search('аб{2,3}', line):
                print("Строка соответствует шаблону")
            else:
                print("Строка не соответствует шаблону")


filename = "row.txt"
match_pattern(filename)