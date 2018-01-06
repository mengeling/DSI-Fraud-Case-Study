# Fraud Detection Case Study

Use machine learning to identify user accounts that might be fraudulent.

## App Usage
- Run ```python model.py``` to create a model
- This model is saved as a pickle file
- Run ```python app/app.py``` to open a model to base new predictions on
- An infinite loop is initiated that makes a GET request to the fraud case endpoint
- The new row is stored in the database along with a prediction and a probability of fraud 
- Open ```http//:localhost:8000``` in a browser to see front end where fraud predictions appear

## EDA
In ```EDA.py```:
- Create column to label fraud transactions
- Create variable with transaction amounts as 'total_payout'
- Select numerical columns including 'sale_duration2', 'user_age', and 'body_length' 
- Drop rows with null values

## Machine Learning
In ```model.py```:
- Use 'description' column to vectorize, TFIDF, and fit RandomForestClassifier to predict fraud from text description
- Use 'sale_duration2', 'user_age', 'total_payout', and 'body_length' to fit RandomForestClassifier to make predictions
from numerical features
- Create average of probability of fraud produced

## Persistence
- Use MongoDB to store new user accounts along with our prediction and the probability of fraud produced by our model

## Interface
- Use Flask to present user with a rating of high, medium, or low risk of fraud

## Team
- Fraud analysts: Michael Engeling, Kim Sorensen, and Owen Temple

&nbsp;
&nbsp;

![App Screenshot](/images/app_screenshot.png)
