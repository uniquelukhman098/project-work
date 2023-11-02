import numpy as np
from flask import Flask, request, render_template
import pickle

app=Flask(__name__)

model=pickle.load(open("model.pkl",'rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/findthedonor')
def findthedonor():
    return render_template('findthedonor.html')

@app.route('/predict',methods=['POST'])
def predict():
  int_features= [int(x) for x in request.form.values()]
  features=[np.array(int_features)]
  prediction=model.predict(features)

  output = prediction[0]
  return render_template('findthedonor.html',prediction_text='chance of donor to donate blood is {}'.format(output))

if __name__=="__main__":
  app.run(debug=True)

