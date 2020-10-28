from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
df = pd.read_csv('Demo.csv')



x=df.drop(columns=['Fun','Name'])
y=df['Fun']


x_train , x_test , y_train, y_test = train_test_split(x,y,test_size=0.2)
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
predictions = model.predict(x_test)
home = accuracy_score(y_test,predictions)
print(home)

regr = linear_model.LinearRegression()
regr.fit(x_test,y_test)
predictem = regr.predict([[8,2]])
if 1 in predictem:
    print(predictem,'happy')
elif 2 in predictem:
    print(predictem,'bitchass')
else:
    print(predictem)


