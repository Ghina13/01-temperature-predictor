import numpy as np
from sklearn.linear_model import LinearRegression

# Data: past days and corresponding temperatures
x = np.array([[30], [31], [32], [33], [34]])
y = np.array([31, 32, 33, 34, 35])

# Model training
model = LinearRegression()
model.fit(x, y)

# Prediction
new_x = np.array([[35]])
prediction = model.predict(new_x)

print(f"the possible temperature for tomorrow will be:{prediction[0]} ")