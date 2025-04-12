from flask import Flask, render_template, url_for,request
import pandas as pd
import joblib
import warnings
warnings.filterwarnings
model = joblib.load("linear_regression_model.lb")
app = Flask(__name__)

# Home URL "/", URL or root
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        brand = int(request.form['brand'])
        owner = int(request.form['owner'])
        Kms_driven =int( request.form['Kms_driven'])
        power = int(request.form['power'])
        age = int(request.form['age'])


        unseen_data = [[Kms_driven,owner,age,power,brand]]
        prediction = model.predict(unseen_data)[0]

        return str(round(prediction[0],2))

if __name__ == "__main__":
    app.run(debug=True)
