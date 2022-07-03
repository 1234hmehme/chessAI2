from flask import Flask, render_template, request, flash
import pickle
import chess
import _pickle as cPickle
import gzip
def load_zipped_pickle(filename):
    with gzip.open(filename, 'rb') as f:
        loaded_object = cPickle.load(f)
        return loaded_object
qValues = load_zipped_pickle('kkkkkkkk')
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