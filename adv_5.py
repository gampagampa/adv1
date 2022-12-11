
from main import read_file


def move_from_to(from_, to_, list_of_lists):
    from_list = list_of_lists[from_ - 1]
    to_list = list_of_lists[to_ - 1]

    entry = from_list[-1]
    from_list.pop(-1)
    to_list = to_list.append(entry)


def move_from_to2(quanity, from_, to_, list_of_lists):
    from_list = list_of_lists[from_ - 1]
    to_list = list_of_lists[to_ - 1]

    entries = from_list[-quanity:]
    for entry in entries:
        from_list.pop(-1)
        to_list.append(entry)


def execute_command(entry, list_of_lists):
    entry = entry.split(' ')

    quantity = int(entry[1])

    from_ = int(entry[3])
    to_ = int(entry[5].replace('\n', ''))
    
    for i in range(1, quantity+1):
        move_from_to(from_, to_, list_of_lists)


def execute_command2(entry, list_of_lists):
    entry = entry.split(' ')

    quantity = int(entry[1])

    from_ = int(entry[3])
    to_ = int(entry[5].replace('\n', ''))

    move_from_to2(quantity, from_, to_, list_of_lists)


def process():
    file = read_file('adv/adv_5.txt')

    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []

    initials = file[:8]
    initials.reverse()
    commands = file[10:]

    for entry in initials:
        first_entry = entry[:3]
        list_1.append(first_entry) if first_entry != '   ' else ''
        second_entry = entry[4:7]
        list_2.append(second_entry) if second_entry != '   ' else ''
        third_entry = entry[8:11]
        list_3.append(third_entry) if third_entry != '   ' else ''
        fourth_entry = entry[12:15]
        list_4.append(fourth_entry) if fourth_entry != '   ' else ''
        fifth_entry = entry[16:19]
        list_5.append(fifth_entry) if fifth_entry != '   ' else ''
        sixth_entry = entry[20:23]
        list_6.append(sixth_entry) if sixth_entry != '   ' else ''
        seventh_entry = entry[24:27]
        list_7.append(seventh_entry) if seventh_entry != '   ' else ''
        eight_entry = entry[28:31]
        list_8.append(eight_entry) if eight_entry != '   ' else ''
        ninth_entry = entry[32:35]
        list_9.append(ninth_entry) if ninth_entry != '   ' else ''

    list_of_lists = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]

    for entry in commands:
        execute_command(entry, list_of_lists)

    for entry in list_of_lists:
        print(entry[-1])

def process2():
    file = read_file('adv/adv_5.txt')

    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []

    initials = file[:8]
    initials.reverse()
    commands = file[10:]

    for entry in initials:
        first_entry = entry[:3]
        list_1.append(first_entry) if first_entry != '   ' else ''
        second_entry = entry[4:7]
        list_2.append(second_entry) if second_entry != '   ' else ''
        third_entry = entry[8:11]
        list_3.append(third_entry) if third_entry != '   ' else ''
        fourth_entry = entry[12:15]
        list_4.append(fourth_entry) if fourth_entry != '   ' else ''
        fifth_entry = entry[16:19]
        list_5.append(fifth_entry) if fifth_entry != '   ' else ''
        sixth_entry = entry[20:23]
        list_6.append(sixth_entry) if sixth_entry != '   ' else ''
        seventh_entry = entry[24:27]
        list_7.append(seventh_entry) if seventh_entry != '   ' else ''
        eight_entry = entry[28:31]
        list_8.append(eight_entry) if eight_entry != '   ' else ''
        ninth_entry = entry[32:35]
        list_9.append(ninth_entry) if ninth_entry != '   ' else ''

    list_of_lists = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]

    for entry in commands:
        execute_command2(entry, list_of_lists)

    for entry in list_of_lists:
        print(entry[-1], end=" ")

if __name__ == '__main__':
    # process()
    process2()
