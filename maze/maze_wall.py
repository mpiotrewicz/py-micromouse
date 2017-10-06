class MazeWall():
    '''
    Implements a wall of a maze cell.
    A wall can be set or cleared. It can  also be locked to
    prevent it from being altered (set or cleared) or unlocked
    to re-enable set/clear operations.
    '''

    def __init__(self, wall=False, locked=False):
        self.__wall = wall
        self.__locked = locked

    def set(self):
        if self.__locked is not True:
            self.__wall = True

    def clear(self):
        if self.__locked is not True:
            self.__wall = False

    def is_set(self):
        return self.__wall

    def lock(self):
        self.__locked = True

    def unlock(self):
        self.__locked = False

    def is_locked(self):
        return self.__locked

