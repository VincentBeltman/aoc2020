import re
from Graph import Graph


def parse_rules(raw_rules):
    graph = Graph()
    for raw_rule in raw_rules:
        match = re.match(r"^([a-z ]+) bags contain ([a-z0-9 ,]+).$", raw_rule)
        assert(match is not None)
        root_bag_name = match.group(1)
        graph.add_vertex(root_bag_name)
        contains = match.group(2)
        for bag in contains.split(", "):
            if bag != "no other bags":
                bag_match = re.match(r"(\d) ([a-z ]+) bags?", bag)
                assert(bag_match is not None)
                graph.add_edge(root_bag_name, bag_match.group(2), int(bag_match.group(1)))
    return graph


def get_parent_nodes(vertex):
    parent_nodes = []
    for connection in vertex.get_upstream_connections():
        parent_nodes.append(connection)
        parent_nodes.extend(get_parent_nodes(connection))
    return set(parent_nodes)


def part1(rules):
    part1_result = get_parent_nodes(rules.get_vertex("shiny gold"))
    print(len(part1_result))


def count_downstream_bags(vertex):
    nr_of_bags = 1
    for connection in vertex.get_downstream_connections():
        tmp = count_downstream_bags(connection)
        print(connection, vertex.get_weight(connection), tmp)
        nr_of_bags += vertex.get_weight(connection) * count_downstream_bags(connection)
    return nr_of_bags


def part2(rules):
    print(count_downstream_bags(rules.get_vertex("shiny gold")) - 1)  # -1 for shiny gold


if __name__ == '__main__':
    with open("test2.txt") as file:
        result = parse_rules(file.read().splitlines())
        part1(result)
        part2(result)
