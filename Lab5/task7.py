def snake_to_camel(input_file, output_file):
    with open(input_file, 'r', encoding='UTF-8') as file:
        snake_case_text = file.read()
        components = snake_case_text.split('_')
        camel_case_text = components[0] + ''.join(x.title() for x in components[1:])

    with open(output_file, 'w', encoding='UTF-8') as file:
        file.write(camel_case_text)


input_filename = "row.txt"
output_filename = "row.txt"
snake_to_camel(input_filename, output_filename)