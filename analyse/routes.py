"""Contains all the routes that are required for the app's API's or website Functionality

Keep in mind that imports specfic to a seprate function is to be done in its own file
"""



from flask import  render_template, request
from markupsafe import escape
from analyse import app
from analyse.externalFileExample import JokesFunction


@app.route("/")
def Home():
    name = "lallan bhiya"
    return render_template("HomePage.html")

@app.route("/dumb")
def Dumb():
    return "<h1> Setting the Policy As DUMB </h1>"

@app.route("/input")
def inputFourm():
    return(render_template("predict.html"))

@app.route("/output",methods=["POST"])
def predictReq():
    if request.method == 'POST':
        lol = request.form
        
        print(lol) 
        return render_template("Result page.html",value = lol)

@app.route("/<food>/<mood>")
def lol(food,mood):

    string = "When my mood is "+ escape(mood)+ " I eat that Tasty "+ escape(food)

    return "<h1>"+string+"</h1>"



@app.route("/funny")
def funnyJoke():
    return JokesFunction()