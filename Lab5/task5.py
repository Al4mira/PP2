import re

def start_end(filename):
    with open(filename, encoding='UTF-8') as file:
        text = file.read()
        pattern = r'(.*?)(a)(.*?)(\W*)(b)'
        result = re.search(pattern, text)
        return result

filename = "row.txt"
result = start_end(filename)
if result:
    print("Match found in the file!")
else:
    print("No match in the file.")