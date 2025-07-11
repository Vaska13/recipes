def read_file_with_line_count(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return {
        'name': filename,
        'line_count': len(lines),
        'content': lines
    }

# Список файлов для объединения
filenames = ['1.txt', '2.txt', '3.txt']

# Чтение данных из файлов
files_data = [read_file_with_line_count(f) for f in filenames]

# Сортировка по количеству строк
files_data.sort(key=lambda x: x['line_count'])

# Запись результата в итоговый файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_info in files_data:
        result_file.write(file_info['name'] + '\n')
        result_file.write(str(file_info['line_count']) + '\n')
        result_file.writelines(file_info['content'])