from Graph import Graph, Vertex


def part_1(raw):
    sortedNumbers = [0]
    sortedNumbers.extend(sorted(raw))
    sortedNumbers.append(sortedNumbers[-1] + 3)
    nrOfOnes = 0
    nrOfThrees = 0
    for i in range(0, len(sortedNumbers) - 1):
        difference = sortedNumbers[i + 1] - sortedNumbers[i]
        if difference == 1:
            nrOfOnes += 1
        elif difference == 3:
            nrOfThrees += 1
        else:
            assert False
    print(len(sortedNumbers), nrOfOnes, nrOfThrees, nrOfOnes * nrOfThrees)


def find_total(cache, from_vertex: Vertex, to_vertex: Vertex):
    total = 0
    if from_vertex in cache:
        total = cache[from_vertex]
    else:
        for connection in from_vertex.get_downstream_connections():
            if connection == to_vertex:
                total += 1
            else:
                total += find_total(cache, connection, to_vertex)
        cache[from_vertex] = total
    return total


def part_2(raw):
    sortedNumbers = [0]
    sortedNumbers.extend(sorted(raw))
    end = sortedNumbers[-1] + 3
    sortedNumbers.append(end)
    print(sortedNumbers)
    graph = Graph()
    for i in range(0, len(sortedNumbers) - 1):
        graph.add_vertex(sortedNumbers[i])
        for j in range(i+1, len(sortedNumbers)):
            if sortedNumbers[j] - sortedNumbers[i] <= 3:
                graph.add_edge(sortedNumbers[i], sortedNumbers[j])
            else:
                break
    print(find_total({}, graph.get_vertex(0), graph.get_vertex(end)))


if __name__ == '__main__':
    with open("test2.txt") as file:
        numbers = [int(a) for a in file.read().splitlines()]
        # part_1(numbers)
        part_2(numbers)
