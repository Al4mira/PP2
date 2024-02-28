def replace(input_file, output_file):
    with open(input_file, 'r', encoding='UTF-8') as file:
        text = file.read()
        new_text = text.replace(' ', ':').replace(',', ':').replace('.', ':')

    with open(output_file, 'w', encoding='UTF-8') as file:
        file.write(new_text)


input_filename = "row.txt"
output_filename = "row.txt"
replace(input_filename, output_filename)