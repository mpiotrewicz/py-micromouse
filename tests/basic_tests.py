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
        wall.bind('cell1', 'cell2')
        self.assertEqual('cell2', wall.get_neighbour('cell1'))
        self.assertEqual('cell1', wall.get_neighbour('cell2'))

class CellTestCase(unittest.TestCase):
    def test_get_neighbour(self):
        '''
        Tests the following setup of cells and walls:
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
        wall1 = maze.blocks.Wall()
        wall2 = maze.blocks.Wall()
        cell1 = maze.blocks.Cell(north = wall1, east = wall2)
        cell2 = maze.blocks.Cell(south = wall1)
        cell3 = maze.blocks.Cell(west = wall2)

        self.assertTrue(cell2 == wall1.get_neighbour(cell1))
        self.assertTrue(cell1 == wall1.get_neighbour(cell2))
        self.assertTrue(cell1 == wall2.get_neighbour(cell3))
        self.assertTrue(cell3 == wall2.get_neighbour(cell1))

        self.assertTrue(cell2 == cell1.get_neighbour(maze.blocks.NORTH))
        self.assertTrue(cell3 == cell1.get_neighbour(maze.blocks.EAST))
        self.assertTrue(None == cell1.get_neighbour(maze.blocks.SOUTH))
        self.assertTrue(None == cell1.get_neighbour(maze.blocks.WEST))

        self.assertTrue(None == cell2.get_neighbour(maze.blocks.NORTH))
        self.assertTrue(None == cell2.get_neighbour(maze.blocks.EAST))
        self.assertTrue(cell1 == cell2.get_neighbour(maze.blocks.SOUTH))
        self.assertTrue(None == cell2.get_neighbour(maze.blocks.WEST))

        self.assertTrue(None == cell3.get_neighbour(maze.blocks.NORTH))
        self.assertTrue(None == cell3.get_neighbour(maze.blocks.EAST))
        self.assertTrue(None == cell3.get_neighbour(maze.blocks.SOUTH))
        self.assertTrue(cell1 == cell3.get_neighbour(maze.blocks.WEST))

if __name__ == '__main__': unittest.main()

