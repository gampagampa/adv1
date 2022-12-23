import math

import self as self

from main import read_file

class Item:
    def __init__(self, val):
        self.div_by_11_rest = val
        self.div_by_5_rest = val
        self.div_by_7_rest = val
        self.div_by_2_rest = val
        self.div_by_17_rest = val
        self.div_by_13_rest = val
        self.div_by_3_rest = val
        self.div_by_19_rest = val

    def change_value(self, val, i):
        if i == 1:
            self.div_by_11_rest = val % 11
        elif i == 2:
            self.div_by_5_rest = val % 5
        elif i == 3:
            self.div_by_7_rest = val % 7
        elif i == 4:
            self.div_by_2_rest = val % 2
        elif i == 5:
            self.div_by_17_rest = val % 17
        elif i == 6:
            self.div_by_13_rest = val % 13
        elif i == 7:
            self.div_by_3_rest = val % 3
        elif i == 8:
            self.div_by_19_rest = val % 19

    def get_attribute(self, i):
        if i == 1:
            return self.div_by_11_rest
        elif i == 2:
            return self.div_by_5_rest
        elif i == 3:
            return self.div_by_7_rest
        elif i == 4:
            return self.div_by_2_rest
        elif i == 5:
            return self.div_by_17_rest
        elif i == 6:
            return self.div_by_13_rest
        elif i == 7:
            return self.div_by_3_rest
        elif i == 8:
            return self.div_by_19_rest

    def get_relevant_value(self, test_factor):
        if test_factor == 13:
            return self.div_by_13_rest
        elif test_factor == 23:
            return self.div_by_23_rest
        elif test_factor == 19:
            return self.div_by_19_rest
        elif test_factor == 17:
            return self.div_by_17_rest
        elif test_factor == 3:
            return self.div_by_3_rest
        elif test_factor == 5:
            return self.div_by_5_rest
        elif test_factor == 11:
            return self.div_by_11_rest
        elif test_factor == 7:
            return self.div_by_7_rest
        elif test_factor == 2:
            return self.div_by_2_rest


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
        for i in range(1, len(item.__dict__) + 1):
            input_ = item.get_attribute(i)
            if self.operation_factor == 'squarred':
                new_value = input_ * input_
            elif self.operation == '*':
                new_value = input_ * self.operation_factor
            else:
                new_value = input_ + self.operation_factor

            # item.change_value(math.floor(new_value/3))
            item.change_value(new_value, i)

    def is_val_divisible(self, item):
        val = item.get_relevant_value(self.test_factor)

        return val == 0

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
    file = read_file('adv/adv_11.txt')

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
    monkey_4 = get_monkey_from_list(monkey_list[4])
    monkey_5 = get_monkey_from_list(monkey_list[5])
    monkey_6 = get_monkey_from_list(monkey_list[6])
    monkey_7 = get_monkey_from_list(monkey_list[7])

    monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
    # monkeys = [monkey_0, monkey_1, monkey_2, monkey_3]

    for i in range(1, 10001):
        print(i) if i % 100 == 0 else 0
        process_round(monkeys)

    monkey_inspection_list = []
    for monkey in monkeys:
        monkey_inspection_list.append(monkey.inspected)

    monkey_inspection_list.sort()
    print(monkey_inspection_list)
    print(monkey_inspection_list[-1]*monkey_inspection_list[-2])


if __name__ == '__main__':
    process()
