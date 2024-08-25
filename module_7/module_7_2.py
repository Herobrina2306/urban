def custom_write(file_name, strings):
    f = open(file_name, 'r+', encoding='utf-8')
    p = []
    for i in range(len(strings)):
        pos = (i + 1, f.tell())
        f.writelines(strings[i] + '\n')
        p.append(pos)
    sp = {}
    for j in range(len(strings)):
        sp[p[j]] = [strings[j]]
    return sp
    f.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)