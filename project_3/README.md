<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Project 3: NLP subreddit post classifier

## Problem statement
---
This project is about using 2 subreddits, of my choice, to train a Natural Language Processing classifier that can differentiate which subreddit a given post came from.

This is a binary classification problem.

### Jupyter Notebooks:
---
* [`Webscraping_data`](./Project_3_data.ipynb)
* [`EDA_ML_evaluation`](./Project_3_ML.ipynb)
* [`Wrong_classification_evaluation`](./Project_3_misclass_EDA.ipynb)

## Contents:
---
1. Get data:
    * Chose [r/Marvel](https://www.reddit.com/r/Marvel/) and [r/DCcomics](https://www.reddit.com/r/DCcomics/)
    * Webscraped with some filtering, excluded blank, removed or deleted posts. 

1. Data exploration:
    * Check for null values
    * Word clouds using [word cloud package](https://pypi.org/project/wordcloud/)
    * Word count

1. Feature engineering:
    * `full_post`(label) = `selftext` + `title`
    * One-hot encoding of label (`subreddit`)

1. Train-test-split
    * Stratify label
    * test size .2
    
1. Tokenizing / lemmatizing
    * `RegexpTokenizer('[a-z]+', gaps=False)`
    * `WordNetLemmatizer()`

1. GridSearchCV 
    * test best parameters and word vectorizers-classifier combinations
    * Word vectorizers:
        * `CountVectorizer()`
        * `TfidfVectorizer()`
    * Classifiers:
        * `RandomForestClassifier()`
        * `MultinomialNB()`

1. Chose the word vectorizer-classifiers combination with the best `ROC AUC score` for each model type. 

1. Isolate **`GridSearchCV RandomForest classifier`** and **`GridSearchCV MultinomialNB`** models for detailed model evaluation using specific model attributes
    
1. Evaluate models with multiple metrics
    * `confusion_matrix()`
    * `model.score()` (accuracy)
    * `precision_score()`
    * `recall_score()`
    * `f1_score()`
    * `tn/(tn+fp)` (specificity)
    * `roc_auc_score()`
    * Generalisation of each score except confusion matrix

1. Plot evaluation metrics
    * feature importances horizontal bar chart
    * `ConfusionMatrixDisplay()`
    * Predicted probability distribution bar charts
    * `RocCurveDisplay()`
    * `PrecisionRecallDisplay()`

## Limitations, Recommendations and Conclusion
---

__Conclusion:__
1. Final model chosen for deployment is Countvectorizer with Multinomial Naive Bayes

__Limitations:__
1. This model is limited to classifying between <mark>**Marvel**</mark> and <mark>**DC comics**</mark> subreddits
1. any new post with all out-of-vocabulary words may not be classified correctly

__Recommendations:__
1. Use specified vocabulary list in word vectorizers
1. Try other classification models
1. Investigate what contributes to posts being wrongly classified 