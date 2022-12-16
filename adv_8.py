from main import read_file
import numpy as np


def create_matrix(file):
    x = len(file[0])
    y = len(file)
    matrix = np.zeros([x, y])

    for key_x, entry in enumerate(file):
        for key_y, number in enumerate(entry):
            matrix[key_x, key_y] = int(number)

    return matrix


file = read_file('adv/adv_8.txt')

matrix = create_matrix(file)

umfang = matrix.shape[0] * 2 + matrix.shape[1] * 2 - 4


def check_val(val, check_below):
    temp_m = val > check_below
    return False not in temp_m


def is_entry_visible(val, matrix,  key_x, key_y):

    check_below = matrix[key_x+1:, key_y]
    check_top = matrix[:key_x, key_y]
    check_right = matrix[key_x, key_y + 1:]
    check_left = matrix[key_x, :key_y]
    if check_val(val, check_below) or \
        check_val(val, check_top) or \
        check_val(val, check_right) or \
        check_val(val, check_left):
        return True
    else:
        return False


def get_interior_values(matrix):
    count_visible = 0
    for key_x, entry in enumerate(matrix[1:-1, 1:-1]):
        for key_y, val in enumerate(entry):
            if is_entry_visible(val, matrix, key_x + 1, key_y + 1):
                count_visible += 1
    return count_visible

interior = get_interior_values(matrix)


def calc_score(val, check_):
    score = 1
    for entry in check_:
        if val > entry:
            score += 1
        else:
            break
    return min(score, len(check_))


def get_score(viewing_score_list, matrix, val, key_x, key_y):
    if val == 0:
        return
    check_below = matrix[key_x + 1:, key_y]
    check_top = np.flip(matrix[:key_x, key_y].T)
    check_right = matrix[key_x, key_y + 1:]
    check_left = np.flip(matrix[key_x, :key_y])

    score_below = calc_score(val, check_below)
    score_top = calc_score(val, check_top)
    score_right = calc_score(val, check_right)
    score_left = calc_score(val, check_left)

    viewing_score_list.append(score_top * score_below * score_right * score_left)


def get_best_viewing_score(matrix):
    viewing_score_list = []
    for key_x, entry in enumerate(matrix[1:-1, 1:-1]):
        for key_y, val in enumerate(entry):
            get_score(viewing_score_list, matrix, val, key_x + 1, key_y + 1)
    return max(viewing_score_list)


best_viewing_score = get_best_viewing_score(matrix)

print(umfang + interior)
print(best_viewing_score)
