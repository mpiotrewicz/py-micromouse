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
        self.assertTrue(wall.adjacent_cells == ['cell1'])
        wall.bind('cell2', 'cell3', 'cell4')
        self.assertEqual(2, len(wall.adjacent_cells))
        self.assertTrue(wall.adjacent_cells == ['cell1', 'cell2'])
        wall.bind('cell5', 'cell6')
        self.assertEqual(2, len(wall.adjacent_cells))
        self.assertTrue(wall.adjacent_cells == ['cell1', 'cell2'])

    def test_get_neighbour(self):
        wall = maze.blocks.Wall()
        self.assertEqual(None, wall.get_neighbour('cell1'))
        self.assertEqual(None, wall.get_neighbour('cell2'))
        wall.bind('cell1')
        self.assertEqual(None, wall.get_neighbour('cell1'))
        wall.bind('cell2')
        self.assertEqual('cell2', wall.get_neighbour('cell1'))
        self.assertEqual('cell1', wall.get_neighbour('cell2'))

class CellTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Setup all tests to work on the following setup of cells and walls:
        +------+
        |      |
        |  c2  |
        |      |
        +--w1--+------+
        |      |      |
        |  c1  w2 c3  |
        |      |      |
        +------+------+
        '''
        self.wall1 = maze.blocks.Wall()
        self.wall2 = maze.blocks.Wall()
        self.cell1 = maze.blocks.Cell(north = self.wall1, east = self.wall2)
        self.cell2 = maze.blocks.Cell(south = self.wall1)
        self.cell3 = maze.blocks.Cell(west = self.wall2)
        self.assertTrue(self.cell2 == self.wall1.get_neighbour(self.cell1))
        self.assertTrue(self.cell1 == self.wall1.get_neighbour(self.cell2))
        self.assertTrue(self.cell1 == self.wall2.get_neighbour(self.cell3))
        self.assertTrue(self.cell3 == self.wall2.get_neighbour(self.cell1))

    def tearDown(self):
        pass

    def test_get_neighbour(self):
        self.assertTrue(self.cell2 == self.cell1.get_neighbour(maze.blocks.NORTH))
        self.assertTrue(self.cell3 == self.cell1.get_neighbour(maze.blocks.EAST))
        self.assertTrue(None == self.cell1.get_neighbour(maze.blocks.SOUTH))
        self.assertTrue(None == self.cell1.get_neighbour(maze.blocks.WEST))

        self.assertTrue(None == self.cell2.get_neighbour(maze.blocks.NORTH))
        self.assertTrue(None == self.cell2.get_neighbour(maze.blocks.EAST))
        self.assertTrue(self.cell1 == self.cell2.get_neighbour(maze.blocks.SOUTH))
        self.assertTrue(None == self.cell2.get_neighbour(maze.blocks.WEST))

        self.assertTrue(None == self.cell3.get_neighbour(maze.blocks.NORTH))
        self.assertTrue(None == self.cell3.get_neighbour(maze.blocks.EAST))
        self.assertTrue(None == self.cell3.get_neighbour(maze.blocks.SOUTH))
        self.assertTrue(self.cell1 == self.cell3.get_neighbour(maze.blocks.WEST))

    def test_get_wall(self):
        self.wall1.is_set = True

        self.assertTrue(self.cell1.get_wall(maze.blocks.NORTH))
        self.assertFalse(self.cell1.get_wall(maze.blocks.EAST))
        self.assertFalse(self.cell1.get_wall(maze.blocks.SOUTH))
        self.assertFalse(self.cell1.get_wall(maze.blocks.WEST))

        self.assertFalse(self.cell2.get_wall(maze.blocks.NORTH))
        self.assertFalse(self.cell2.get_wall(maze.blocks.EAST))
        self.assertTrue(self.cell2.get_wall(maze.blocks.SOUTH))
        self.assertFalse(self.cell2.get_wall(maze.blocks.WEST))

        self.assertFalse(self.cell3.get_wall(maze.blocks.NORTH))
        self.assertFalse(self.cell3.get_wall(maze.blocks.EAST))
        self.assertFalse(self.cell3.get_wall(maze.blocks.SOUTH))
        self.assertFalse(self.cell3.get_wall(maze.blocks.WEST))

if __name__ == '__main__': unittest.main()

