from flask import Flask #importing the flask class Flask
from flask import render_template # importing render template to render html

from flask import url_for # used for css files

app = Flask(__name__) # createing an instance of the Flask class (__name__) is a special name in python

posts = [
    {
        'author': 'Agwe Bryan',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2022',
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022',
    },
]

# What we type in our browsers
# The decorator @app.route() handles all the routing and the 
# function returns what the specific route returns
@app.route("/")
@app.route("/home ")
def home_page():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About page')


if __name__ == '__main__':
    app.run(debug=True)