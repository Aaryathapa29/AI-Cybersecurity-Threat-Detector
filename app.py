from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/check_url', methods=['POST'])
def check_url():

    url = request.form['url']

    features = [[
        len(url),
        url.count('.'),
        url.count('-'),
        1 if "https" in url else 0
    ]]

    prediction = model.predict(features)

    result = "SAFE"

    if prediction[0] == 1:
        result = "PHISHING DETECTED"

    return render_template(
        'dashboard.html',
        result=result,
        url=url
    )

if __name__ == '__main__':
    app.run(debug=True)