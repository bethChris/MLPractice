from sklearn.dummy import DummyRegressor
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd
import joblib

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import (
    cross_validate,
    train_test_split,
)

# Load dataset
joke_data = pd.read_csv('../data/jester_combined.csv')

# define data
X = joke_data['jokeText']
y = joke_data['rank']

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state=321)


# define dummy model
dummy = DummyRegressor()

# define the preprocessing
countvec = CountVectorizer(stop_words="english")

# create pipeline
pipeline = make_pipeline(countvec, dummy)
pipeline.fit(X_train, y_train)

# create a dataframe, insert the results of cross validating the pipeline and data
cross_val_results = pd.DataFrame(
    cross_validate(pipeline, X_train, y_train, return_train_score=True)
)

# take the mean of the cross validation results
print("Mean Cross Validation Scores:\n", cross_val_results.mean())

# make prediction on test data
# print(pipeline.predict(X_test))
print("\nScore:", pipeline.score(X_test, y_test))

