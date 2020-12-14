class Ship:
    def __init__(self):
        self._waypoint = (10, -1)
        self._x = 0
        self._y = 0

    def __str__(self):
        return "Ship is at (" + str(self._x) + ", " + str(self._y) + ") waypoint: " + str(self._waypoint)

    def rotate_right(self, degrees):
        for _ in range(0, int(degrees/90)):
            x, y = self._waypoint
            self._waypoint = (-y, x)

    def rotate_left(self, degrees):
        for _ in range(0, int(degrees/90)):
            x, y = self._waypoint
            self._waypoint = (y, -x)

    def forward(self, ticks):
        x, y = self._waypoint
        self._x += ticks * x
        self._y += ticks * y

    def move_waypoint_east(self, ticks):
        x, y = self._waypoint
        self._waypoint = (x + ticks, y)

    def move_waypoint_south(self, ticks):
        x, y = self._waypoint
        self._waypoint = (x, y + ticks)

    def move_waypoint_west(self, ticks):
        x, y = self._waypoint
        self._waypoint = (x - ticks, y)

    def move_waypoint_north(self, ticks):
        x, y = self._waypoint
        self._waypoint = (x, y - ticks)

    def get_manhatten_distance(self):
        return abs(self._x) + abs(self._y)
