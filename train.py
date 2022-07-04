# This model is for AI being trained for playing white pieces
import chess
from stockfish import Stockfish

stockfish = Stockfish("C:/Users/USER/Dropbox/My PC (DESKTOP-LPQTGUL)/Downloads/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe")

from IPython.display import clear_output
from time import sleep
import pickle
# YOUR CODE HERE
from collections import defaultdict
import random
from tqdm import tqdm
import random
import numpy as np
alpha = 0.8
gamma = 0.9
episodes = 250
epsilon_init = 1
epsilon_min = 0.01
epsilon_decay_rate = 0.9
def newFen(fen):

    a = fen.split() 
    a = a[:-2]
    a = ' '.join(a)

    return a
def act1(qValues, state, epsilon):
  possibleMoves = list(state.legal_moves )

  q = np.array([qValues[(newFen(state.fen()), action)] for action in possibleMoves])
  k =np.max(q)
  temp = np.where(q == k)[0]

  return possibleMoves[temp[random.randint(0, len(temp)-1)]]
def act(qValues6, state, epsilon):

  stockfish.set_fen_position(state.fen())

  action_temp1 = stockfish.get_top_moves(2)
  if random.random() < epsilon:

                

                  
    action = action_temp1[random.randint(0, len(action_temp1)-1)]["Move"]
    action = chess.Move.from_uci(action)
    return action

  q = np.array([qValues6[(newFen(state.fen()), chess.Move.from_uci(action["Move"]))] for action in action_temp1])
  k =np.max(q)
  temp = np.where(q == k)[0]

  return chess.Move.from_uci(action_temp1[temp[random.randint(0, len(temp)-1)]]['Move'])
def qlearning():
  qValues = defaultdict(float) # biến chứa các giá trị Q Value / Action cần training
  epsilon = epsilon_init

  wins = 0
  

  for _ in tqdm(range(episodes)):
    whiteToPlay = True
    board = chess.Board() # AI will be trained to play from beginning. If you want AI solve puzzle please pass a FEN string into this line (EX: board = chess.Board('1k6/1r6/2b5/8/6R1/4N1PQ/5P1P/1R2R2K w - - 0 1') )

    done = False
    gameIter = []
    gameCheck = ''
    turn = 0



    



    state = newFen(board.fen())
    
    while not done:
      reward = 0

      if whiteToPlay:
        if wins >=10:
          action = act1(qValues, board, epsilon)
        else:



          action = act(qValues, board, epsilon)

        turn +=1
        board.push(action)

        whiteToPlay = False




        if board.is_checkmate():
          gameCheck = 'w'
          wins +=1





          qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] + alpha *1000

          done = True
          gameIter.append((state, action))


        elif board.is_stalemate() or board.is_insufficient_material() or turn == 75:

          gameCheck = 'd'





          qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -100
          done = True
          gameIter.append((state, action))


      else:
        stockfish.set_fen_position(board.fen())

        action1  = stockfish.get_best_move()
        gameIter.append((state, action))
                      

        action1 = chess.Move.from_uci(action1)

        board.push(action1) 


        next_state = newFen(board.fen())


        whiteToPlay = True
        if board.is_checkmate():
          gameCheck = 'l'




          done = True
          qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -alpha *1000 
        if board.is_stalemate() or board.is_insufficient_material() :
          reward = 0
          gameCheck = 'd'



          done = True

          qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -100


        possibleMoves1 = list(board.legal_moves )


        next_QValues = [qValues[(next_state, next_action)] for next_action in possibleMoves1]
        


        try:
          qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] + alpha * (reward + gamma * max(next_QValues))
        except:
          pass

        state = next_state
        



    for (state, action) in gameIter:
      if gameCheck == 'w':

        qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] + 10000


      elif gameCheck == 'l':

        qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] - 1000
      elif gameCheck == 'd':
        
        qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -10



    epsilon = max(epsilon_min, epsilon * epsilon_decay_rate)





 
  return qValues  

qValues2= qlearning()

# This model is for AI being trained for playing black pieces


# import chess
# from stockfish import Stockfish

# stockfish = Stockfish("C:/Users/USER/Dropbox/My PC (DESKTOP-LPQTGUL)/Downloads/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe")

