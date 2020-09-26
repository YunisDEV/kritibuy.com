from flask import Blueprint, render_template
import json
from .methods import getContentHTML

views = Blueprint('views', __name__,template_folder='../views')


@views.route('/')
def index():
    with open('./src/page_contents/contents_en.json', 'rt') as source:
        h = getContentHTML(json.load(source)['index'])
        return render_template('index.html', htmlFromContent=h)


@views.route('/about')
def about():
    with open('./src/page_contents/contents_en.json', 'rt') as source:
        h = getContentHTML(json.load(source)['about'])
        return render_template('about.html', htmlFromContent=h)


@views.route('/blog')
def blog():
    fetched_blogs = [
        {
            "title": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image": "https://via.placeholder.com/728x400.png"
        },
        {
            "title": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image": "https://via.placeholder.com/728x400.png"
        },
        {
            "title": "Some quick example text to build on the card title and make up the bulk of the card's content.Some quick example text to buildadgadgokpokpokakmglkm",
            "image": "https://via.placeholder.com/728x400.png"
        },
        {
            "title": "Some quick example text to build on the card title aaaaaaaaaaaa make up the bulk of the card's content.",
            "image": "https://via.placeholder.com/728x400.png"
        },
        {
            "title": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image": "https://via.placeholder.com/728x400.png"
        }
    ]
    _blogs = []
    temp = []
    for i in range(len(fetched_blogs)):
        _temp = fetched_blogs[i]
        _temp["title"] = _temp["title"][0:126]
        if len(fetched_blogs[i]["title"]) >= 126:
            _temp["title"] += "..."
        temp.append(_temp)
        if i % 3 == 2:
            _blogs.append(temp)
            temp = []
    _blogs.append(temp)
    print(_blogs)
    return render_template('blog.html', _blogs=_blogs)


@views.route('/contact')
def contact():
    return render_template('contact.html')


@views.route('/pricing')
def pricing():
    with open('./src/page_contents/contents_en.json', 'rt') as source:
        h = getContentHTML(json.load(source)['pricing'])
        return render_template('pricing.html', htmlFromContent=h)


@views.route('/login')
def login():
    return render_template('login.html')


@views.route('/signup')
def signup():
    return render_template('signup.html')