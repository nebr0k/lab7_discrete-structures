import unittest
import numpy as np
from main import  calculate_degree, find_isolated_pendant_vertices

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.adjacency_matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

    def test_calculate_degree(self):
        in_degree, out_degree = calculate_degree(self.adjacency_matrix)
        self.assertTrue(np.array_equal(in_degree, np.array([1, 2, 1])))
        self.assertTrue(np.array_equal(out_degree, np.array([1, 2, 1])))

    def test_find_isolated_pendant_vertices(self):
        isolated, pendant = find_isolated_pendant_vertices(self.adjacency_matrix)
        self.assertTrue(np.array_equal(isolated, np.array([])))
        self.assertTrue(np.array_equal(pendant, np.array([0, 2])))



if __name__ == '__main__':
    unittest.main()
