import typing


def main(tomato_grid: typing.List[typing.List[int]]):
    # START WRITING CODE HERE
    pass


if __name__ == "__main__":
    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [1, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    assert (main(tomato_grid) == 2), "Tomatoes will be rotten in 2 days"

    tomato_grid = [
        [-1, 1, 0, -1, 1],
        [0, 0, 1, -1, 1],
        [1, 0, 0, -1, 1],
    ]
    assert (main(tomato_grid) == -1), "All tomatoes cannot be rotten"
