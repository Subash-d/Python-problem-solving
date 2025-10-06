# 2 cols.
import numpy as np
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
a = np.linspace(1,20,100).reshape(-1,1)
b = a* random.uniform(2, 9)
X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(a,b)
print(mse)
print(f"{mse:.2f}")
print("{:.2f}".format(mse))



