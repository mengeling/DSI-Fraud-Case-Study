# threshold for classification
THRESHOLD = 0.5

# columns used to build model
MODEL_COLS = ["sale_duration2", "user_age", "body_length", "description", "acct_type", "ticket_types"]

# columns used to make predictions
PREDICT_COLS = ["sale_duration2", "user_age", "body_length", "description", "ticket_types"]

# columns used in EDA
EDA_COLS = ["user_age", "body_length", "channels", "delivery_method", "fb_published", "has_analytics",
            "num_payouts", "sale_duration2", "total_payout"]
