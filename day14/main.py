def part1(raw):
    memory = {}
    mask = ['X'] * 36
    for line in raw:
        name, value = line.split(' = ')
        if name == 'mask':
            mask = [char for char in value]
            mask.reverse()
        else:
            masked_value = int(value)
            for i, bit in enumerate(mask):
                if bit == '1':
                    masked_value |= (1 << i)
                elif bit == '0':
                    masked_value &= ~(1 << i)
            memory[int(name[4:-1])] = masked_value
    total = 0
    for address, value in memory.items():
        total += value
    print(total)


def part2(raw):
    memory = {}
    address_mask = ['0'] * 36
    for line in raw:
        name, value = line.split(' = ')
        if name == 'mask':
            address_mask = [char for char in value]
            address_mask.reverse()
        else:
            masked_address = int(name[4:-1])
            for i, bit in enumerate(address_mask):
                if bit == '1':
                    masked_address |= (1 << i)
            addresses = [masked_address]
            for i, bit in enumerate(address_mask):
                if bit == 'X':
                    extension = []
                    for j, address in enumerate(addresses):
                        addresses[j] = address | (1 << i)
                        extension.append(address & ~(1 << i))
                    addresses.extend(extension)
            for address in addresses:
                memory[address] = int(value)
    total = 0
    for address, value in memory.items():
        total += value
    print(total)


if __name__ == '__main__':
    with open("test2.txt") as file:
        lines = file.read().splitlines()
        part2(lines)
