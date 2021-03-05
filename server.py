from flask import Flask, render_template
import random
import datetime as dt
import requests
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = dt.datetime.today().year
    print(year)
    return render_template("index.html", num=random_number, current_year=dt.datetime.today().year)


def get_name_from_name(name):
    URL = "https://api.agify.io"
    params = {
        "name": name
    }
    response = requests.get(url=URL, params=params).json()
    return response["age"]


def get_gender_from_name(name):
    URL = "https://api.genderize.io"
    params = {
        "name": name
    }
    return requests.get(url=URL, params=params).json()


@app.route("/guess/<string:name>")
def guess_page(name):
    guessed_age = get_name_from_name(name)
    guessed_gender = get_gender_from_name(name)["gender"]
    guessed_gender_probability = get_gender_from_name(name)["probability"]
    return render_template("guess.html", name=name.capitalize(), guessed_age=guessed_age, guessed_gender=guessed_gender, guessed_gender_probability=guessed_gender_probability)


@app.route("/blog/<int:num>")
def blog_page(num):
    print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    # print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
