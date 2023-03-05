import sys
from elo_runner import run_elo


def fit_elo(student_item_scores, step=0.01):
    """
    Searches the optimal k for a given list of students, items, and scores and returns student abilities, item difficulties, the optimal k and
    the Root Mean Squared Error (RMSE) of predictions for that optimal k. This function iteratively calls the run_elo function by varying the values of k
    between 0 and 1, with a default step of 0.01.
    :param student_item_scores: a numpy array of shape mxn, where the first column is the student's name, the second column is the item's name and the third
    column is the student's score on that item. A score of 1 is correct and a score of 0 is incorrect.
    :param step: an optional parameter that informs the algorithm by how much to increase k on each iteration. The default value of step is 0.01.
    :return: a dictionary of the abilities of students, a dictionary of the difficulties or items, the optimal k, and
    the Root Mean Squared Error (RMSE) of predictions.
    """

    if step < 0 or step > 1:
        raise ValueError("step must be between 0 and 1. You provided ", step)

    k = 0
    optimal_k = 0
    lowest_root_mean_squared_error = sys.float_info.max
    optimal_abilities = []
    optimal_difficulties = []
    while k < 1:
        abilities, difficulties, root_mean_squared_error = run_elo(student_item_scores, k)
        if root_mean_squared_error < lowest_root_mean_squared_error:
            optimal_k = k
            lowest_root_mean_squared_error = root_mean_squared_error
            optimal_abilities = abilities
            optimal_difficulties = difficulties
        k += step
    return optimal_abilities, optimal_difficulties, optimal_k, lowest_root_mean_squared_error
