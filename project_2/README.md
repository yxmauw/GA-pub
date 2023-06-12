<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# __Project 2: Ames Housing sale price__

## __Problem Statement__:

Create a regression model based on the _**Ames Housing Dataset**_. This model will predict the price of a house at sale. <br><br>
Using this model, I would develop a web application where homeowners who wish to sell their property can use to find out what `SalePrice` to sell their property for. The website will have specific fields for visitors to fill and submit details about their property. Using our proprietary machine learning algorithm, the website will generate an estimate visitors can use as reference to quote their property `SalePrice`. 

## __Background:__
Project 2 involves using a well-known _**Ames housing data**_ to create a regression model that predicts the price of houses in Ames, IA. The Ames Housing Dataset is an exceptionally detailed and robust dataset with over 80 columns of different features relating to houses. I am allowed to use any and all features that are present in this dataset. <br><br> This is also a [Kaggle challenge](https://www.kaggle.com/competitions/dsi-us-11-project-2-regression-challenge/overview), so I would be making one or more submissions towards this regression challenge. Kaggle leaderboard standings will be determined by root mean squared error (`RMSE`).

## __Data provided:__
There are 3 datasets included in the [`datasets`](datasets/) folder for this project.
* [`sample_sub_reg.csv`](datasets/sample_sub_reg.csv): An example of a correctly formatted submission for this challenge (with a random number provided as predictions for `SalePrice`). My submission to Kaggle must match this format
* [`test.csv`](datasets/test.csv): Contains Kaggle test data. This data is fed into my regression model to make predictions for Kaggle submission. Target variable (`SalePrice`) is excluded from this data.
* [`train.csv`](datasets/train.csv): Contains all of the training data for my model. 
* [Data Dictionary](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

## __Goal:__
To predict the `SalePrice` for each house. For each Id in the test set, I must predict the value of the SalePrice variable.

## __Contents:__
1. [Data validation, exploration and cleaning](#data-validation-exploration-and-cleaning)
1. [Feature engineering](#feature-engineering)
1. [Feature selection](#feature-selection)
1. [Model and prediction](#model-and-prediction)
1. [Business case groupwork](#business-case)

For file reading accessibility, I split my technical report to 2 parts. 
1. [`Submission_EDA.ipynb`](#part-1) 
1. [`Submission_ML.ipynb`](#part-2) 

---
## __Part 1:__
---
### __Data validation, exploration and cleaning:__
* `.describe()`; `.info()`; `is.null().sum()`
* For graphical plots, I used:
    * scatterplot for numerical features
    * boxplot for categorical features
    * histogram for `SalePrice` target
* `SalePrice` has a right skewed distribution. 
* Outliers were identified visually on plots and isolated using `.loc` function.

### __Feature engineering:__
* Ordinal label encoding for ordinal categorical features. [Data dictionary](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt) helps differentiate nominal and ordinal categorical features.
* New features added for presence or absence of attribute e.g. `have_pool`, `have_fireplace`, `have_garage`, `have_fence`, `have_bsmt`. 
* Grouping of categorical values to reduce dummy columns during `pd.get_dummies()`
* `pd.get_dummies()`
* Dropped outliers and `Garage Yr Blt` feature

---
## __Part 2:__
---
### __Feature Selection:__
* Ranked features correlated to `SalePrice`. [`df.corr().SalePrice.sort_values(ascending=False)`]
* Find statistical significance of correlation after train-test-split and imputation of missing `Lot Frontage` values.
* Based on p-value < 0.05, shortlisted 20 features.

### __Model and Prediction:__
* `GridSearchCV`
    * Scoring by `neg_root_mean_squared_error`
* Fine tuned best model type from `GridSearchCV` <details>  Ridge model </details>
* Found that finetuning did not work well
* Checked for multicollinearity
    * Used VIF `from statsmodels.stats.outliers_influence import variance_inflation_factor`
    * Used correlation heatmap
* Dropped 4 features with high multicollinearity.
* Model `RSME` score became slightly worse, but still maintained generalisation with `test RSME` and `train RMSE` difference < 5%.
* Rerun `GridSearchCV` with 16 features. 
    * New best performing model <details> ElasticNet </details>
* Attempt to fine tune
* Used model for **Kaggle Submission** predictions. <details> impute missing values in [test.csv](./datasets/test.csv) using imputer trained on training data. </details>

### __Business Case:__
* Find common features used for model predictions among group members' models.
* 6 common features found, applied polynomial engineering for `Gr Liv Area` feature.
* Isolate the features on training data and rerun `GridSearchCV`.
* Using `mean_absolute_error`(MAE) as scoring metric, I picked the best model for deployment on web application.
* Web application [link](https://huggingface.co/spaces/yxmauw/ames-houseprice-recommender)

### __Summary:__
* `SalePrice` has a right skewed distribution, which results in a model that is unable to predict accurately for house sale prices above $400k
* `ElasticNet` under `GridSearchCV` is the final model used for deployment
* Deployed model has an accuracy of ±$11k based on MAE score
* There is high multicollinearity between strong predictive features for `SalePrice`
