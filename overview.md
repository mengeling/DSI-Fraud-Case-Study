
## Process Flow
- Ran DecisionTree, RandomForestClassifier, MultinomialNB, and LogisticRegression
- Decided to avaerage results of MultinomialNB and LogisticRegression
   
## Preprocessing
- Take every row that is not labeled "Premium" and tag them as "Fraud" in new column
- Take out the "description" column and vectorize, TFIDF, the text
- Take out the 'user_age', 'sale_duration2', and 'body_length'
    
## Assessment Metrics Selected
- Ran accuracy of text classification via score method of MultinomialNB library
- Ran accuracy of LogisticRegression via score method
- Calculated precision and recall of LogisticRegression via sklearn precision and recall modules
    
## Validation and Testing Methodology
- Use sklearn's train_test_split to reserve 20% of train data 
- Assessed accuracy on test dataset
    
## Parameter Tuning Involved in Generating the Model
- Determined that default settings performed satisfactorily
    
## Next Steps 
- Hyperparameter tuning using grid search
- Use Bootstrap dashboard skin for model output
- Use confusion matrix to assess more accurate costs of classification errors
