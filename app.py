from flask import Flask, render_template, request
from function import recommendation

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main_page():
    return render_template("index.html")
    
@app.route("/post", methods=['POST'])
def post():
    value = request.form['input'] # 책 이름 입력
    try:
        data = recommendation.recommend(value)
        return render_template("recommendation.html", data=data, title=value)
    except:
        return render_template("no.html")

@app.route("/index.html",)
def move():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run()