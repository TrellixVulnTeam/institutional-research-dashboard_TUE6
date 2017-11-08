from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/admin')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/7777')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug=True)

