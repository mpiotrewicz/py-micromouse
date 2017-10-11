#!/usr/bin/python3

import unittest
import context
import pprint
import maze.blocks

class WallTestCase(unittest.TestCase):
    def test_set_clear(self):
        wall = maze.blocks.Wall()
        wall.state = True
        self.assertTrue(wall.state, 'Failed to set the wall')
        wall.state = False
        self.assertFalse(wall.state, 'Failed to clear the wall')

    def test_lock_unlock(self):
        wall = maze.blocks.Wall()
        self.assertFalse(wall.locked)
        self.assertFalse(wall.state)
        wall.state = True
        self.assertTrue(wall.state)
        wall.state = False
        wall.locked = True
        wall.state = True
        self.assertFalse(wall.state, 'The wall is not locked')
        wall.locked = False
        wall.state = True
        self.assertTrue(wall.state, 'The wall is not unlocked')

    def test_bind(self):
        wall = maze.blocks.Wall()
        self.assertEqual(0, len(wall._adjacent_cells))
        wall.bind('cell1')
        self.assertEqual(1, len(wall._adjacent_cells))
        self.assertTrue(wall._adjacent_cells == ['cell1'])
        wall.bind('cell2', 'cell3', 'cell4')
        self.assertEqual(2, len(wall._adjacent_cells))
        self.assertTrue(wall._adjacent_cells == ['cell1', 'cell2'])
        wall.bind('cell5', 'cell6')
        self.assertEqual(2, len(wall._adjacent_cells))
        self.assertTrue(wall._adjacent_cells == ['cell1', 'cell2'])

    def test_adjacent(self):
        wall = maze.blocks.Wall()
        self.assertEqual(None, wall.adjacent('cell1'))
        self.assertEqual(None, wall.adjacent('cell2'))
        wall.bind('cell1')
        self.assertEqual(None, wall.adjacent('cell1'))
        wall.bind('cell2')
        self.assertEqual('cell2', wall.adjacent('cell1'))
        self.assertEqual('cell1', wall.adjacent('cell2'))

class CellTestCase(unittest.TestCase):
    def test_valid_cell(self):
        try:
            cell = maze.blocks.Cell(north   = maze.blocks.Wall(),
                                    east    = maze.blocks.Wall(),
                                    south   = maze.blocks.Wall(),
                                    west    = maze.blocks.Wall())
        except ValueError:
            self.assertTrue(False)

    def test_missing_wall(self):
        try:
            cell = maze.blocks.Cell(north   = maze.blocks.Wall(),
                                    east    = maze.blocks.Wall(),
                                    south   = None,
                                    west    = maze.blocks.Wall())
        except ValueError:
            pass
        else:
            self.assertTrue(False)

    def test_neighbour(self):
        rows = 2
        columns = 2
        cells = []

        for r in range(rows):
            cells.append([])

            for c in range(columns):
                if r == 0:
                    south_wall = maze.blocks.Wall()
                else:
                    south_wall = cells[r - 1][c].walls[maze.blocks.NORTH]

                if c == 0:
                    west_wall = maze.blocks.Wall()
                else:
                    west_wall = cells[r][c - 1].walls[maze.blocks.EAST]

                cells[r].append(maze.blocks.Cell(north = maze.blocks.Wall(),
                                          east  = maze.blocks.Wall(),
                                          south = south_wall,
                                          west  = west_wall))
        for row in cells:
            for cell in row:
                pprint.pprint(cell.walls)


#    def test_neighbour(self):
#        self.assertTrue(self.cell2 == self.cell1.neighbour(maze.blocks.NORTH))
#        self.assertTrue(self.cell3 == self.cell1.neighbour(maze.blocks.EAST))
#        self.assertTrue(None == self.cell1.neighbour(maze.blocks.SOUTH))
#        self.assertTrue(None == self.cell1.neighbour(maze.blocks.WEST))
#
#        self.assertTrue(None == self.cell2.neighbour(maze.blocks.NORTH))
#        self.assertTrue(None == self.cell2.neighbour(maze.blocks.EAST))
#        self.assertTrue(self.cell1 == self.cell2.neighbour(maze.blocks.SOUTH))
#        self.assertTrue(None == self.cell2.neighbour(maze.blocks.WEST))
#
#        self.assertTrue(None == self.cell3.neighbour(maze.blocks.NORTH))
#        self.assertTrue(None == self.cell3.neighbour(maze.blocks.EAST))
#        self.assertTrue(None == self.cell3.neighbour(maze.blocks.SOUTH))
#        self.assertTrue(self.cell1 == self.cell3.neighbour(maze.blocks.WEST))

if __name__ == '__main__': unittest.main()

