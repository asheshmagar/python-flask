from flask import  Flask , render_template
app = Flask(__name__)

data=[
    {
        "title": "Python",
        "bio": "Python is a dynamically interpreted langauge."
    },
    {
        "title": "Java",
        "bio": "Java is an object oriented langauge."
    },
    {
        "title": "c#",
        "bio": "C# os an object oriented langauge of microsoft."
    }
]

@app.route('/')

def hello_world():
    title="Home Page"
    return render_template("index.html",title=title)

@app.route('/lang/<name>')

def lang(name):
    title= name
    lang= next(item for item in data if item["title"].lower()== name.lower())
    return render_template("lang.html",title=title,lang=lang)

@app.route('/about')

def about():
    title="About Us"
    return render_template("about.html",title=title)

@app.route('/contact')

def contact():
    title="Contact Us"
    return render_template("contact.html",title=title)

@app.route('/terms')

def terms():
    title="Terms USe"
    return render_template("terms.html",title=title)


@app.route('/privacy')

def privacy():
    title="Privacy Policy"
    return render_template("privacy.html",title=title)