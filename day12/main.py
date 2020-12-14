from Part2Captain import Captain


if __name__ == '__main__':
    with open("test2.txt") as file:
        captain = Captain()
        captain.set_instructions(file.read().splitlines())
        end = captain.navigate()
        print("Manhatten distance", end)

