from flask import Flask, render_template, url_for


app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About Me')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/soosh')
def soosh():
    return render_template('soosh.html')
