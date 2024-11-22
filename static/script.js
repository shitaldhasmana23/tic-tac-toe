function makeMove(index) {
    fetch(`/move/${index}`)
        .then(response => response.json())
        .then(data => {
            updateBoard(data.board);
            if (data.message.includes("wins") || data.message.includes("draw")) {
                // If there's a winner or a draw, show the end screen
                showEndScreen(data.message);
            } else {
                // Otherwise, update the message with the current player's turn
                document.getElementById("message").innerText = data.message;
            }
        });
}

function resetGame() {
    fetch(`/reset`)
        .then(response => response.json())
        .then(data => {
            updateBoard(data.board);
            document.getElementById("message").innerText = "New game started!";
            hideEndScreen(); // Hide the end screen if visible
        });
}

function updateBoard(board) {
    const cells = document.getElementsByClassName("cell");
    for (let i = 0; i < cells.length; i++) {
        cells[i].innerText = board[i] ? board[i] : "";
    }
}

// Show the end screen with a win/draw message
function showEndScreen(message) {
    document.getElementById("end-message").innerText = message;
    document.getElementById("end-screen").style.display = "flex";
}

// Hide the end screen
function hideEndScreen() {
    document.getElementById("end-screen").style.display = "none";
}

// Start a new game by calling resetGame()
function newGame() {
    resetGame();
}
