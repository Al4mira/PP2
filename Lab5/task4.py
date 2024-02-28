import re

def find_upper_lower_sequences_in_file(filename):
    with open(filename, encoding='UTF-8') as file:
        text = file.read()
        pattern = r'\b[А-Я][а-я]+\b'
        upper_lower_sequences = re.findall(pattern, text)
        return upper_lower_sequences


filename = "row.txt"
sequences = find_upper_lower_sequences_in_file(filename)

print(sequences)