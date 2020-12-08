
def find2020(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                if list[i] + list[j] + list[k] == 2020:
                    print(list[i] * list[j] * list[k])


if __name__ == '__main__':
    with open("test2.txt") as file:
        find2020([int(a) for a in file.read().splitlines()])
