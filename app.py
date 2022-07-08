from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model_new.pkl','rb'))

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)

    if output == 1:
        out = 'Harga Diprediksi Naik'
    else:
        out = 'Harga Diprediksi Turun'
        
    return render_template('predict.html', prediction_text='{}'.format(out))

@app.route("/predict_page")
def predict():
    return render_template('predict.html')

if __name__ == "__main__":
    app.run()

