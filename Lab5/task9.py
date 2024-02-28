import re

def insert_spaces(text):
    result = ""
    for char in text:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result


with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()


spaced_text = insert_spaces(text)


print(spaced_text)