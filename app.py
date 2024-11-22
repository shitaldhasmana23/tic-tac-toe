from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Game state
board = [""] * 9
current_player = "X"
winner = None

def check_winner():
    global winner
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            winner = board[combo[0]]
            return winner
    if "" not in board:
        winner = "Draw"
    return winner

@app.route("/")
def index():
    return render_template("tic_tac_toe.html")

@app.route("/move/<int:index>", methods=["GET"])
def move(index):
    global current_player, board, winner
    if board[index] == "" and not winner:
        board[index] = current_player
        winner = check_winner()
        if winner:
            message = f"{winner} wins!" if winner != "Draw" else "It's a draw!"
        else:
            current_player = "O" if current_player == "X" else "X"
            message = f"Player {current_player}'s turn."
    else:
        message = "Invalid move." if winner else "Cell already taken."
    
    return jsonify({"board": board, "message": message})

@app.route("/reset", methods=["GET"])
def reset():
    global board, current_player, winner
    board = [""] * 9
    current_player = "X"
    winner = None
    return jsonify({"board": board})

if __name__ == "__main__":
    app.run(debug=True)
