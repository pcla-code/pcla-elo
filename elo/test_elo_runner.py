from unittest import TestCase
from elo_runner import run_elo
import numpy as np
from numpy.testing import assert_almost_equal


class Test(TestCase):

    def test_run_elo_nine_students_nine_items(self):
        # given
        student_item_scores = np.array([['good-1', 'easy-1', 1],
                                        ['good-1', 'easy-2', 1],
                                        ['good-1', 'easy-3', 1],
                                        ['good-1', 'med-1', 1],
                                        ['good-1', 'med-2', 1],
                                        ['good-1', 'med-3', 1],
                                        ['good-1', 'hard-1', 1],
                                        ['good-1', 'hard-2', 1],
                                        ['good-1', 'hard-3', 0],
                                        ['good-2', 'easy-1', 1],
                                        ['good-2', 'easy-2', 1],
                                        ['good-2', 'easy-3', 1],
                                        ['good-2', 'med-1', 1],
                                        ['good-2', 'med-2', 1],
                                        ['good-2', 'med-3', 1],
                                        ['good-2', 'hard-1', 1],
                                        ['good-2', 'hard-2', 0],
                                        ['good-2', 'hard-3', 0],
                                        ['good-3', 'easy-1', 1],
                                        ['good-3', 'easy-2', 1],
                                        ['good-3', 'easy-3', 1],
                                        ['good-3', 'med-1', 1],
                                        ['good-3', 'med-2', 1],
                                        ['good-3', 'med-3', 1],
                                        ['good-3', 'hard-1', 0],
                                        ['good-3', 'hard-2', 0],
                                        ['good-3', 'hard-3', 0],
                                        ['med-1', 'easy-1', 1],
                                        ['med-1', 'easy-2', 1],
                                        ['med-1', 'easy-3', 1],
                                        ['med-1', 'med-1', 1],
                                        ['med-1', 'med-2', 1],
                                        ['med-1', 'med-3', 0],
                                        ['med-1', 'hard-1', 0],
                                        ['med-1', 'hard-2', 0],
                                        ['med-1', 'hard-3', 0],
                                        ['med-2', 'easy-1', 1],
                                        ['med-2', 'easy-2', 1],
                                        ['med-2', 'easy-3', 1],
                                        ['med-2', 'med-1', 1],
                                        ['med-2', 'med-2', 0],
                                        ['med-2', 'med-3', 0],
                                        ['med-2', 'hard-1', 0],
                                        ['med-2', 'hard-2', 0],
                                        ['med-2', 'hard-3', 0],
                                        ['med-3', 'easy-1', 1],
                                        ['med-3', 'easy-2', 1],
                                        ['med-3', 'easy-3', 1],
                                        ['med-3', 'med-1', 0],
                                        ['med-3', 'med-2', 0],
                                        ['med-3', 'med-3', 0],
                                        ['med-3', 'hard-1', 0],
                                        ['med-3', 'hard-2', 0],
                                        ['med-3', 'hard-3', 0],
                                        ['bad-1', 'easy-1', 1],
                                        ['bad-1', 'easy-2', 1],
                                        ['bad-1', 'easy-3', 0],
                                        ['bad-1', 'med-1', 0],
                                        ['bad-1', 'med-2', 0],
                                        ['bad-1', 'med-3', 0],
                                        ['bad-1', 'hard-1', 0],
                                        ['bad-1', 'hard-2', 0],
                                        ['bad-1', 'hard-3', 0],
                                        ['bad-2', 'easy-1', 1],
                                        ['bad-2', 'easy-2', 0],
                                        ['bad-2', 'easy-3', 0],
                                        ['bad-2', 'med-1', 0],
                                        ['bad-2', 'med-2', 0],
                                        ['bad-2', 'med-3', 0],
                                        ['bad-2', 'hard-1', 0],
                                        ['bad-2', 'hard-2', 0],
                                        ['bad-2', 'hard-3', 0],
                                        ['bad-3', 'easy-1', 0],
                                        ['bad-3', 'easy-2', 0],
                                        ['bad-3', 'easy-3', 0],
                                        ['bad-3', 'med-1', 0],
                                        ['bad-3', 'med-2', 0],
                                        ['bad-3', 'med-3', 0],
                                        ['bad-3', 'hard-1', 0],
                                        ['bad-3', 'hard-2', 0],
                                        ['bad-3', 'hard-3', 0]])
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
        actual_abilities, actual_difficulties = run_elo(student_item_scores)
        # then
        for student in actual_abilities.keys():
            assert_almost_equal(actual_abilities[student], expected_abilities[student], decimal=4,
                                err_msg="mismatch:\n", verbose=True)
        for item in actual_difficulties.keys():
            assert_almost_equal(actual_difficulties[item], expected_difficulties[item], decimal=4,
                                err_msg="mismatch:\n", verbose=True)
        assert len(actual_abilities) == len(expected_abilities)
        assert len(actual_difficulties) == len(expected_difficulties)
