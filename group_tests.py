# group_tests.py

import unittest
from group import groups_of_3


class TestGroupsOf3(unittest.TestCase):
    def test_full_groups(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_incomplete_group(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]), [[1, 2, 3], [4, 5, 6], [7, 8]])

    def test_single_group(self):
        self.assertEqual(groups_of_3([1, 2, 3]), [[1, 2, 3]])

    def test_partial_group(self):
        self.assertEqual(groups_of_3([1, 2]), [[1, 2]])

    def test_empty_list(self):
        self.assertEqual(groups_of_3([]), [])

    def test_large_list(self):
        self.assertEqual(groups_of_3(list(range(1, 20))),
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19]])


if __name__ == '__main__':
    unittest.main()
