from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from joblib import dump, load


app = Flask(__name__)

# model=pickle.load(open('model.pkl','rb'))
model = load('./tree_deploy.joblib')


@app.route('/')
def hello_world():
    return render_template("robot_anomaly_detection.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 0)

    if output>str(0.5):
        return render_template('robot_anomaly_detection.html',pred='Your robot is in Danger!!!\nAnomaly detection label is {}'.format(output),bhai="Under Attack!!!")
    else:
        return render_template('robot_anomaly_detection.html',pred='Your robot is safe.\n Anomaly detection label is {}'.format(output),bhai="Safe..")


if __name__ == '__main__':
    app.run(debug=False)
