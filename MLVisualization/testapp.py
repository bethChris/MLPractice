# app.py
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('models/trained_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    iris_list = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']
    # Assume your form has input fields named in the list below
    features = [float(request.form[f]) for f in ['sLength', 'sWidth', 'pLength', 'pWidth']]
    
    # Make a prediction using the pre-trained model
    prediction = model.predict([features])

    return render_template('result.html', prediction=iris_list[prediction[0]])

if __name__ == '__main__':
    app.run(debug=True)
