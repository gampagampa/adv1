from main import read_file
import pandas as pd


def get_total_dir_size(current_dict):
    sum = 0
    for key in current_dict:
        val = current_dict[key]

        if isinstance(val, int):
            sum += val
        else:
            for key2 in val:
                val2 = val[key2]
                if isinstance(val2, int):
                    sum += val2
                else:
                    for key3 in val2:
                        val3 = val2[key3]
                        if isinstance(val3, int):
                            sum += val3
                        else:
                            for key4 in val3:
                                val4 = val3[key4]
                                if isinstance(val4, int):
                                    sum += val4
                                else:
                                    for key5 in val4:
                                        val5 = val4[key5]
                                        if isinstance(val5, int):
                                            sum += val5
                                        else:
                                            for key6 in val5:
                                                val6 = val5[key6]
                                                if isinstance(val6, int):
                                                    sum += val6
                                                else:
                                                    for key7 in val6:
                                                        val7 = val6[key7]
                                                        if isinstance(val7, int):
                                                            sum += val7
                                                        else:
                                                            print('hi')

    return sum if sum <= 100000 else 0


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
            total_dir_sizes += get_total_dir_size(current_dict)
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
        prev_entry = entry

    print(total_dir_sizes + 95962)


if __name__ == '__main__':
    process()
