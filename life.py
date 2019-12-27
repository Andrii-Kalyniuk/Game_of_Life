import os
import time
from random import randrange

from generation_zero_patterns import (LWSS_raw,
                                      pulsar_raw,
                                      glider_gun_raw)


def clear_screen():
    """
    Clear console's screen in Windows or Linux
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def find_neighborhood(row, column, gen, ignore_borders=True):
    """
    Finds neighbors for the specified cell in an array at a distance of
    one cell and its sum
    """
    # done_todo: loop the borders of the matrix
    #   fixed in find_neighborhood_unlim()
    # done_todo: rename like find_neighborhood_with_boarders or just add
    #   parameter ignore_boarders=True
    neighborhood = []
    steps = (
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (-1, -1), (1, -1)
    )
    for row_step, column_step in steps:
        if ignore_borders:
            if row + row_step >= len(gen):
                row_step = -len(gen) + 1
            if column + column_step >= len(gen[row]):
                column_step = -len(gen[row]) + 1
            neighborhood.append(gen[row + row_step][column + column_step])
        else:
            if 0 <= row + row_step < len(gen) and \
                    0 <= column + column_step < len(gen[row]):
                neighborhood.append(gen[row + row_step][column + column_step])
    return (row, column), neighborhood, sum(neighborhood)


def find_neighborhood_unlim(row, column, gen):
    """
    Finds neighbors for the specified cell in an array at a distance of
    one cell neglecting the boundaries of the array
    """
    neighborhood = []
    steps = (
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (-1, -1), (1, -1)
    )
    for row_step, column_step in steps:
        if row + row_step >= len(gen):
            row_step = -len(gen) + 1
        if column + column_step >= len(gen[row]):
            column_step = -len(gen[row]) + 1
        neighborhood.append(gen[row + row_step][column + column_step])
    return (row, column), neighborhood, sum(neighborhood)


def next_generation(gen, ignore_borders=True):
    """
    Calculates the next generation of cells based on the state of the
    current generation
    """
    # gen_next = gen[:]  # not work
    # gen_next = list(gen)  # not work
    gen_next = []
    for row in range(len(gen)):
        gen_next.append(gen[row][:])  # it's work
        for column in range(len(gen[row])):
            # print(find_neighborhood(row, column, gen))
            # life_count = find_neighborhood_unlim(row, column, gen)[2]
            life_count = find_neighborhood(
                row, column, gen, ignore_borders=ignore_borders)[2]
            # TODO: refactor ifs
            if gen[row][column] == 1 and life_count in (2, 3):
                # stay alive
                pass
            if gen[row][column] == 0 and life_count == 3:
                # born
                gen_next[row][column] = 1
            if gen[row][column] == 1 and (life_count <= 1 or life_count >= 4):
                # die
                gen_next[row][column] = 0
        # print('---now--->', gen[row])
        # print('---new--->', gen_next[row])
    # TODO: convert to generator with yield
    return gen_next


def show_generations(current_generation=[], number_of_gen=1):
    """
    Displays the specified number of generations
    """
    clear_screen()
    for current_gen_number in range(number_of_gen):
        current_generation = next_generation(current_generation)
        for line in current_generation:
            print(''.join(map(str, line))
                  .replace('0', '.')
                  .replace('1', 'O'))
        print('generation #', current_gen_number + 1)
        time.sleep(0.5)
        if current_gen_number != number_of_gen - 1:
            clear_screen()
            # TODO: how to clear screen in PyCharm terminal?
            # it works only 4 Linux terminal
            # cursor_up_and_home = "\033[F"
            # cursor_down = "\033[B"
            # print(cursor_up_and_home * (len(current_generation) + 1), end='')
    # print(cursor_down * (len(current_generation) + 1))


def make_playground(columns, lines):
    """
    Generate empty playground for cells
    """
    return [[0 for column in range(columns)] for line in range(lines)]


def scatter_life(playground):
    """
    Randomly scatters cells on a all playground
    """
    for line in range(len(playground)):
        for column in range(len(playground[line])):
            playground[line][column] = randrange(2)
        # print(''.join(map(str, playground[line]))
        #       .replace('1', 'O')
        #       .replace('0', '.'))
    # time.sleep(1)
    return playground


def str_2_list_playground(str_playground):
    """
    Convert string representation of first generation pattern into list
    """
    list_playground = str_playground.strip().split('\n')
    list_playground = list(
        map(lambda line: list(line.replace('.', '0').replace('O', '1')),
            list_playground))
    list_playground = map(lambda line: [int(sign) for sign in line],
                          list_playground)
    # for line in list_playground:
    #     print(line)
    return list(list_playground)


def insert_pattern(playground, x, y):
    # TODO: insert some pattern into the playground from a given
    #   position (x, y) adding the missing pad sizes if needs
    pass


if __name__ == "__main__":
    # TODO_done: move start generations in a file
    # LWSS_gen = str_2_list_playground(LWSS_raw)
    # show_generations(LWSS_gen, 100)
    pulsar_gen = str_2_list_playground(pulsar_raw)
    show_generations(pulsar_gen, 99)
    # glider_gun_gen_0 = str_2_list_playground(glider_gun_raw)
    # show_generations(glider_gun_gen_0, 500)
    # gen_0 = scatter_life(make_playground(20, 5))
    # show_generations(gen_0, 100)
