from flask import Flask
from flask import redirect, url_for
from flask import request, render_template
import os


# Initiate file paths
parentPath = os.getcwd()
templatePath = f"{parentPath}/templates"
staticPath = f"{parentPath}/static"
imgPath = f"{parentPath}/static/img"
machineModel = f"{parentPath}/model"

# Initiate flask object
# Template folder stores .html files
# Static folder stores .css files
app = Flask(__name__, template_folder=templatePath, static_folder=staticPath)

@app.route("/")
def base():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("extendAbout.html")

@app.route("/testing")
def test():
    return render_template("testing.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
