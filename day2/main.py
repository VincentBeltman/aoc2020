import re


def part1(lines):
    nrOfValidPasswords = 0
    for line in lines:
        match = re.match(r"(\d+)-(\d+)\s([a-z]):\s([a-z]+)", line)
        min_bound = int(match.group(1))
        max_bound = int(match.group(2))
        character = match.group(3)
        password = match.group(4)
        nrOfOccurrences = (len([place for place, letter in enumerate(password) if letter == character]))
        if min_bound <= nrOfOccurrences <= max_bound:
            nrOfValidPasswords += 1
    print(nrOfValidPasswords)


def part2(lines):
    nrOfValidPasswords = 0
    for line in lines:
        match = re.match(r"(\d+)-(\d+)\s([a-z]):\s([a-z]+)", line)
        pos1 = int(match.group(1))
        pos2 = int(match.group(2))
        character = match.group(3)
        password = match.group(4)
        if (password[pos1-1] == character) != (password[pos2-1] == character):
            nrOfValidPasswords += 1
    print(nrOfValidPasswords)


if __name__ == "__main__":
    with open("test2.txt") as file:
        # part1(file.read().splitlines())
        part2(file.read().splitlines())
