from flask import Flask
import click
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.cli.command()
def start():
    value = click.prompt('Please enter a valid integer', type=int)
    print('your value is')
    print(value)
