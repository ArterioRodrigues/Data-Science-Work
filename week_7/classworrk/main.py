"""
Name:  Arterio Rodrigues
Email: arterio.rodrigues47@myhunter.cuny.edu
Resources:  Python3.8
I attended lecture today.
Row:  2
Seat:  72
"""

#Import datasets, classifiers and performance metrics:
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#Using the digits data set from sklearn:
from sklearn import datasets


def binary_digit_clf(data, target, test_size = 0.25, random_state = 21):
    '''
    data: a numpy array that includes rows of equal size flattend arrays,
    target a numpy array that takes values 0 or 1 corresponding to the rows of data.
    test_size: the size of the test set created when the data is divided into test and training sets with train_test_split. The default value is 0.25.
    random_state: the random seed used when the data is divided into test and training sets with train_test_split. The default value is 21.
    '''
    log_reg = LogisticRegression(tol=0.0001, random_state=42)

    X_train = data[0: int(len(data) * (1-test_size))]
    y_train = target[0: int(len(target) * (1-test_size))]

    X_test = data[int(len(data) * (1-test_size)):]
    y_test = target[int(len(target) * (1-test_size)):]

    log_reg.fit(X_train, y_train)
    log_reg_pred = log_reg.predict(X_test)
    
    return metrics.confusion_matrix(y_test, log_reg_pred)

