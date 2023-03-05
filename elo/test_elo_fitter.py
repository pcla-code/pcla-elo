from unittest import TestCase

from numpy.testing import assert_almost_equal

from elo_fitter import fit_elo

from base_test_case import BaseTestCase


class Test(TestCase, BaseTestCase):
    def test_fit_elo_nine_students_nine_items(self):
        # given
        expected_optimal_k = 0.99
        expected_lowest_root_mean_squared_error = 0.4899

        # when
        _, _, actual_optimal_k, actual_lowest_root_mean_squared_error = fit_elo(self.student_item_scores)

        # then
        assert_almost_equal(actual_optimal_k, expected_optimal_k, decimal=4, err_msg="mismatch:\n", verbose=True)
        assert_almost_equal(actual_lowest_root_mean_squared_error, expected_lowest_root_mean_squared_error, decimal=4, err_msg="mismatch:\n", verbose=True)
