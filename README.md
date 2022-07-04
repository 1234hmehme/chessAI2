# chessAI2

This model is trained using qlearning to play chess or solve puzzles 
The architecture of the model is very simple:
	+ state : The FEN string when white to move or black to move ( only one depending on which side you want your bot plays)
  + action spaces : All the possible moves 
  + reward is devided into 4 parts:
    + Win : 10000
    + Lose : -100
    + Draw : 0 (if you train your model to solve puzzle , draw can be -10 because puzzle often is want you to find a winning move)
    + reward for all moves in one trajectory ( the reason is chess is a complicated game. If you do a traditional way, the times you meet a same  position is very small. So to avoid this I will take all moves into account ( the reward will base on the resilt of last move))
    + pre-trained model : Stockfish ( the most powerfull chess machine ) to help model reduce possile moves and will play against a model


You can try to solve puzzle with my trained model in this [collab file](https://colab.research.google.com/drive/1QFtyeIebwymd1hc9JufXH1CFkhx2oJvr?usp=sharing)
You can also play against my bot (still in development) [here](https://chesshoangminh.herokuapp.com/?fbclid=IwAR2ym7ivm4zHGXWRKc39dI-K03nnlgj1wLw0Qv9RMvT_zB1LWcugw1z8z1c)
( The website is originally built by https://projectworlds.in/artificial-intelligence-project-chess-game-python-flask-with-source-code/ and I just adjust few details and up a bot into website)
