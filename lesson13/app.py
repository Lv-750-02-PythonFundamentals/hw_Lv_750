from flask import Flask, request
from flask.helpers import url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/my')
def get_my():
    return  "my"

# @app.route('/my/<name>/<age>')
# def get_my_name(name, age=18):
#     return  f"my {name} {age}"
@app.route('/my/<name>', defaults={"age": 18})
@app.route('/my/<name>/<age>')
def get_my_name(name, age=18):
    print(request.method)
    print(type(name), name)
    print(type(age), age)
    return render_template("main.html", data={"name": name, "age": age})


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for("get_my_name", name="Anna", age=99))
    app.run(host="0.0.0.0")
