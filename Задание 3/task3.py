file_list = ['Задание 3\\1.txt', 'Задание 3\\2.txt', 'Задание 3\\3.txt']
file_lines = {}

for file_name in file_list:
    with open(file_name, 'r', encoding='utf8') as f:
        lines = f.readlines()
        file_lines[file_name] = len(lines)

sorted_files = sorted(file_lines.items(), key=lambda x: x[1])

with open('Задание 3\\result.txt', 'w', encoding='utf8') as res_f:
    for name, lines in sorted_files:
        res_f.write(name + '\n')
        res_f.write(str(lines) + '\n')
        with open(name, 'r', encoding='utf8') as text:
            res_f.writelines(text.readlines())
        res_f.write('\n')
