class InfiniteLoopException(Exception):
    pass


class Instruction:
    def __init__(self, operation_map, operation, argument):
        self._operation_map = operation_map
        self._operation = operation
        self._argument = argument
        self._is_executed = False

    def execute(self):
        # print("Executing", self._operation, self._argument)
        if self._is_executed:
            raise InfiniteLoopException
        self._operation_map[self._operation](self._argument)
        self._is_executed = True

    def get_operation(self):
        return self._operation

    def set_operation(self, new_operation):
        self._operation = new_operation

    def get_argument(self):
        return self._argument

    def set_argument(self, new_argument):
        self._argument = new_argument


class Interpreter:
    def __init__(self, instructions):
        self.operation_map = {
            "nop": self._nop,
            "jmp": self._jmp,
            "acc": self._acc
        }
        self._instructions = []
        for instruction in instructions:
            operation, argument = instruction.split(" ")
            self._instructions.append(Instruction(self.operation_map, operation, int(argument)))
        self._instructionPointer = 0
        self._accumulator = 0

    def reset(self):
        self._instructionPointer = 0
        self._accumulator = 0
        for instruction in self._instructions:
            instruction._is_executed = False

    def run(self):
        self.reset()
        while self._instructionPointer < len(self._instructions):
            self._instructions[self._instructionPointer].execute()

    def get_accumulator(self):
        return self._accumulator

    def get_instruction_set(self):
        return self._instructions

    def _nop(self, argument):
        self._instructionPointer += 1
        pass

    def _jmp(self, argument):
        self._instructionPointer += argument

    def _acc(self, argument):
        self._accumulator += argument
        self._instructionPointer += 1

    def print(self):
        print("----------- interpreter ----------")
        print("Accumulator:", self._accumulator)
        print("Instruction pointer:", self._instructionPointer)
        print("Instructions:")
        for instruction in self._instructions:
            print(" -", instruction.get_operation(), instruction.get_argument())
