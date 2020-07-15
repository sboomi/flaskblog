from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8445011cdfc685cca1e7da707553cbce'

posts = [
    {
        'author': 'Shadi Boomi',
        'title': 'Hello and welcome',
        'content': 'What should I put here',
        'date_posted': 'July 14, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'This is a title',
        'content': 'First post content',
        'date_posted': 'July 15, 2020'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
