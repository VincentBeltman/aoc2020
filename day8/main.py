from Interpreter import Interpreter, InfiniteLoopException


def part1(raw_instructions):
    interpreter = Interpreter(raw_instructions)
    try:
        interpreter.run()
    except InfiniteLoopException:
        print(interpreter.get_accumulator())


def part2(raw_instructions):
    interpreter = Interpreter(raw_instructions)
    i = 0
    previous_operation = "acc"
    instruction_set = interpreter.get_instruction_set()
    while True:
        try:
            # interpreter.print()
            interpreter.run()
            break
        except InfiniteLoopException:
            if previous_operation != "acc":
                instruction_set[i].set_operation(previous_operation)
            i += 1
            while instruction_set[i].get_operation() == "acc":
                i += 1
            previous_operation = instruction_set[i].get_operation()
            instruction_set[i].set_operation("jmp" if previous_operation == "nop" else "nop")
    print(interpreter.get_accumulator())


if __name__ == '__main__':
    with open("test2.txt") as file:
        lines = file.read().splitlines()
        part2(lines)

