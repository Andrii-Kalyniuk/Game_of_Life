import os
import time
from random import randrange

from generation_zero_patterns import (lwss_raw,
                                      pulsar_raw,
                                      glider_gun_raw,
                                      fuse_raw,
                                      glider_raw, python_raw,
                                      ff_force_field_raw)


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
    # TODO: remove row, columns, neighborhood
    return (row, column), neighborhood, sum(neighborhood)


def next_generation(gen, ignore_borders=True):
    """
    Calculates the next generation of cells based on the state of the
    current generation
    """
    gen_next = []
    for row in range(len(gen)):
        gen_next.append(gen[row][:])
        for column in range(len(gen[row])):
            life_count = find_neighborhood(
                row, column, gen, ignore_borders=ignore_borders)[2]
            if gen[row][column] == 0 and life_count == 3:
                # born
                gen_next[row][column] = 1
            if gen[row][column] == 1 and (life_count <= 1 or life_count >= 4):
                # die
                gen_next[row][column] = 0
    # TODO: convert to generator with yield
    return gen_next


def list_playground_2_str(list_playground, print_it=False):
    """
    Convert list representation of generation pattern into string
    """
    str_playground = ''
    for line in list_playground:
        str_playground = f"{str_playground}</br>\n{''.join(map(str, line))}"
    str_playground = str_playground.replace('0', '.').replace('1', 'O')
    if print_it:
        print(str_playground.replace('</br>', ''))
    return str_playground


def show_generations(current_generation=[], number_of_gen=1,
                     ignore_borders=True, respawn=False):
    """
    Displays the specified number of generations
    """
    # prev_generation = current_generation.copy()
    clear_screen()
    for current_gen_number in range(number_of_gen):
        current_generation = next_generation(current_generation,
                                             ignore_borders=ignore_borders)
        list_playground_2_str(current_generation, print_it=True)
        print('generation #', current_gen_number + 1)
        time.sleep(0.25)
        if current_gen_number != number_of_gen - 1:
            clear_screen()
        # TODO: scatter_life if gen died or prev_gen == cur_gen
        # if respawn:
        # if prev_generation == current_generation:
        #     columns, lines = (len(line), len(current_generation))
        #     new_generation = scatter_life(make_playground(columns, lines))
        #     show_generations(new_generation, number_of_gen=number_of_gen,
        #                      ignore_borders=ignore_borders,
        #                      respawn=respawn)
        # TODO: how to clear screen in PyCharm terminal?
        # it works only 4 Linux terminal
        # cursor_up_and_home = "\033[F"
        # cursor_down = "\033[B"
        # print(cursor_up_and_home * (len(current_generation) + 1), end='')
    # print(cursor_down * (len(current_generation) + 1))
    return list_playground_2_str(current_generation)


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
    #DEBUG
    # list_playground_2_str(playground, print_it=True)
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


def extend_playground(pattern, lines=0, columns=0,
                      lines_before=0, cols_before=0):
    """
    Add given numbers of empty lines and empty columns before and after
     every line and column of the playground
    """
    for line in range(len(pattern)):
        pattern[line].extend([0 for _ in range(columns)])
        pattern[line] = [0 for _ in range(cols_before)] + pattern[line]
        if line == len(pattern) - 1:
            pattern.extend([[0 for _ in range(len(pattern[line]))]
                            for new_line in range(lines)])
    pattern = make_playground(columns=len(pattern[0]),
                              lines=lines_before) + pattern
    return pattern


def insert_pattern(playground, x, y):
    # TODO: insert some pattern into the playground from a given
    #   position (x, y) adding the missing pad sizes if needs
    pass


if __name__ == "__main__":
    # TODO_done: move start generations in a file

    # lwss_gen = str_2_list_playground(lwss_raw)
    # lwss_gen = extend_playground(lwss_gen,lines=2, columns=10,
    #                              cols_before=10)
    # show_generations(lwss_gen, 100)

    # pulsar_gen = str_2_list_playground(pulsar_raw)
    # show_generations(pulsar_gen, 99)

    # glider_gun_gen_0 = str_2_list_playground(glider_gun_raw)
    # glider_gun_gen_0 = extend_playground(glider_gun_gen_0, 10, 10, 10, 10)
    # show_generations(glider_gun_gen_0, 500)

    # fuse_gen = str_2_list_playground(fuse_raw)
    # fuse_gen = extend_playground(fuse_gen, columns=10, cols_before=10,
    #                              lines=10, lines_before=10)
    # show_generations(fuse_gen, 99)

    # python_gen = str_2_list_playground(python_raw)
    # python_gen = extend_playground(python_gen, 1, 1, 1, 1)
    # show_generations(python_gen, 99)

    # ff_force_field_gen = str_2_list_playground(ff_force_field_raw)
    # ff_force_field_gen = extend_playground(ff_force_field_gen,
    #                                        lines=5, columns=10,
    #                                        lines_before=5,
    #                                        cols_before=10)
    # show_generations(ff_force_field_gen, 99, ignore_borders=True)

    # glider_gen = str_2_list_playground(glider_raw)
    # glider_gen = extend_playground(glider_gen,
    #                                lines=1, columns=1,
    #                                lines_before=1, cols_before=1)
    # show_generations(glider_gen, 99, ignore_borders=True)

    gen_0 = scatter_life(make_playground(20, 5))
    show_generations(gen_0, 100, respawn=True)
