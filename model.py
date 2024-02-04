from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score


dataset=pd.read_csv('iot.csv')
X=dataset.iloc[:,1].values
Y=dataset.iloc[:,-1].values

X=X.reshape(-1,1)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25)

classifier=KNeighborsClassifier()
classifier.fit(X_train,Y_train)

Y_pred=classifier.predict(X_test)
print(accuracy_score(Y_pred,Y_test))