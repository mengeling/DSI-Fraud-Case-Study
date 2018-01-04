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
In '''EDA.py''':
- Create column to label fraud transactions
- Create variable with transaction amounts as 'total_payout'
- Select numerical columns including 'sale_duration2', 'user_age', and 'body_length' 
- Drop rows with null values


## Machine Learning
In '''model.py''':
- Use 'description' column to vectorize, TFIDF, and fit Naive Bayes to predict fraud from text description
- Use 'sale_duration2', 'user_age', and 'body_length' to fit LogisticRegression to predict fraud
- Create average of probability of fraud produced b


## Persistence
- Use monggodb to store new user accounts along with our prediction and the probability of fraud produced by our model

## Interface
- Use Flask to present to user a rating of high, medium, or low risk of an individual user account


## Team
- Fraud analysts Michael Engeling, Kim Sorensen, and Owen Temple
