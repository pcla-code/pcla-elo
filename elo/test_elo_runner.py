from unittest import TestCase

from numpy.testing import assert_almost_equal

from base_test_case import BaseTestCase
from elo_runner import run_elo


class Test(TestCase, BaseTestCase):

    def test_run_elo_nine_students_nine_items(self):
        # given
        expected_abilities = {'good-1': 1.1598,
                              'good-2': 0.3651,
                              'good-3': -.1206,
                              'med-1': -0.505,
                              'med-2': -.8437,
                              'med-3': -1.1526,
                              'bad-1': -1.4361,
                              'bad-2': -1.6958,
                              'bad-3': -1.9333}
        expected_difficulties = {'easy-1': -1.1598,
                                 'easy-2': -.3651,
                                 'easy-3': .1206,
                                 'med-1': .5050,
                                 'med-2': .8437,
                                 'med-3': 1.1526,
                                 'hard-1': 1.4361,
                                 'hard-2': 1.6958,
                                 'hard-3': 1.9333}

        # when
        actual_abilities, actual_difficulties, _ = run_elo(self.student_item_scores)

        # then
        for student in actual_abilities.keys():
            assert_almost_equal(actual_abilities[student], expected_abilities[student], decimal=4,
                                err_msg="mismatch:\n", verbose=True)
        for item in actual_difficulties.keys():
            assert_almost_equal(actual_difficulties[item], expected_difficulties[item], decimal=4,
                                err_msg="mismatch:\n", verbose=True)
        assert len(actual_abilities) == len(expected_abilities)
        assert len(actual_difficulties) == len(expected_difficulties)
