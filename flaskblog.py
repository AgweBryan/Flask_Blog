from flask import Flask #importing the flask class Flask
from flask import render_template # importing render template to render html
from flask import flash
from flask import url_for # used for css files
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from flask import redirect
from datetime import datetime

app = Flask(__name__) # createing an instance of the Flask class (__name__) is a special name in python
app.config['SECRET_KEY'] = '4c646ca7670c07c818b8093121c3c326'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # How to print this class. Similar to the toString() method
    def __repr__(self) -> str:
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'


# Class to hold our posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self) -> str:
        return f'User("{self.title}", "{self.date_posted}", "{self.image_file}")'

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
def about_page():
    return render_template('about.html', title='About page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm();
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm();
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page')
            )
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)