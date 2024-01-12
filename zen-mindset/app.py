from flask import Flask, render_template
import tkinter as tk

app = Flask(__name__)
# Configure templates directory (optional)
app.template_folder = "templates"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")
if __name__ == "__main__":
    app.run()
