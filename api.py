from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from flask import Flask,render_template,request

def generate_model(dataset_file):
    dataset=pd.read_csv('iot.csv')
    X=dataset.iloc[:,1].values
    Y=dataset.iloc[:,-1].values

    X=X.reshape(-1,1)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25)

    classifier=KNeighborsClassifier()
    classifier.fit(X_train,Y_train)

    Y_pred=classifier.predict(X_test)
    print(accuracy_score(Y_pred,Y_test))
    return classifier

app=Flask(__name__)

@app.route('/')
def indexPage():
    return 'API Server Running'

@app.route('/predict',methods=['get'])
def predict():
    h=int(request.args.get('h'))
    classifier=generate_model('iot.csv')
    result=classifier.predict([[h]])
    return str(result[0])

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)