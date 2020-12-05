from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'welcome to home page!'


@app.route('/ashish')
def hello_world():
    return 'This is admin page!'

@app.route('/user')
def all_user():
    return 'This web page is for all users'

app.run(debug=True)