# from IPython.display import clear_output
# from time import sleep
# import pickle
# # YOUR CODE HERE
# from collections import defaultdict
# import random
# from tqdm import tqdm
# import random
# import numpy as np
# alpha = 0.8
# gamma = 0.9
# episodes = 250
# epsilon_init = 1
# epsilon_min = 0.01
# epsilon_decay_rate = 0.9
# def newFen(fen):

#     a = fen.split() 
#     a = a[:-2]
#     a = ' '.join(a)

#     return a
# def act1(qValues, state, epsilon):
#   possibleMoves = list(state.legal_moves )

#   q = np.array([qValues[(newFen(state.fen()), action)] for action in possibleMoves])
#   k =np.max(q)
#   temp = np.where(q == k)[0]

#   return possibleMoves[temp[random.randint(0, len(temp)-1)]]
# def act(qValues6, state, epsilon):

#   stockfish.set_fen_position(state.fen())

#   action_temp1 = stockfish.get_top_moves(2)
#   if random.random() < epsilon:

                

                  
#     action = action_temp1[random.randint(0, len(action_temp1)-1)]["Move"]
#     action = chess.Move.from_uci(action)
#     return action

#   q = np.array([qValues6[(newFen(state.fen()), chess.Move.from_uci(action["Move"]))] for action in action_temp1])
#   k =np.max(q)
#   temp = np.where(q == k)[0]

#   return chess.Move.from_uci(action_temp1[temp[random.randint(0, len(temp)-1)]]['Move'])
# def qlearning():
#   qValues = defaultdict(float) # biến chứa các giá trị Q Value / Action cần training
#   epsilon = epsilon_init

#   wins = 0
  

#   for _ in tqdm(range(episodes)):
#     whiteToPlay = False
#     board = chess.Board() # AI will be trained to play from beginning. If you want AI solve puzzle please pass a FEN string into this line (EX: board = chess.Board('1k6/1r6/2b5/8/6R1/4N1PQ/5P1P/1R2R2K w - - 0 1') )

#     done = False
#     gameIter = []
#     gameCheck = ''
#     turn = 0



    
    
#     stockfish.set_fen_position(board.fen())

#     action2  = stockfish.get_best_move()

                      

#     action2 = chess.Move.from_uci(action2)

#     board.push(action2) 




#     state = newFen(board.fen())
    
#     while not done:
#       reward = 0

#       if not whiteToPlay:
#         if wins >=10:
#           action = act1(qValues, board, epsilon)
#         else:



#           action = act(qValues, board, epsilon)

#         turn +=1
#         board.push(action)

#         whiteToPlay = True




#         # next_state = board.fen()
#         if board.is_checkmate():
#           gameCheck = 'w'
#           wins +=1





#           qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] + alpha *1000

#           done = True
#           gameIter.append((state, action))

#         # state = next_state
#         elif board.is_stalemate() or board.is_insufficient_material() or turn == 75:

#           gameCheck = 'd'





#           qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -100
#           done = True
#           gameIter.append((state, action))


#       else:
#         stockfish.set_fen_position(board.fen())

#         action1  = stockfish.get_best_move()
#         gameIter.append((state, action))
                      

#         action1 = chess.Move.from_uci(action1)

#         board.push(action1) 


#         next_state = newFen(board.fen())


#         whiteToPlay = False
#         if board.is_checkmate():
#           gameCheck = 'l'




#           done = True
#           qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -alpha *1000 
#         if board.is_stalemate() or board.is_insufficient_material() :
#           reward = 0
#           gameCheck = 'd'



#           done = True

#           qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -100


#         possibleMoves1 = list(board.legal_moves )


#         next_QValues = [qValues[(next_state, next_action)] for next_action in possibleMoves1]
        


#         try:
#           qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] + alpha * (reward + gamma * max(next_QValues))
#         except:
#           pass

#         state = next_state
        



#     for (state, action) in gameIter:
#       if gameCheck == 'w':

#         qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] + 10000


#       elif gameCheck == 'l':

#         qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] - 1000
#       elif gameCheck == 'd':
        
#         qValues[(state, action)] = (1 - alpha) * qValues[(state, action)] -10



#     epsilon = max(epsilon_min, epsilon * epsilon_decay_rate)





 
#   return qValues  

# qValues2= qlearning()
