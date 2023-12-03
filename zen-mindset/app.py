from flask import Flask, render_template

app = Flask(__name__)

# Configure templates directory (optional)
app.template_folder = "templates"

@app.route("/")
def index():
    return render_template("index.html")
