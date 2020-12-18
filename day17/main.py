import GridPart1
import GridPart2


def part1(iterations, filename):
    with open(filename) as file:
        grid = GridPart1.Grid(file.read())
        print(grid)
        for _ in range(0, iterations):
            grid.iterate()
            print(grid)
        print("Nr of active cubes:", grid.count_nr_of_active_cubes())


def part2(iterations, filename):
    with open(filename) as file:
        grid = GridPart2.Grid(file.read())
        # print(grid)
        for _ in range(0, iterations):
            grid.iterate()
            # print(grid)
        print("Nr of active cubes:", grid.count_nr_of_active_cubes())


if __name__ == '__main__':
    test = "test2.txt"
    # part1(1, test)
    # part1(2, test)
    # part1(3, test)
    # part1(4, test)
    # part1(5, test)
    # part1(6, test)
    part2(1, test)
    # part2(2, test)
    # part2(3, test)
    # part2(4, test)
    # part2(5, test)
    part2(6, test)
