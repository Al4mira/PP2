import re 

def lowercase_sequence(filename):
    with open(filename, encoding='UTF-8') as file:
        text = file.read()
        pattern = r'\b[а-я]+_[а-я]+\b'
        lowercase_sequences = re.findall(pattern, text)
        return lowercase_sequences


filename = "row.txt"
sequences = lowercase_sequence(filename)

print(sequences)