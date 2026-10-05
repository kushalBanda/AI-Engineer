from flask import Flask,render_template,request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("artifacts/models/model.pkl")

@app.route('/' , methods=['GET' , 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        sepal_length = float(request.form['SepalLengthCm'])
        sepal_width = float(request.form['SepalWidthCm'])
        petal_length = float(request.form['PetalLengthCm'])
        petal_width = float(request.form['PetalWidthCm'])

        input_data = np.array([[sepal_length,sepal_width,petal_length,petal_width]])

        prediction = model.predict(input_data)[0]

    return render_template("index.html" , prediction=prediction)

if __name__=="__main__":
    app.run(host="0.0.0.0" , port=6412 , debug=True)