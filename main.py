# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_file(link):
    with open(link) as f:
        lines = f.read().splitlines()

    return lines

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # txt = open('adv/adv_1.txt')
    with open('adv/adv_1.txt') as f:
        lines = f.readlines()

    calories_max = 0
    current_sum = 0
    calories_list = []
    for line in lines:
        line = line.replace('\n', '')
        if line == '':
            calories_list.append(current_sum)
            if current_sum > calories_max:
                calories_max = current_sum
            current_sum = 0
        else:
            current_sum += int(line)

    calories_list.sort()
    print(sum(calories_list[-3:]))
    print(calories_max)



    print('finished')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
