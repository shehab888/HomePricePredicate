from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import numpy as np

#creating the dataframe
np.random.seed(42)
#number of samples
n_samples = 1000
#random properties
rooms = np.random.randint(1, 6, size=n_samples)  #
area = np.random.randint(500, 4000, size=n_samples)  #
age = np.random.randint(0, 50, size=n_samples)  #
price = rooms * 10000 + area * 200 + (50 - age) * 3000 + np.random.randint(10000, 50000, size=n_samples)  #
# DataFrame
df = pd.DataFrame({
    'rooms': rooms,
    'area': area,
    'age': age,
    'price': price
})

# print(df.head())

x=df[['area','rooms','age']] # 2d always
y=df['price']

#split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)
#get the model
model=LinearRegression()
#fit the model to get the linear equation
model.fit(x_train,y_train)
#get the initial score
print(f"the initial score: {model.score(x_test,y_test)} ")
#save the model in file.pkl
with open('C:/Users/sheha/PycharmProjects/SimplePythonProject/home_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

