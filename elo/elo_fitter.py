# import numpy as np
# import pandas as pd
#
#
# def fit_elo(student_item_scores, k=1):
#     students = pd.unique(student_item_scores[:, 0])
#     items = pd.unique(student_item_scores[:, 1])
#     abilities = dict(zip(students, np.zeros(len(students), np.double)))
#     difficulties = dict(zip(items, np.zeros(len(items), np.double)))
#     probs = dict(zip(students, [dict(zip(items, np.full(len(items), 0.5))) for _ in range(len(students))]))
#
#     for row in student_item_scores:
#         ability = abilities[row[0]]
#         difficulty = difficulties[row[1]]
#         correct = row[2]
#         prob = probs[row[0]][row[1]]
#         abilities[row[0]] = ability + (k * (correct - prob))
#         difficulties[row[1]] = difficulty + (k * (prob - correct))
#         probs[row[0]][row[1]] = 1 / (1 + np.exp(-(ability - difficulty)))
