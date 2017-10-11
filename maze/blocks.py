'''
Basic building blocks of a maze.
'''

NORTH   = 'N'
EAST    = 'E'
SOUTH   = 'S'
WEST    = 'W'

class Wall:
    '''
    Implements a wall of a maze cell.
    A wall can be set or cleared. It can  also be locked to
    prevent changing its state or unlocked to make set and
    clear operations work again.
    '''
    def __init__(self, state = False, locked = False):
        self._state = state
        self.locked = locked
        self._adjacent_cells = []

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if not self.locked:
            self._state = value

    def bind(self, *cells):
        for cell in cells:
            if len(self._adjacent_cells) < 2:
                self._adjacent_cells.append(cell)

    def get_neighbour(self, cell):
        if cell not in self._adjacent_cells:
            return None
        for adjacent in self._adjacent_cells:
            if cell != adjacent:
                return adjacent


class Cell:
    def __init__(self, north = None, east = None, south = None, west = None):
        self.__walls = {NORTH: north, EAST: east, SOUTH: south, WEST: west}
        for wall in self.__walls.values():
            try:
                wall.bind(self)
            except AttributeError:
                pass

    def get_neighbour(self, direction):
        try:
            return self.__walls[direction].get_neighbour(self)
        except AttributeError:
            return None

    def is_wall(self, direction):
        try:
            return self.__walls[direction].state
        except AttributeError:
            return False

