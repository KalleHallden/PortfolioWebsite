
from flask import Flask, render_template, url_for
import urllib, json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from flask import Flask,redirect


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

@app.route('/latest-youtube-video')
def lastest_video():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.youtube.com/kallehallden/videos")
    
    wait = WebDriverWait(driver, 3)
    visible = EC.visibility_of_element_located
    
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    return redirect(driver.current_url, code=302)

    
if __name__ == "__main__":
    app.run(debug=True)

