def get_disected_value(entry, first_part, second_part):
    for letter in entry:
        if letter in first_part and letter in second_part:
            return letter


def get_transferred_value(disected_value):
    if disected_value.islower():
        disected_value = ord(disected_value) - 96
    else:
        disected_value = ord(disected_value) - 38
    return disected_value


def process():
    with open('adv/adv_3.txt') as f:
        file = f.readlines()

    transferred_value_sum = 0
    for entry in file:
        entry = entry.replace('\n', '')
        entry_length = len(entry)
        first_part = entry[:int((entry_length/2))]
        second_part = entry[int(entry_length/2):]

        disected_value = get_disected_value(entry, first_part, second_part)
        transferred_value = get_transferred_value(disected_value)
        transferred_value_sum += transferred_value
    print(transferred_value_sum)


def process():
    with open('adv/adv_3.txt') as f:
        file = f.readlines()
    transferred_value_sum = 0
    steps = 0
    for i, j, k in zip(file[0::3], file[1::3], file[2::3]):
        i = i.replace('\n', '')
        j = j.replace('\n', '')
        k = k.replace('\n', '')
        disected_value = get_disected_value(i, j, k)
        if disected_value is not None:
            transferred_value = get_transferred_value(disected_value)
            transferred_value_sum += transferred_value
        else:
            print('uff ')
        steps += 1
    print(transferred_value_sum)



if __name__ == '__main__':
    # process()
    process()
