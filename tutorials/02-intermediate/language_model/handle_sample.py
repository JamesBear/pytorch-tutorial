
import os

file_name_format = 'sample{}.txt'

def get_file_content(path, encoding='utf-8'):
    f = open(path, encoding=encoding)
    content = f.read()
    f.close()
    return content

def write_to_file(path, content, encoding='utf-8'):
    f = open(path, 'w', encoding=encoding)
    f.write(content)
    f.close()


def get_available_file_name():
    for i in range(2, 100):
        name = file_name_format.format(i)
        if os.path.exists(name):
            continue
        return name

def strip_spaces(s):
    return s.replace('   ', '>%$^$&"').replace(' ', '').replace('>%$^$&"', ' ')

if __name__ == '__main__':
    s = get_file_content('sample.txt')
    s = strip_spaces(s)
    path = get_available_file_name()
    write_to_file(path, s)
    print('File written to ', path)