
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    temp = request.form['temp']
    oxy = request.form['oxy']
    humid = request.form['humid']
    temp=float(temp)
    oxy=float(oxy)
    humid=float(humid)
    
    features = [[oxy,temp,humid]]
    prediction = model.predict_proba(features)
    output=round(prediction[0][1],2)
    output=output*100

    if(output>50):
        return render_template('index.html', message='Forest Fire will Occur' , result='Probablity of Occuring is {} %'.format(output))
    else:
        return render_template('index.html', message='Forest Fire will Not Occur' , result='Probablity of Occuring is {} %'.format(output))


if __name__ == "__main__":
    app.run(debug=True)