# pcla-elo
Implementation of the Elo Algorithm

### This package provides two functionalities:
1. Running the Elo algorithm on a dataset of students, items, and scores for a given weighting parameter _k_
2. Fitting a dataset of students, items, and scores by running the elo algorithm iteratively and searching for the optimal weighting parameter _k_.

### Running the Elo algorithm
Use the `run_elo` function:

`run_elo(student_item_scores, k=1):`

This runs the elo algorithm for a given list of students, items, and scores and a weighting parameter k and returns the ability of each student,
 the difficulty of each item, and the Root Mean Squared Error (RMSE) of the predictions.

`student_item_scores`: a numpy array of shape mxn, where the first column is the student's name, the second column is the item's name and the third
column is the student's score on that item. A score of 1 is correct and a score of 0 is incorrect.

`k`: an optional parameter that informs the algorithm how much weight to put on predictions. The range of k is [0, 1], with default value of k 1.

`run_elo` returns: a dictionary of the abilities of students, a dictionary of the difficulties or items, and the Root Mean Squared Error (RMSE) of predictions.
"""

#### Example:
    student_item_scores = np.array([['good-1', 'easy-1', 1],
                                    ['good-2', 'med-1', 1],
                                    ['good-3', 'hard-1', 1],
                                    ['med-2', 'hard-2', 0],
                                    ['med-3', 'easy-1', 1],
                                    ['med-3', 'med-1', 0],
                                    ['med-3', 'med-2', 1],
                                    ['bad-1', 'med-1', 0],
                                    ['bad-1', 'med-2', 0],])

`k=0.5`

`abilities, difficulties, rmse = run_elo(student_item_scores, k)`

#### abilities

| good-1 | good-2 | good-3 | med-2 | med-3    | bad-1    |
|--------|--------|--------|-------|----------|----------|
| 0.25   | 0.25   | 0.25   | -0.25 | 0.172423 | -0.49509 |

#### difficulties

| easy-1    | med-1   | hard-1  | hard-2 | med-2     |
|-----------|---------|---------|--------|-----------|
| -0.468912 | 0.30037 | -0.25   | 0.25   | -0.008791 |

`rmse=0.49197252665675867`

### Fitting a dataset
Use the `fit_elo` function:

`fit_elo(student_item_scores, step=0.01):`

This searches the optimal k for a given list of students, items, and scores and returns student abilities, item difficulties, the optimal k and
the Root Mean Squared Error (RMSE) of predictions for that optimal k. This function iteratively calls the run_elo function by varying the values of k
between 0 and 1, with a default step of 0.01.

`student_item_scores`: a numpy array of shape mxn, where the first column is the student's name, the second column is the item's name and the third
column is the student's score on that item. A score of 1 is correct and a score of 0 is incorrect.

`step`: an optional parameter that informs the algorithm by how much to increase k on each iteration. The default value of step is 0.01.

`fit_elo` returns a dictionary of the abilities of students, a dictionary of the difficulties or items, the optimal k, and
the Root Mean Squared Error (RMSE) of predictions.

#### Example
    student_item_scores = np.array([['good-1', 'easy-1', 1],
                                    ['good-2', 'med-1', 1],
                                    ['good-3', 'hard-1', 1],
                                    ['med-2', 'hard-2', 0],
                                    ['med-3', 'easy-1', 1],
                                    ['med-3', 'med-1', 0],
                                    ['med-3', 'med-2', 1],
                                    ['bad-1', 'med-1', 0],
                                    ['bad-1', 'med-2', 0],])

`step=0.05`

`abilities, difficulties, optimal_k, rmse = fit_elo(student_item_scores, step)`

#### abilities

| good-1 | good-2 | good-3 | med-2  | med-3    | bad-1     |
|--------|--------|--------|--------|----------|-----------|
| 0.475  | 0.475  | 0.475  | -0.475 | 0.246386 | -0.932702 |

#### difficulties

| easy-1    | med-1    | hard-1 | hard-2 | med-2     |
|-----------|----------|--------|--------|-----------|
| -0.839262 | 0.618782 | -0.475 | 0.475  | -0.043206 |

`optimal_k=0.9500000000000003`

`rmse=0.4839302619103182`