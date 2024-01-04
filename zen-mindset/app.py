from flask import Flask, render_template

app = Flask(__name__)

# Configure templates directory (optional)
app.template_folder = "templates"


course = 'Zen Mindset'
print(course.upper())
print(course.lower())

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
