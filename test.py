from joblib import load

# Load the model
d_tree_loaded = load('decision_tree_model.joblib')

# Now you can use d_tree_loaded to make predictions
# y_pred_loaded = d_tree_loaded.predict(X_test)

print(type(d_tree_loaded))  # This should print a model class, not numpy.ndarray
