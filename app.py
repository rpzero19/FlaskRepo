from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us at contact@example.com.'

if __name__ == '__main__':
    app.run(debug=True)
