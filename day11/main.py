def print_map_part1(seats):
    print("")
    for line in seats:
        print("".join(line))


def get_neighbours_part_1(x, y, max_x, max_y):
    neighbours = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    return [(x, y) for x, y in neighbours if 0 <= x <= max_x and 0 <= y <= max_y]


def maps_are_equal_part1(a, b):
    for y in range(0, len(a)):
        for x in range(0, len(a[y])):
            if a[y][x] != b[y][x]:
                return False
    return True


def count_occupied_seats_part1(seats):
    nr_of_occupied_seats = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                nr_of_occupied_seats += 1
    return nr_of_occupied_seats


def part_1_iterate(seats):
    tmp = []
    max_y = len(seats) - 1
    max_x = len(seats[0]) - 1
    for y in range(0, len(seats)):
        row = seats[y]
        tmp.append(row[:])
        for x in range(0, len(row)):
            if seats[y][x] != '.':
                nrOfOccupied = 0
                for n_x, n_y in get_neighbours_part_1(x, y, max_x, max_y):
                    if seats[n_y][n_x] == '#':
                        nrOfOccupied += 1
                if nrOfOccupied == 0:
                    tmp[y][x] = '#'
                elif nrOfOccupied >= 4:
                    tmp[y][x] = 'L'
    return tmp


def part_1(seats):
    print_map_part1(seats)
    i = 0
    while True:
        tmp = part_1_iterate(seats)
        if maps_are_equal_part1(seats, tmp):
            print_map_part1(seats)
            nr_of_occupied_seats = count_occupied_seats_part1(seats)
            print(i, nr_of_occupied_seats)
            break
        seats = tmp
        i += 1
        print(i)


def part_2_iterate(seats):
    tmp = []
    for y in range(0, len(seats)):
        row = seats[y]
        tmp.append([])
        for x in range(0, len(row)):
            tmp[y].append({"content": seats[y][x]["content"], "neighbours": seats[y][x]["neighbours"]})
            if seats[y][x]["content"] != '.':
                nrOfOccupied = 0
                for n_x, n_y in seats[y][x]["neighbours"]:
                    if seats[n_y][n_x]['content'] == '#':
                        nrOfOccupied += 1
                if nrOfOccupied == 0:
                    tmp[y][x]["content"] = '#'
                elif nrOfOccupied >= 5:
                    tmp[y][x]['content'] = 'L'
    return tmp


def find_first_visible_neighbour(seats, x, y, x_dir, y_dir):
    x += x_dir
    y += y_dir
    if 0 <= x <= (len(seats[0]) - 1) and 0 <= y <= (len(seats) - 1):
        if seats[y][x] != '.':
            return x, y
        else:
            return find_first_visible_neighbour(seats, x, y, x_dir, y_dir)
    else:
        return -1, -1


def maps_are_equal_part2(a, b):
    for y in range(0, len(a)):
        for x in range(0, len(a[y])):
            if a[y][x]["content"] != b[y][x]["content"]:
                return False
    return True


def count_occupied_seats_part2(seats):
    nr_of_occupied_seats = 0
    for row in seats:
        for seat in row:
            if seat["content"] == '#':
                nr_of_occupied_seats += 1
    return nr_of_occupied_seats


def parse_neighbours(seats):
    result = []
    for y in range(0, len(seats)):
        row = []
        for x in range(0, len(seats[0])):
            neighbours = [(n_x, n_y) for n_x, n_y in [
                                find_first_visible_neighbour(seats, x, y, -1, -1),
                                find_first_visible_neighbour(seats, x, y, -1, 1),
                                find_first_visible_neighbour(seats, x, y, 0, -1),
                                find_first_visible_neighbour(seats, x, y, 0, 1),
                                find_first_visible_neighbour(seats, x, y, -1, 0),
                                find_first_visible_neighbour(seats, x, y, 1, -1),
                                find_first_visible_neighbour(seats, x, y, 1, 0),
                                find_first_visible_neighbour(seats, x, y, 1, 1)]
                          if n_x >= 0 and n_y >= 0]
            row.append({"content": seats[y][x], "neighbours": neighbours})
        result.append(row)
    return result


def print_map_part2(seats):
    print("")
    for line in seats:
        print("".join([item["content"] for item in line]))


def part_2(seats):
    seats = parse_neighbours(seats)
    i = 0
    while True:
        print_map_part2(seats)
        tmp = part_2_iterate(seats)
        if maps_are_equal_part2(seats, tmp):
            nr_of_occupied_seats = count_occupied_seats_part2(seats)
            print(i, nr_of_occupied_seats)
            break
        seats = tmp
        i += 1
        print(i)


def execute(filename):
    with open(filename) as file:
        seats = []
        for line in file.read().splitlines():
            seats.append([a for a in line])
        part_2(seats)


if __name__ == '__main__':
    execute("test2.txt")
