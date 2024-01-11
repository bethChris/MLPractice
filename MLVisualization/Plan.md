# Design Plan

## Overview
This project is intended to be a visualization of simple machine learning models on a free data set from Kaggle. The idea is the user would be able to choose which model they'd like to see, and it would make a prediction using randomly pulled test data from a free API. (Either a joke, quote, house listing, etc) The hope is to have a display of how close the model got by visualizing differnt metrics. It would be cool to have some sort of gradient descent visual/animation as well. 

## List of Parts

### Main Page
This page will have the sites information on it. This will include:
- an overview of how to use the site

### Models Page
This page will have different buttons to click on that switches the visual to represent that certain model. The graphic will be a graph of the AUC and there will be explanations and a button for them to continue to get new test data to see how the model predicts.

> Ideally I'd like 3 different models to compare and contrast

### Gradient Descent Page
This page is on the back burner a bit but I'd like to have a way to show how hyperparameter tuning using gradient descent works. It's more of a general loose concept that i'll work on once the basic models page is implemented.

### Resource Page
This page is a list and links and thank yous to all the resources i'll most definitly be using for this.
Start list here:
- Flask



### TODO CHECKLIST
- Decide on dataset
    - https://www.kaggle.com/datasets/vikashrajluhaniwal/jester-17m-jokes-ratings-dataset?select=jester_ratings.csv 

- clean data set
- train models
- save models (using joblib)
- create index html UI
- decide on visualization and metrics
