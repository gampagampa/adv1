from main import read_file
import pandas as pd


def get_total_dir_size(current_dict, dir_list):
    dir_size = 0
    for key in current_dict:
        current_item = current_dict[key]
        if isinstance(current_item, dict):
            dir_size += get_total_dir_size(current_item, dir_list)
        else:
            dir_size += current_item
    dir_list.append(dir_size)
    return dir_size


def process():
    file = read_file('adv/adv_7.txt')

    friendly_dict = {'root': {}}
    prev_entry = ''
    current_dict = friendly_dict['root']
    path = []
    total_dir_sizes = 0
    for entry in file:
        if prev_entry == '$ cd /' and entry == '$ ls':
            current_dict = friendly_dict['root']
            path = ['root']

        elif prev_entry.startswith('$ cd') and entry == '$ ls':
            directory = prev_entry.split(' ')[2]
            current_dict = current_dict['dir ' + directory]
            path += ['dir ' + directory]

        elif entry.startswith('$ cd ..'):
            path = path[:-1]

            for dir in path:
                if dir == 'root':
                    current_dict = friendly_dict[dir]
                else:
                    current_dict = current_dict[dir]

        if entry.startswith('dir'):
            current_dict[entry] = {}
        elif entry[0].isdigit():
            split_entry = entry.split(' ')
            size = int(split_entry[0])
            name = split_entry[1]
            current_dict[name] = size
            if name == 'mzvb' and file.index(entry) < 10:
                total_dir_sizes += size

        prev_entry = entry

    # print(total_dir_sizes + 95962)
    dir_list = []
    for key in friendly_dict['root']:
        current_dict = friendly_dict['root'][key]
        if isinstance(current_dict, dict):
            get_total_dir_size(current_dict, dir_list)

    dir_list_smaller_100k = [i for i in dir_list if i <= 100000]
    print(f'part A: {sum(dir_list_smaller_100k)}')

    # part B
    total_dir_size = get_total_dir_size(friendly_dict, dir_list)

    available = 70000000 - total_dir_size - 30000000
    dir_list.sort()

    for entry in dir_list:
        if entry > abs(available):
            print(f'dir to delete: {entry}')
            break


if __name__ == '__main__':
    process()
