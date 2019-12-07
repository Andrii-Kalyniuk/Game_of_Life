import time


def find_neighborhood(row, column, gen):
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


def next_generation(gen):
    # gen_next = gen[:]  # not work
    # gen_next = list(gen)  # not work
    gen_next = []
    for row in range(len(gen)):
        gen_next.append(gen[row][:])  # it's work
        for column in range(len(gen[row])):
            # print(find_neighborhood(row, column, gen))
            life_count = find_neighborhood(row, column, gen)[2]
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
    for _ in range(4):
        gen_0 = next_generation(gen_0)
        for line in gen_0:
            print(line)
        print('-' * 20, _ + 1)
        time.sleep(1)
