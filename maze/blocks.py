'''
Basic building blocks of a maze.
'''

class Wall():
    '''
    Implements a wall of a maze cell.
    A wall can be set or cleared. It can  also be locked to
    prevent changing its state or unlocked to make set and
    clear operations work again.
    '''
    def __init__(self, is_set=False, is_locked=False):
        self.__is_set = is_set
        self.is_locked = is_locked
        self.__adjacent_cells = ()

    def set_or_clear(self, is_set):
        if self.is_locked is not True:
            self.__is_set = is_set
    def get(self):
        return self.__is_set
    is_set = property(get, set_or_clear)

    def bind(self, *cells):
        self.__adjacent_cells = cells[0:2]

    def get_neighbour(self, cell):
        if cell not in self.__adjacent_cells:
            return None
        for adjacent in self.__adjacent_cells:
            if cell != adjacent:
                return adjacent
    def get_adjacent_cells(self):
        return self.__adjacent_cells
    adjacent_cells = property(get_adjacent_cells, None)

