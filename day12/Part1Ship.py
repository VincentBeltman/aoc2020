class Ship:
    class Direction:
        EAST = 0
        SOUTH = 1
        WEST = 2
        NORTH = 3

    _multipliers = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def _get_multiplier(self, direction):
        return self._multipliers[direction]

    def __init__(self):
        self._direction = self.Direction.EAST
        self._x = 0
        self._y = 0

    def __str__(self):
        return "Ship is at (" + str(self._x) + ", " + str(self._y) + ") facing " + str(self._direction)

    def rotate_right(self, degrees):
        for _ in range(0, int(degrees/90)):
            self._direction = self._direction + 1 if self._direction < self.Direction.NORTH else self.Direction.EAST

    def rotate_left(self, degrees):
        for _ in range(0, int(degrees/90)):
            self._direction = self._direction - 1 if self._direction > self.Direction.EAST else self.Direction.NORTH

    def _move(self, ticks, direction):
        x_mul, y_mul = self._multipliers[direction]
        self._x += ticks * x_mul
        self._y += ticks * y_mul

    def forward(self, ticks):
        self._move(ticks, self._direction)

    def move_east(self, ticks):
        self._move(ticks, self.Direction.EAST)

    def move_south(self, ticks):
        self._move(ticks, self.Direction.SOUTH)

    def move_west(self, ticks):
        self._move(ticks, self.Direction.WEST)

    def move_north(self, ticks):
        self._move(ticks, self.Direction.NORTH)

    def get_manhatten_distance(self):
        return abs(self._x) + abs(self._y)
