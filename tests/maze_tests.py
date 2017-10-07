#!/usr/bin/python3

import unittest
import context
import maze.blocks

class WallTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWallSetClear(self):
        wall = maze.blocks.Wall()
        wall.is_set = True
        self.assertTrue(wall.is_set, 'Failed to set the wall')
        wall.is_set = False
        self.assertTrue(not wall.is_set, 'Failed to clear the wall')

    def testWallLockUnlock(self):
        wall = maze.blocks.Wall()
        wall.is_locked = True
        wall.is_set = True
        self.assertTrue(not wall.is_set, 'The wall is not locked')
        wall.is_locked = False
        wall.is_set = True
        self.assertTrue(wall.is_set, 'The wall is not unlocked')

if __name__ == '__main__': unittest.main()

