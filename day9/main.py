def part_1(numbers, preamble_length):
    for i in range(preamble_length, len(numbers)):
        valid = False
        for j in range(i-preamble_length, i-1):
            for k in range(j+1, i):
                if numbers[j] + numbers[k] == numbers[i]:
                    valid = True
                    break
            if valid:
                break

        if not valid:
            return numbers[i]
    assert False


def part_2(numbers, number_to_find):
    for i in range(0, len(numbers)):
        total = 0
        for j in range(i, len(numbers)):
            total += numbers[j]
            if total == number_to_find:
                return numbers[i:j+1]
            elif total > number_to_find:
                break
    assert False


if __name__ == '__main__':
    with open("test2.txt") as file:
        raw = [int(line) for line in file.read().splitlines()]
        weakness = part_1(raw, 25)
        print(weakness)
        contiguous_set = part_2(raw, weakness)
        print(contiguous_set, min(contiguous_set) + max(contiguous_set))
