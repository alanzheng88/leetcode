from unittest import TestCase
from ..three_sum_closest import calculate_three_sum_closest


class Test(TestCase):
    def test_calculate_three_sum_closest(self):
        # self.assertEqual(
        #     0,
        #     calculate_three_sum_closest([0, 0, 0], 0)
        # )
        #
        # self.assertEqual(
        #     2,
        #     calculate_three_sum_closest([-1, 2, 1, -4], 1)
        # )        # self.assertEqual(
        #     0,
        #     calculate_three_sum_closest([0, 0, 0], 0)
        # )
        #
        # self.assertEqual(
        #     2,
        #     calculate_three_sum_closest([-1, 2, 1, -4], 1)
        # )

        self.assertEqual(
            0,
            calculate_three_sum_closest([0, 2, 1, -3], 1)
        )
        # -3, 0, 1, 2
