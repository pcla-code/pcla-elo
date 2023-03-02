import numpy as np
import pandas as pd


def run_elo(student_item_scores, k=1):
    students = pd.unique(student_item_scores[:, 0])
    items = pd.unique(student_item_scores[:, 1])
    abilities = dict(zip(students, np.zeros(len(students), np.double)))
    difficulties = dict(zip(items, np.zeros(len(items), np.double)))

    for row in student_item_scores:
        correct = int(row[2])
        prob = 1 / (1 + np.exp(-(abilities[row[0]] - difficulties[row[1]])))
        abilities[row[0]] = abilities[row[0]] + (k * (correct - prob))
        difficulties[row[1]] = difficulties[row[1]] + (k * (prob - correct))
    return abilities, difficulties
