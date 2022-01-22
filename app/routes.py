from app import app, db
from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required, login_user, logout_user
from app.forms import LoginForm, RegistrationForm, EditProfileForm, CommentForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = CommentForm()
    return render_template(
        'index.html',
        title='Posts',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {user.username}')
        return redirect(url_for('index'))
    return render_template(
        'login.html',
        title='Login',
        form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! Login to continue')
        return redirect(url_for('login'))
    return render_template(
        'register.html',
        title='Register',
        form=form
    )


@app.route('/user/<username>')
@login_required
def user(username):
    return render_template(
        'user.html',
        title='User',
        username=username,
    )


@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    return render_template(
        'edit_profile.html',
        title='Edit Profile',
        form=form
    )
