#!/usr/bin/python3

import unittest
import context
import maze.blocks

class WallTestCase(unittest.TestCase):
    def test_set_clear(self):
        wall = maze.blocks.Wall()
        wall.is_set = True
        self.assertTrue(wall.is_set, 'Failed to set the wall')
        wall.is_set = False
        self.assertTrue(not wall.is_set, 'Failed to clear the wall')

    def test_lock_unlock(self):
        wall = maze.blocks.Wall()
        wall.is_locked = True
        wall.is_set = True
        self.assertTrue(not wall.is_set, 'The wall is not locked')
        wall.is_locked = False
        wall.is_set = True
        self.assertTrue(wall.is_set, 'The wall is not unlocked')

    def test_bind(self):
        wall = maze.blocks.Wall()
        self.assertEqual(0, len(wall.adjacent_cells))
        wall.bind('cell1')
        self.assertEqual(1, len(wall.adjacent_cells))
        self.assertTrue(wall.adjacent_cells == ('cell1',))
        wall.bind('cell1', 'cell2')
        self.assertEqual(2, len(wall.adjacent_cells))
        self.assertTrue(wall.adjacent_cells == ('cell1', 'cell2'))
        wall.bind('cell1', 'cell2', 'cell3')
        self.assertEqual(2, len(wall.adjacent_cells))
        self.assertTrue(wall.adjacent_cells == ('cell1', 'cell2'))

    def test_get_neighbour(self):
        wall = maze.blocks.Wall()
        self.assertEqual(None, wall.get_neighbour('cell1'))
        self.assertEqual(None, wall.get_neighbour('cell2'))
        wall.bind('cell1', 'cell2')
        self.assertEqual('cell2', wall.get_neighbour('cell1'))
        self.assertEqual('cell1', wall.get_neighbour('cell2'))

if __name__ == '__main__': unittest.main()

