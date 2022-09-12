"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body>
        <section>
            Hi! This is the home page.
        </section>
        <a href="/hello">Take me to the start</a>
      </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():

    answer = request.args.get("game_answer")

#   "yes" here is the value="yes" from compliment.html
    if answer == "yes":
        return render_template("game.html")
    else: 
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():

    name = request.args.get("person")
    hue = request.args.get("color")
    a_noun = request.args.get("noun")
    adjective = request.args.get("adj")

    return render_template(
        "madlib.html", 
        a_person=name, 
        a_color=hue, 
        a_noun=a_noun, 
        a_adj=adjective)




if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
