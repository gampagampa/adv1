def is_draw(opp, myself):
    if opp == 'A' and myself == 'X':
        return True
    elif opp == 'B' and myself == 'Y':
        return True
    elif opp == 'C' and myself == 'Z':
        return True
    else:
        return False


def is_win(opp, myself):
    if opp == 'A' and myself == 'Y':
        return True
    elif opp == 'B' and myself == 'Z':
        return True
    elif opp == 'C' and myself == 'X':
        return True
    else:
        return False


def is_win2(opp, myself):
    return opp == 'A'


def get_points_for_my_choice(myself):
    if myself == 'X':
        return 1
    elif myself == 'Y':
        return 2
    else:
        return 3


def process():
    with open('adv/adv_2.txt') as f:
        file = f.readlines()

    count_points = 0
    # a rock = 1, b paper = 2,  c scissors = 3
    # x rock = 1 y paper = 2, z scissors = 3
    for entry in file:
        entry = entry.replace('\n', '').split(' ')
        opponent = entry[0]

        myself = entry[1]
        points_for_my_choice = get_points_for_my_choice(myself)

        count_points += points_for_my_choice
        if is_draw(opponent, myself):
            count_points += 3
        elif is_win(opponent, myself):
            count_points += 6
        else:
            count_points += 0
    print(count_points)


def play_draw(opponent):
    if opponent == 'A':
        return 'X'
    elif opponent == 'B':
        return 'Y'
    else:
        return 'Z'


def play_lose(opponent):
    if opponent == 'A':
        return 'Z'
    elif opponent == 'B':
        return 'X'
    else:
        return 'Y'


def play_win(opponent):
    if opponent == 'A':
        return 'Y'
    elif opponent == 'B':
        return 'Z'
    else:
        return 'X'


def get_my_strategy(opponent, param):
    if param == 'X':
        # TODO: loose
        return play_lose(opponent)
    if param == 'Y':
        # play draw
        return play_draw(opponent)
    elif param == 'Z':
        return play_win(opponent)


def process_pt2():
    with open('adv/adv_2.txt') as f:
        file = f.readlines()

    count_points = 0
    # a rock = 1, b paper = 2,  c scissors = 3
    # x lose,  y = draw , z win
    for entry in file:
        entry = entry.replace('\n', '').split(' ')
        opponent = entry[0]

        myself = get_my_strategy(opponent, entry[1])
        points_for_my_choice = get_points_for_my_choice(myself)

        count_points += points_for_my_choice
        if is_draw(opponent, myself):
            count_points += 3
        elif is_win(opponent, myself):
            count_points += 6
        else:
            count_points += 0
    print(count_points)


if __name__ == '__main__':
    # process()
    process_pt2()
