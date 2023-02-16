from flask import Flask, render_template
import requests


blog_url = "https://api.npoint.io/06e77261250810e905f8"
response = requests.get(blog_url)
posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_posts():
    """
    This function will get all the preview posts information on the home page
    """
    return render_template('index.html', all_posts=posts)


@app.route('/about')
def get_about():
    """
    When clicking on the "about" section, the user will receive the "about.html" file and its information
    """
    return render_template('about.html')


@app.route('/contact')
def get_contact():
    """
    When clicking on the "contact" section, the user will receive the "contact.html" file and its information
    """
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
