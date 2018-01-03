# Fraud Detection Case Study

Use machine learning to identify user accounts that might be fraudulent.

## EDA
In '''EDA.py''':
- Create column to label fraud transactions
- Select numerical and categorical columns 
- Drop rows with null values
- Create variable with transaction amounts
- Convert categorical features to dummy code variables


## Machine Learning
In '''model.py''':
- Use 'description' column to vectorize, TFIDF, and fit Naive Bayes to predict fraud from text description
- Use numerical and categorical features to fit DecisionTreeClassifier to predict fraud

 

