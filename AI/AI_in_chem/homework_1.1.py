# Imports
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator





# Open data
# Cause the code was tested in Github, please change the directory.
train_data = pd.read_table('./AI/AI_in_chem/train.dat',sep=" ",header=None).values.tolist()
test_data = pd.read_table('./AI/AI_in_chem/test.dat',sep=" ",header=None).values.tolist() # type - list

x = np.array([row[0] for row in train_data] )
y = np.array([row[1] for row in train_data] )
X_test = np.array([row[0] for row in test_data] )
Y_test = np.array([row[1] for row in test_data] )

# Generate polynomial features for fitting
# With degree=4 and include_bias=False, train_X will be transformed to 4-feature data series (without constant term)
# Got train_X like this:
# [[X0, X0^2, X0^3, X0^4],
# [X1, X1^2, X1^3, X1^4],
# ...
# [Xn-1, Xn-1^2, Xn-1^3, Xn-1^4]]


poly_features = PolynomialFeatures(degree=4, include_bias=False)
train_X = poly_features.fit_transform(x.reshape(-1, 1)) #reshape (-1,1)转换成一列，为np功能
test_X = poly_features.fit_transform(X_test.reshape(-1, 1)) #reshape (-1,1)转换成一列，为np功能


# create list to save data
lambda_to_y_list = []
list_collect_0 = []

for lam in np.logspace(-6, 6, 100):
    
    # Train Data
    # ==============================================
    # ==============================================
    lambda_ =lam
    # lambda_ = np.power(2,lam)/np.power(2,10) # Regularization factor
    train_model = linear_model.Ridge(alpha=lambda_, fit_intercept=True) # Create a ridge regression model
    train_model.fit(train_X, y) # Training

    # Get model coefficients
    # C[0] - intercept (constant term)
    # C[1], C[2], C[3], C[4] - unpack model coefficients

    C = [train_model.intercept_, *train_model.coef_]
    print("="*20, "# Model Parameters", "="*20, sep='\n')
    for i, v in enumerate(C):
        print("C%d = %.4f" % (i, v))
        
    pred_Y = train_model.predict(train_X) # Predicting
    # with squared=False, mean_squared_error calculates RMSE
    # Otherwise, mean_squared_error calculates RME
    train_rmse = mean_squared_error(y, pred_Y, squared=False)

    print("="*20, "# Predict", "="*20, sep='\n')
    print("Train RMSE = %.3f" % train_rmse,'\n',"Lambda = %.2f" % lambda_)
    lambda_to_y_list = []
    lambda_to_y_list.append(lambda_)
    lambda_to_y_list.append(float(f'{train_rmse:>.3f}'))
    lambda_to_y_list += C
    
    # Test Data
    # ==============================================
    # ==============================================
    
    pred_Y_test = train_model.predict(test_X) # Predicting
    # with squared=False, mean_squared_error calculates RMSE
    # Otherwise, mean_squared_error calculates RME
    test_rmse = mean_squared_error(Y_test, pred_Y_test, squared=False)
    print("Test RMSE = %.3f" % test_rmse,'\n',"Lambda = %.2f" % lambda_)
    lambda_to_y_list.append(float(f'{test_rmse:>.3f}'))
    
    list_collect_0.append(lambda_to_y_list)


# show the min test_rmse data
list_collect_0 = list(map(list,zip(*list_collect_0)))

index = list_collect_0[-1].index(min(list_collect_0[-1]))
print(list_collect_0[-1])
print("="*20, "# Predict_MIN_Test_RMSE", "="*20, sep='\n')
print("Train RMSE = %.3f" % list_collect_0[1][index],'\n',"Lambda = %.2f" % list_collect_0[0][index],'\n',"Test RMSE = %.3f" % list_collect_0[-1][index])
print("="*20, "# Model Parameters", "="*20, sep='\n')
for i in range(len(list_collect_0)-3):
    print("C%d = %.4f" % (i, list_collect_0[i+2][index]))


# show the lambda_to_result plot

plt.figure(num=3,figsize=(8,5))

plt.plot(np.log(list_collect_0[0]),list_collect_0[1],label = "RMSE_TRAIN")
plt.plot(np.log(list_collect_0[0]),list_collect_0[-1],label = "RMSE_TEST")



for i in range(len(list_collect_0)-3): 
    plt.plot(np.log(list_collect_0[0]),list_collect_0[i+2],label='C'+str(i))


plt.xlabel('ln(lambda)')
plt.title("Regression Result")


# plt.ylim(-0.5,10)
plt.legend()
plt.grid(ls='--')#添加网格

plt.show()