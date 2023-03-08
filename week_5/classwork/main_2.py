from sklearn import linear_model, datasets

X,y = datasets.load_diabetes(return_X_y = True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.33, random_state = 42)

reg = linear_model.LinearRegression()

reg.fit(X_train, y_train)


print(X_test)
print(y_test)
y_pred = reg.predict(X_test)

print(y_pred)