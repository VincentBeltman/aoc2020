class Grid:
    ACTIVE = '#'
    INACTIVE = '.'

    def __init__(self, raw):
        self._grid = {0: {0: {}}}
        lines = raw.splitlines()
        i = 0
        for line in lines:
            self._grid[0][0][i] = {}
            j = 0
            for cube in line:
                self._grid[0][0][i][j] = cube
                j += 1
            i += 1

    def __str__(self):
        result = ''
        for w, world in self._grid.items():
            for z, plain in world.items():
                result += "z=" + str(z) + " w=" + str(w) + "\n"
                for y, row in plain.items():
                    result += str(y) + ":\t" + "".join(row.values()) + "\n"
                result += "\n"
        return result

    def is_active(self, x, y, z, w):
        return w in self._grid and \
               z in self._grid[w] and \
               y in self._grid[w][z] and \
               x in self._grid[w][z][y] and \
               self._grid[w][z][y][x] == self.ACTIVE

    def iterate(self):
        new_grid = {}
        w_range = range(min(self._grid)-1, max(self._grid)+2)
        z_range = range(min(self._grid[0])-1, max(self._grid[0])+2)
        y_range = range(min(self._grid[0][0])-1, max(self._grid[0][0])+2)
        x_range = range(min(self._grid[0][0][0])-1, max(self._grid[0][0][0])+2)
        for w in w_range:
            new_grid[w] = {}
            for z in z_range:
                new_grid[w][z] = {}
                for y in y_range:
                    new_grid[w][z][y] = {}
                    for x in x_range:
                        nr_of_neighbours_on = self.count_nr_of_neighbours_on(x, y, z, w)
                        if 3 == nr_of_neighbours_on or (self.is_active(x, y, z, w) and 2 == nr_of_neighbours_on):
                            new_grid[w][z][y][x] = self.ACTIVE
                        else:
                            new_grid[w][z][y][x] = self.INACTIVE
        self._grid = new_grid

    def count_nr_of_neighbours_on(self, x, y, z, w):
        nr_of_neighbours_on = -1 if self.is_active(x, y, z, w) else 0
        for n_w in range(w-1, w+2):
            for n_z in range(z-1, z+2):
                for n_y in range(y-1, y+2):
                    for n_x in range(x-1, x+2):
                        if n_w in self._grid and \
                                n_z in self._grid[n_w] and \
                                n_y in self._grid[n_w][n_z] and \
                                n_x in self._grid[n_w][n_z][n_y]:
                            if self._grid[n_w][n_z][n_y][n_x] == self.ACTIVE:
                                nr_of_neighbours_on += 1
        return nr_of_neighbours_on

    def count_nr_of_active_cubes(self):
        result = 0
        for world in self._grid.values():
            for plain in world.values():
                for row in plain.values():
                    for cube in row.values():
                        if cube == self.ACTIVE:
                            result += 1
        return result

