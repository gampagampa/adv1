import math

import self as self

from main import read_file

class Item:
    def __init__(self, val):
        self.value = val
        self.div_by_13 = False
        self.div_by_17 = False
        self.div_by_19 = False
        self.div_by_23 = False

    def change_value(self, val):
        self.value = val


class Monkey:
    def __init__(self, current_items, operation_factor, operation, test_factor, test_true, test_false):
        self.current_items = current_items
        self.operation_factor = operation_factor
        self.operation = operation
        self.test_factor = test_factor
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0

    def do_operation(self, item):
        input_ = item.value
        if self.operation_factor == 'squarred':
            new_value = input_ * input_
        elif self.operation == '*':
            new_value = input_ * self.operation_factor
        else:
            new_value = input_ + self.operation_factor

        item.change_value(math.floor(new_value/3))

    def is_val_divisible(self, item):
        val = item.value

        return val % self.test_factor == 0

    def get_rest(self, val):
        return val % self.test_factor

    def add_item(self, item):
        current_items = self.current_items
        self.current_items = current_items + [item]

    def remove_first_item(self):
        self.current_items = self.current_items[1:]

    def increase_inspection_nr(self):
        self.inspected = self.inspected + 1


def get_monkey_from_list(list_):
    return Monkey(list_[0], list_[1], list_[2], list_[3], list_[4], list_[5])


def get_operation_factor(file, key):
    operation_factor = file[key*7 + 2].split(' ')[-1]

    if operation_factor == 'old':
        return 'squarred'
    else:
        return int(operation_factor)
    pass


def do_monkey_business(monkey, monkeys):
    for item in monkey.current_items:

        monkey.do_operation(item)
        if monkey.is_val_divisible(item):
            transfer_to = monkey.test_true
        else:
            transfer_to = monkey.test_false

        monkey.increase_inspection_nr()
        monkey.remove_first_item()
        monkey_to_transfer = monkeys[transfer_to]
        # todo check
        monkey_to_transfer.add_item(item)


def process_round(monkeys):
    count = 0
    for monkey in monkeys:
        do_monkey_business(monkey, monkeys)
        count += 1


def process():
    file = read_file('adv/adv_11_test.txt')

    monkey_list = []
    for key, entry in enumerate(file[::7]):
        starting_items = file[key * 7 + 1].split(' ')[4:]
        starting_items = [int(k.replace(',', '')) for k in starting_items]
        starting_items = [Item(k) for k in starting_items]
        operation_factor = get_operation_factor(file, key)
        operation = file[key * 7 + 2].split(' ')[-2]
        test_factor = int(file[key * 7 + 3].split(' ')[-1])
        true_throw = int(file[key * 7 + 4].split(' ')[-1])
        false_throw = int(file[key * 7 + 5].split(' ')[-1])

        monkey_list.append([starting_items, operation_factor, operation, test_factor, true_throw, false_throw])

    monkey_0 = get_monkey_from_list(monkey_list[0])
    monkey_1 = get_monkey_from_list(monkey_list[1])
    monkey_2 = get_monkey_from_list(monkey_list[2])
    monkey_3 = get_monkey_from_list(monkey_list[3])
    """monkey_4 = get_monkey_from_list(monkey_list[4])
    monkey_5 = get_monkey_from_list(monkey_list[5])
    monkey_6 = get_monkey_from_list(monkey_list[6])
    monkey_7 = get_monkey_from_list(monkey_list[7])"""

    # monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
    monkeys = [monkey_0, monkey_1, monkey_2, monkey_3]

    for i in range(1, 21):
        print(i) if i % 100 == 0 else 0
        process_round(monkeys)

    monkey_inspection_list = []
    for monkey in monkeys:
        monkey_inspection_list.append(monkey.inspected)

    monkey_inspection_list.sort()
    print(monkey_inspection_list[-1]*monkey_inspection_list[-2])


if __name__ == '__main__':
    process()
