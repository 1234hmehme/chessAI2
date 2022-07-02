from flask import Flask, render_template, request, flash
import pickle
import chess
with open('proo4.pkl','rb') as f:  # Python 3: open(..., 'rb')
    qValues= pickle.load(f)
import numpy as np
def newFen(fen):

    a = fen.split() 
    a = a[:-2]
    a = ' '.join(a)

    return a
import random
def get_move1(fen):
    board = chess.Board(fen)
    possibleMoves = list(board.legal_moves )
    q = [qValues[(newFen(board.fen()), action)] for action in possibleMoves]
    k =np.max(q)
    temp = np.where(q == k)[0]

    return str(possibleMoves[temp[random.randint(0,len(temp)-1)]])

app = Flask(__name__,template_folder='template')

@app.route("/")
def index():
    return render_template("index1.html")
@app.route('/move/<int:depth>/<path:fen>/')
def get_move(depth,fen):


    move = get_move1(fen)

    return move