import random

from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapping():
        return "<b>" + func() + "</b>"

    return wrapping


@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


answer = random.randint(0, 9)

print(answer)


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < answer:
        return f"<h1 style='color:red;'> Your Guess is too low.</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif guess > answer:
        return f"<h1 style='color:blue;'> Your Guess is too high.</h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1 style='color:green;'> Your Guess is correct: {guess}</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


@app.route('/bye')
@make_bold
def bye():
    return "bye"


if __name__ == "__main__":
    app.run(debug=True)
