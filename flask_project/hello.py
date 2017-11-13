from flask import Flask

app = Flask(__name__)

# Routing

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'


# Variable Rules

@app.route('/user/admin')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/7777')
def show_post(post_id):
    return 'Post %d' % post_id


# Unique URLs / Redirection Behavior

@app.route('/projects/')
def projects():
    # show the user profile for that user
    return 'The project page'

@app.route('/about/')
def about():
    # show the post with the given id, the id is an integer
    return 'The about page'


# HTTP method

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True)

