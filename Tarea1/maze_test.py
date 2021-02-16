from unittest import TestCase
from maze import Maze

class TryTesting(TestCase):
    def test_maze1_solution(self):
        m = Maze("maze1.txt")
        m.solve()
        self.assertEqual(m.solution,(['up', 'right', 'right', 'right', 'right', 'up', 'up', 'right', 'up', 'up'],
                                    [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (2, 5), (1, 5), (0, 5)]))

    def test_maze2_solution(self):
        m = Maze("maze2.txt")
        m.solve()
        self.assertEqual(m.solution,(['right', 'right', 'right', 'right', 'right', 'right', 'up', 'up', 'up', 'left',
                                    'left', 'left', 'up', 'up', 'up', 'up', 'right', 'right', 'right', 'up', 'up',
                                    'right', 'right', 'right', 'right', 'right', 'right', 'right', 'down', 'down'],
                                    [(15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (14, 6), (13, 6), (12, 6),
                                    (12, 5), (12, 4), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (8, 4), (8, 5), (8, 6),
                                    (7, 6), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (7, 13), (8, 13)]))
    
    def test_maze3_solution(self):
        m = Maze("maze3.txt")
        m.solve()
        self.assertEqual(m.solution,(['up', 'right', 'up', 'up'], [(4, 0), (4, 1), (3, 1), (2, 1)]))

    def test_maze4_solution(self):
        m = Maze("maze4.txt")
        m.solve()
        self.assertEqual(m.solution,(['right','right','right','right','right','right','up',
                                      'right','right','right','right','right','right','right',
                                      'right','right', 'up','up','left','left','up','up','left','up','up','up',
                                      'right','right','right','up','up','right','right','right','right','right','up','up',
                                      'left','left','left','left','left','left','left','up','up','left','left','left','left'],
                                    [(15, 1),(15,2),(15,3),(15,4),(15,5),(15,6),(14,7),(14,8),
                                     (14,9),(14,10),(14,11),(14,12),(14,13),(14,14),(14,15),(14,16),
                                     (13,16),(12,16),(12,15),(12,14),(11,14),(10,14),(10,13),(10,12),(10,11),(10,10),(10,9),(10,8),(10,7),
                                     (9,7),(8,7),(7,7),(6,7),(6,8),(6,9),(6,10),(5,10),(4,10),(4,11),(4,12),(4,13),(4,14),(4,15),(3,15),(2,15),
                                     (2,14),(2,13),(2,12),(2,11),(2,11),(2,10),(2,9),(1,9),(0,9),(0,8),(0,6),(0,5),(0,4)]))

    def test_maze5_solution(self):
        m = Maze("maze5.txt")
        m.solve()
        self.assertEqual(m.solution,(['down','down','right','right','down','down','right','right','right','right','right',
                                    'down','right','right','right','up','up','up','up','up'],
                                    [(1, 0),(2,0),(2,1),(2,2)(3,2),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(5,7),(5,8),
                                    (5,9),(5,10),(4,10),(3,10),(2,10),(1,10),(0,10),(0,9),(0,8),(0,7),(0,6),(0,5),(0,4),
                                    (0,3)]))