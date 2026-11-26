# Project 4 Write-up: Predicting Titanic Survival with a Decision Tree

## The prediction
Predict whether a passenger survived from their ticket class, sex, age and fare. `survived` is the target, and `pclass`, `sex` (1 = female, 0 = male), `age` and `fare` are the features, in that order.

## Method
- Data: the Titanic dataset from seaborn, reduced to those five columns.
- Cleaning: the 177 rows with a missing age were dropped, leaving 714 passengers.
- Split: 80% training (571 passengers) and 20% test (143 passengers), with `random_state=42` and `stratify=y` so both sets have the same survival rate (0.406).
- Model: `DecisionTreeClassifier(max_depth=4, random_state=42)`, trained on the training set only.

## Results
- **Baseline:** always guessing "did not survive" is right 59.4% of the time on the test set.
- **Model accuracy:** 79.7% on the test set, about 20 points above the baseline.
- **Confusion matrix (test set):** 72 passengers who died were correctly predicted to die and 42 who survived were correctly predicted to survive. The model wrongly predicted survival for 13 passengers who died and wrongly predicted death for 16 who survived. It identified about 85% of those who died but only about 72% of those who survived.
- **Overfitting:** training accuracy rose from 0.779 (depth 1) to 0.968 (depth 12), while test accuracy stayed between about 0.76 and 0.81. A very deep tree memorises the quirks of the training passengers, so it does not generalise.
- **Most important features:** sex (0.55), ticket class (0.24), age (0.14) and fare (0.08).

## Limitations
- **Less data:** dropping rows with a missing age removed about 20% of the passengers, and those passengers may differ from the rest.
- **Small test set:** with only 143 test passengers, one passenger is worth about 0.7 percentage points. A different split could change the accuracy by several points, so small differences between depths are not meaningful.
- **Depth looked at on the test set:** comparing depths on the test set is a mild form of using it to make a choice. Cross-validation would be a fairer approach.
- **Few features:** the model uses only four columns and ignores others, such as family size.
- **Association, not cause:** feature importance shows what the model relies on, not what caused survival. This is a historical dataset used as a learning exercise, not a tool for real decisions.
