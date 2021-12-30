from unittest import TestCase
from ..four_sum import four_sum


class Test(TestCase):
    def test_four_sum(self):
        self.assertEqual(
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            four_sum([1, 0, -1, 0, -2, 2], 0)
        )
        self.assertEqual(
            [[2, 2, 2, 2]],
            four_sum([2, 2, 2, 2, 2], 8)
        )
