from main import read_file
import numpy as np


def move_down(position):
    position['y'] = [position['y'][0] - 1]


def move_up(position):
    position['y'] = [position['y'][0] + 1]


def move_right(position):
    position['x'] = [position['x'][0] + 1]


def move_left(position):
    position['x'] = [position['x'][0] - 1]


def follow_head(position_h, position_t):
    x_h = position_h['x'][0]
    y_h = position_h['y'][0]

    x_t = position_t['x'][0]
    y_t = position_t['y'][0]

    if abs(x_h - x_t) > 1 or abs(y_h - y_t) > 1:
        return True
    else:
        return False


def do_follow(position_H, position_T, arr):
    x_h = position_H['x'][0]
    y_h = position_H['y'][0]

    x_t = position_T['x'][0]
    y_t = position_T['y'][0]

    x_diff = abs(x_h - x_t)
    y_diff = abs(y_h - y_t)

    if x_diff > 1 and y_diff > 0:
        position_T['x'] = [max([x_t, x_h]) - 1]
        position_T['y'] = [y_h]

    elif x_diff > 0 and y_diff > 1:
        position_T['x'] = [x_h]
        position_T['y'] = [max([y_t, y_h]) - 1]

    elif x_diff > 0 and y_diff == 0:
        position_T['x'] = [max([x_t, x_h]) - 1]
    else:
        position_T['y'] = [max([y_t, y_h]) - 1]

    arr[position_T['x'][0], position_T['y'][0]] = 1


def do_moves(position_H, position_T, move, amount, arr):
    for i in range(1, amount + 1):
        if move == 'D':
            move_down(position_H)
        elif move == 'L':
            move_left(position_H)
        elif move == 'R':
            move_right(position_H)
        else:
            move_up(position_H)
        if follow_head(position_H, position_T):
            do_follow(position_H, position_T, arr)



file = read_file('adv/adv_9.txt')

arr = np.zeros([1000, 1000])
position_H = {'x': [500], 'y': [500]}
position_T = {'x': [500], 'y': [500]}
for entry in file:
    move = entry.split(' ')[0]
    amount = int(entry.split(' ')[1])

    do_moves(position_H, position_T, move, amount, arr)
print(f'unique steps: {arr.sum()}')

