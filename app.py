from flask import Flask, render_template
import numpy as np

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
        out = 'Anda terkena Liver'
    else:
        out = 'Anda tidak terkena Liver'
        
    return render_template('result_predict.html', prediction_text='{}'.format(out))

"""
@app.route("/predict")
def predict():
   return render_template('predict.html')

if __name__ == "__main__":
    app.run()
"""
