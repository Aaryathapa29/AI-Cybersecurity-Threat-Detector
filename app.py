from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/check_url', methods=['POST'])
def check_url():

    url = request.form['url']

    # Temporary detection logic
    suspicious_keywords = [
        "login",
        "verify",
        "bank",
        "secure",
        "update"
    ]

    result = "SAFE"

    for word in suspicious_keywords:
        if word in url.lower():
            result = "SUSPICIOUS URL DETECTED"

    return render_template(
        'dashboard.html',
        result=result,
        url=url
    )

if __name__ == '__main__':
    app.run(debug=True)