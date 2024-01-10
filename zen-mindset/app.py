from flask import Flask, render_template
import tkinter as tk

app = Flask(__name__)

# Configure templates directory (optional)
app.template_folder = "templates"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
