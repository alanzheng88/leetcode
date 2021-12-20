from unittest import TestCase
from ..three_sum import calculate_three_sum2


class Test(TestCase):
    def test_calculate_three_sum(self):
        self.assertEqual([], calculate_three_sum2([0]), 'expected empty array')

        self.assertEqual(
            [[-1, -1, 2], [-1, 0, 1]],
            calculate_three_sum2([-1, 0, 1, 2, -1, -4])
        )

        self.assertEqual(
            [[-1, 0, 1]],
            calculate_three_sum2([-1, 0, 1, 0])
        )

        self.assertEqual(
            [[0, 0, 0]],
            calculate_three_sum2([0, 0, 0])
        )

