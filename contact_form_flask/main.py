from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def contact_form():
    if request.method == "POST":
        with open("form.txt", "w") as f:
            f.write(f"Name: {request.form["name"]}, Email: {request.form["email"]}")
    return render_template("contact.html")


app.run(debug=True)