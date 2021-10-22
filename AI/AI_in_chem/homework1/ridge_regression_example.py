# Imports
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

N = 1000 # Sample size
np.random.seed(20211007) # Set random seed
X = np.arange(0., 10., .1) # Generate X data series in range [0.0, 10.0) with step 0.1
Y = np.sin(X) + np.random.normal(0.0, 0.5, X.size) # Generate Y data series by adding gaussian noise with μ = 0.0 and σ = 0.5 to sin(X)

# Generate polynomial features for fitting
# With degree=4 and include_bias=False, train_X will be transformed to 4-4-feature data series (without constant term)
# Got train_X like this:
# [[X0, X0^2, X0^3, X0^4],
# [X1, X1^2, X1^3, X1^4],
# ...
# [Xn-1, Xn-1^2, Xn-1^3, Xn-1^4]]
poly_features = PolynomialFeatures(degree=4, include_bias=False)
train_X = poly_features.fit_transform(X.reshape(-1, 1))

# print(train_X)

lambda_ = 1.0 # Regularization factor
train_model = linear_model.Ridge(alpha=lambda_, fit_intercept=True) # Create a ridge regression model
train_model.fit(train_X, Y) # Training

# Get model coefficients
# C[0] - intercept (constant term)
# C[1], C[2], C[3], C[4] - unpack model coefficients
C = [train_model.intercept_, *train_model.coef_]
print(C)
print("="*20, "# Model Parameters", "="*20, sep='\n')
for i, v in enumerate(C):
    print("C%d = %.4f" % (i, v))
    
pred_Y = train_model.predict(train_X) # Predicting
# with squared=False, mean_squared_error calculates RMSE
# Otherwise, mean_squared_error calculates RME
train_rmse = mean_squared_error(Y, pred_Y, squared=False)
print("="*20, "# Predict", "="*20, sep='\n')
print("Train RMSE = %.3f" % train_rmse)
