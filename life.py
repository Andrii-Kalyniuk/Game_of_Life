import os
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def find_neighborhood(row, column, gen):
    # todo: loop the borders of the matrix
    neighborhood = []
    steps = (
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (-1, -1), (1, -1)
    )
    for row_step, column_step in steps:
        if row + row_step >= 0 and \
                row + row_step < len(gen) and \
                column + column_step >= 0 and \
                column + column_step < len(gen[row]):
            neighborhood.append(gen[row + row_step][column + column_step])
    return (row, column), neighborhood, sum(neighborhood)


def find_neighborhood_unlim(row, column, gen):
    neighborhood = []
    steps = (
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (-1, -1), (1, -1)
    )
    for row_step, column_step in steps:
        if row + row_step >= len(gen):  # 2+(-3+1) = 0
            row_step = -len(gen) + 1
        if column + column_step >= len(gen[row]):
            column_step = -len(gen[row]) + 1
        neighborhood.append(gen[row + row_step][column + column_step])
    return (row, column), neighborhood, sum(neighborhood)


def next_generation(gen):
    # gen_next = gen[:]  # not work
    # gen_next = list(gen)  # not work
    gen_next = []
    for row in range(len(gen)):
        gen_next.append(gen[row][:])  # it's work
        for column in range(len(gen[row])):
            # print(find_neighborhood(row, column, gen))
            life_count = find_neighborhood_unlim(row, column, gen)[2]
            # todo: refactor ifs, maybe use dict
            if gen[row][column] == 1 and life_count in (2, 3):
                pass  # stay alive
            if gen[row][column] == 0 and life_count == 3:
                gen_next[row][column] = 1  # born()
            if gen[row][column] == 1 and (life_count <= 1 or life_count >= 4):
                gen_next[row][column] = 0  # die()
        # print('---now--->', gen[row])
        # print('---new--->', gen_next[row])
    return gen_next


if __name__ == "__main__":

    gen_0 = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    clear_screen()
    number_of_gen = 100
    for _ in range(number_of_gen):
        gen_0 = next_generation(gen_0)
        for line in gen_0:
            print(line)
        print('-' * 20, _ + 1)
        time.sleep(0.5)
        if _ != number_of_gen - 1:
            clear_screen()
            # todo how to clear screen in PyCharm terminal?
            # works only 4 Linux terminal
            # cursor_up_and_home = "\033[F"
            # cursor_down = "\033[B"
            # print(cursor_up_and_home * (len(gen_0) + 1), end='')
    # print(cursor_down * (len(gen_0) + 1))
