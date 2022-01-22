from app import app
from flask import render_template
from app.forms import LoginForm, RegistrationForm, EditProfileForm, CommentForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    return render_template(
        'index.html',
        title='Posts',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template(
        'login.html',
        title='Login',
        form=form
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template(
        'register.html',
        title='Register',
        form=form
    )


@app.route('/user/<username>')
def user(username):
    return render_template(
        'user.html',
        title='User',
        username=username,
    )


@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    return render_template(
        'edit_profile.html',
        title='Edit Profile',
        form=form
    )
