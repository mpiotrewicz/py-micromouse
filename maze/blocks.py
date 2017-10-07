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

    def set_or_clear(self, is_set):
        if self.is_locked is not True:
            self.__is_set = is_set
    def get(self):
        return self.__is_set
    is_set = property(get, set_or_clear)

