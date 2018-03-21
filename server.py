from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/recommend', methods=['POST'])
def recommend():
    return render_template('/pages/question/question.html')

@app.route('result')
def result():
    return 'result'

@app.route('/user/info/<user_id>')
def userInfo():
    return 'userinfo'

@app.route('house/info/<house_id>')
def houseInfo():
    return 'houseInfo'
