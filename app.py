from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        birthdate = request.form.get("birthdate")

        return render_template("result4.html", name=name)


    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
