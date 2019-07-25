from flask import Flask, render_template, url_for, flash, redirect
#from Forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

'''posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]'''


@app.route("/")
def home():
    return render_template('index.html',title='index')

@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/news")
def news():
    return render_template('news.html',title='news')

@app.route("/services")
def entertainment():
    return render_template('entertainment.html',title='entertainment')


@app.route("/portfolio")
def sports():
    return render_template('sports.html', title='sports')


@app.route("/contact")
def contact():
   return render_template('contact.html',title='contact')


if __name__ == '__main__':
    app.run(debug=True)

