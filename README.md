# **Tic Tac Toe Game**
This is a simple implementation of the Tic Tac Toe game in Python. Players can play against an AI opponent that uses the minimax algorithm to determine the best move.

## Intro
This project provides a console-based Tic Tac Toe game where the player competes against an AI. The AI uses the minimax algorithm with alpha-beta pruning to make optimal decisions.

## Used Algorithms
The AI opponent in this game uses the **minimax algorithm** with **alpha-beta pruning** to determine the best move. 

The minimax algorithm recursively evaluates all possible moves to select the optimal one for the AI while assuming the opponent plays optimally. 

Alpha-beta pruning enhances this by pruning branches of the game tree that cannot affect the final decision, thus reducing the number of nodes evaluated and improving efficiency. This technique ensures the AI makes optimal decisions more quickly by avoiding unnecessary calculations.


## Running the code
To run the Tic Tac Toe game, follow these steps:

```shell
git clone git@github.com:aarjan222/tictactoe.git
cd tictactoe
python3 main.py
```

