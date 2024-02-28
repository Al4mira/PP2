import re

def camel_to_snake(text):
    s1 = re.sub('(.)([А-Я][а-я]+)', r'\1_\2', text)
    return re.sub('([а-я0-9])([А-Я])', r'\1_\2', s1).lower()


with open('row.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content = camel_to_snake(content)
f.close()
with open('row2.txt', 'w', encoding='utf-8') as g:
    g.write(content)
g.close()