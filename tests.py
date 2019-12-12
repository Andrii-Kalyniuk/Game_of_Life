from life import find_neighborhood, next_generation


def test_find_neighborhood():
    gen = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_0 = [8, 2, 6, 4, 9, 3, 1, 7]
    expected_1 = [5, 3, 1, 6, 4]
    expected_2 = [4, 8, 5]
    expected_3 = [6, 8, 5]
    assert expected_0 == find_neighborhood(1, 1, gen)[1]
    assert expected_1 == find_neighborhood(0, 1, gen)[1]
    assert expected_2 == find_neighborhood(2, 0, gen)[1]
    assert expected_3 == find_neighborhood(2, 2, gen)[1]


def test_next_generation():
    gen_0 = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    expected_1 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    expected_2 = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert expected_1 == next_generation(gen_0)
    assert expected_2 == next_generation(expected_1)


def test_next_generation_glider():
    gen_0 = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    expected_4th_gen = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    gen = gen_0
    for _ in range(1, 4):
        gen = next_generation(gen)
    assert expected_4th_gen == next_generation(gen)
