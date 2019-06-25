
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # url_for('static', filename='main.css')
    return render_template("main.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
    
if __name__ == "__main__":
    app.run(debug=True)

