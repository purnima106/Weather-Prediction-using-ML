import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pickle

data = pd.read_csv("seattle-weather.csv")
print(data)

print(data.isnull().sum())

features = data[["precipitation", "temp_max", "temp_max", "wind"]]
target = data["weather"]

x_train,x_test,y_train,y_test = train_test_split(features, target)

model = GaussianNB()
model.fit(x_train, y_train)

cr = classification_report(y_test, model.predict(x_test))
print(cr)

preci = float(input("Enter approx precipitation:  "))
temp_max = float(input("Enter maximum temp throughout the day:  "))
temp_min = float(input("Enter minimum temp at night:  "))
win = float(input("Enter wind:  "))
data  = [[preci, temp_max, temp_min, win]]
weather = model.predict(data)
print(weather)

f = open("re.model", "wb")
pickle.dump(model, f)
f.close()

