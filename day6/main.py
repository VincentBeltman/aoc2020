def part1(blob):
    result = []
    for group in blob.split("\n\n"):
        questionnaire = [False] * 26
        for person in group.splitlines():
            for char in person:
                questionnaire[ord(char) - 97] += 1
        result.append(questionnaire)
    return result


def part2(blob):
    result = []
    for group in blob.split("\n\n"):
        counts = [0] * 26
        nrOfPersons = 0
        for person in group.splitlines():
            nrOfPersons += 1
            for char in person:
                counts[ord(char) - 97] += 1
        questionnaire = [False] * 26
        for i, count in enumerate(counts):
            if count is nrOfPersons:
                questionnaire[i] = True
        result.append(questionnaire)
    return result


def count_questions(groups):
    count = 0
    for group in parsed_groups:
        for question in group:
            if question:
                count += 1
    print(count)


if __name__ == '__main__':
    with open("test2.txt") as file:
        parsed_groups = part2(file.read())
        count_questions(parsed_groups)
