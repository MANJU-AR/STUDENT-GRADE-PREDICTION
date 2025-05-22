from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        features = np.array([[
            int(data.get('school', 0)),
            int(data.get('sex', 0)),
            int(data.get('age', 0)),
            int(data.get('address', 0)),
            int(data.get('famsize', 0)),
            int(data.get('Pstatus', 0)),
            int(data.get('Medu', 0)),
            int(data.get('Fedu', 0)),
            int(data.get('Mjob', 0)),
            int(data.get('Fjob', 0)),
            int(data.get('reason', 0)),
            int(data.get('guardian', 0)),
            int(data.get('traveltime', 0)),
            int(data.get('studytime', 0)),
            int(data.get('failures', 0)),
            int(data.get('schoolsup', 0)),
            int(data.get('famsup', 0)),
            int(data.get('paid', 0)),
            int(data.get('activities', 0)),
            int(data.get('nursery', 0)),
            int(data.get('higher', 0)),
            int(data.get('internet', 0)),
            int(data.get('romantic', 0)),
            int(data.get('famrel', 0)),
            int(data.get('freetime', 0)),
            int(data.get('goout', 0)),
            int(data.get('Dalc', 0)),
            int(data.get('Walc', 0)),
            int(data.get('health', 0)),
            int(data.get('absences', 0)),
            int(data.get('G1', 0)),
            int(data.get('G2', 0))
        ]])

        prediction = model.predict(features)[0]
        return render_template('index.html', prediction_text=f'Predicted Final Grade (G3): {prediction:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
