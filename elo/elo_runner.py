import numpy as np
import pandas as pd


def run_elo(student_item_scores, k=1):
    """
    Runs the elo algorithm for a given list of students, items, and scores and a weighting parameter k and returns the ability of each student,
     the difficulty of each item, and the Root Mean Squared Error (RMSE) of the predictions.
    :param student_item_scores: a numpy array of shape mxn, where the fist column is the student's name, the second column is the item's name and the third
    column is the student's score on that item. A score of 1 is correct and a score of 0 is incorrect.
    :param k: an optional parameter that informs the algorithm how much weight to put on predictions. The range of k is [0, 1], with default value of k 1.
    :return: a dictionary of the abilities of students, a dictionary of the difficulties or items, and the Root Mean Squared Error (RMSE) of predictions.
    """

    if k < 0 or k > 1:
        raise ValueError("k must be between 0 and 1. You provided ", k)

    students = pd.unique(student_item_scores[:, 0])
    items = pd.unique(student_item_scores[:, 1])
    abilities = dict(zip(students, np.zeros(len(students), np.double)))
    difficulties = dict(zip(items, np.zeros(len(items), np.double)))
    predicted = 0.5
    error = 0.0
    for row in student_item_scores:
        correct = int(row[2])
        error += pow(predicted - correct, 2)
        prob = 1 / (1 + np.exp(-(abilities[row[0]] - difficulties[row[1]])))
        abilities[row[0]] = abilities[row[0]] + (k * (correct - prob))
        difficulties[row[1]] = difficulties[row[1]] + (k * (prob - correct))
        predicted = prob
    root_mean_squared_error = np.sqrt(error / len(student_item_scores))
    return abilities, difficulties, root_mean_squared_error
