def ranges_one_into_anoth(first_part, second_part):
    first_part_start = int(first_part.split('-')[0])
    first_part_end = int(first_part.split('-')[1])

    second_part_start = int(second_part.split('-')[0])
    second_part_end = int(second_part.split('-')[1])

    if first_part_start <= second_part_start and first_part_end >= second_part_end:
        return True
    elif second_part_start <= first_part_start and second_part_end >= first_part_end:
        return True
    else:
        return False


def is_overlapt(first_part, second_part):
    first_part_start = int(first_part.split('-')[0])
    first_part_end = int(first_part.split('-')[1])

    second_part_start = int(second_part.split('-')[0])
    second_part_end = int(second_part.split('-')[1])

    list_a = list(range(first_part_start, first_part_end + 1))
    list_b = list(range(second_part_start, second_part_end + 1))

    return len(set(list_a).intersection(list_b)) > 0


def process():
    with open('adv/adv_4.txt') as f:
        file = f.readlines()

    count = 0
    count_overlap = 0
    for entry in file:
        entry = entry.replace('\n', '')
        first_part = entry.split(',')[0]
        second_part = entry.split(',')[1]

        ranges_one_into_another = ranges_one_into_anoth(first_part, second_part)
        if ranges_one_into_another:
            count += 1

        overlap = is_overlapt(first_part, second_part)
        if overlap:
            count_overlap += 1

    print(count)
    print(count_overlap)

if __name__ == '__main__':
    process()
