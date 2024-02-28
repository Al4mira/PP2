import re
def split_at_uppercase(s):
    words = []
    word = ""
    for c in s:
        if c.isupper():
            words.append(word)
            word = ""
        else:
            word += c
    words.append(word)
    return words


def split_at_uppercase_in_file(input_file, output_file):
    with open(input_file, 'r', encoding='UTF-8') as file:
        sentence = file.read()
        words = split_at_uppercase(sentence)

    with open(output_file, 'w', encoding='UTF-8') as file:
        for w in words:
            file.write(w + '\n')


input_filename = "row.txt"
output_filename = "row.txt"
split_at_uppercase_in_file(input_filename, output_filename)