#!/usr/bin/python3

import unittest
from maze_wall import MazeWall

class WallTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWallSetClear(self):
        wall = MazeWall()
        wall.set()
        self.assertTrue(wall.is_set(), 'Failed to set the wall')
        wall.clear()
        self.assertTrue(not wall.is_set(), 'Failed to clear the wall')

    def testWallLockUnlock(self):
        wall = MazeWall()
        wall.clear()
        wall.lock()
        self.assertTrue(wall.is_locked(), 'Failed to lock the wall')
        wall.set()
        self.assertTrue(not wall.is_set(), 'The wall is not locked')
        wall.unlock()
        self.assertTrue(not wall.is_locked(), 'Failed to unlock the wall')
        wall.set()
        self.assertTrue(wall.is_set(), 'The wall is not unlocked')
        wall.clear()

if __name__ == '__main__': unittest.main()

