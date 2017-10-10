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
    def __init__(self, is_set = False, is_locked = False):
        self.__is_set = is_set
        self.is_locked = is_locked
        self.__adjacent_cells = []

    def set_or_clear(self, is_set):
        if self.is_locked is not True:
            self.__is_set = is_set
    def get(self):
        return self.__is_set
    is_set = property(get, set_or_clear)

    def bind(self, *cells):
        for cell in cells:
            if len(self.__adjacent_cells) < 2:
                self.__adjacent_cells.append(cell)

    def get_neighbour(self, cell):
        if cell not in self.__adjacent_cells:
            return None
        for adjacent in self.__adjacent_cells:
            if cell != adjacent:
                return adjacent
    def get_adjacent_cells(self):
        return self.__adjacent_cells
    adjacent_cells = property(get_adjacent_cells, None)

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

    def get_wall(self, direction):
        try:
            return self.__walls[direction].is_set
        except AttributeError:
            return False

