from Part2Ship import Ship


class Instruction:
    def __init__(self, raw):
        self.action = raw[0]
        self.value = int(raw[1:])


class Captain:
    _actions = {
        "N": Ship.move_waypoint_north,
        "S": Ship.move_waypoint_south,
        "E": Ship.move_waypoint_east,
        "W": Ship.move_waypoint_west,
        "L": Ship.rotate_left,
        "R": Ship.rotate_right,
        "F": Ship.forward
    }

    def __init__(self):
        self._ship = Ship()
        self._instructions = []

    def set_instructions(self, raw_instructions):
        self._instructions = [Instruction(instruction) for instruction in raw_instructions]

    def navigate(self):
        for instruction in self._instructions:
            self._actions[instruction.action](self._ship, instruction.value)
            print(self._ship)
        return self._ship.get_manhatten_distance()
