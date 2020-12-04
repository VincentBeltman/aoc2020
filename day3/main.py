TREE = '#'
EMPTY = '.'


def parse_forrest(blob):
    forrest = []
    for line in blob.splitlines():
        row = []
        for char in line:
            row.append(char)
        forrest.append(row)
    return forrest


def tree_at(x, y, forrest):
    return forrest[y][x % len(forrest[0])] == TREE


def count_trees_till_bottom(steps_right, steps_down, forrest):
    pos = (0, 0)
    nrOfTrees = 0

    for i in range(0, len(forrest), steps_down):
        x, y = pos

        if tree_at(x, y, forrest):
            nrOfTrees += 1

        pos = (x + steps_right, y + steps_down)
    return nrOfTrees


if __name__ == "__main__":
    with open("test2.txt") as file:
        parsedForrest = parse_forrest(file.read())
        first = count_trees_till_bottom(1, 1, parsedForrest)
        second = count_trees_till_bottom(3, 1, parsedForrest)
        third = count_trees_till_bottom(5, 1, parsedForrest)
        fourth = count_trees_till_bottom(7, 1, parsedForrest)
        fifth = count_trees_till_bottom(1, 2, parsedForrest)

        print(first, second, third, fourth, fifth, first * second * third * fourth * fifth)
