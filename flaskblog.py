from flask import Flask #importing the flask class Flask
from flask import render_template # importing render template to render html
from flask import flash
from flask import url_for # used for css files
from forms import RegistrationForm, LoginForm
from flask import redirect

app = Flask(__name__) # createing an instance of the Flask class (__name__) is a special name in python

app.config['SECRET_KEY'] = '4c646ca7670c07c818b8093121c3c326'

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

@app.route('/register')
def login():
    form = LoginForm();
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)