from flask import Flask, render_template, request, flash
from chessai import *

app = Flask(__name__,template_folder='template')

@app.route("/")
def index():
    return render_template("index1.html")
@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth,fen):


    move = get_move1(fen)

    return move