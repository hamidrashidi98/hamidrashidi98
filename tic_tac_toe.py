import os
import json
import random

# Initialize the game board
board = ["⬜"] * 9

# Load board state
def load_board():
    global board
    try:
        with open("game_state.json", "r") as f:
            board = json.load(f)
    except FileNotFoundError:
        pass

# Save board state
def save_board():
    with open("game_state.json", "w") as f:
        json.dump(board, f)

# Check for a winner
def check_winner():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "⬜":
            return board[combo[0]]
    if "⬜" not in board:
        return "Draw"
    return None

# Computer makes a random move
def computer_move():
    empty_cells = [i for i, cell in enumerate(board) if cell == "⬜"]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"

# Update README with current board
def update_readme():
    readme_content = """# Welcome to My GitHub Profile!

![Hamid Rashidi SVG](./hamidrashidi.svg)

## Hi there! 🫡🙌 
I'm Hamid Rashidi , a passionate developer from Iran. Welcome to my GitHub profile! Below, you can play an interactive Tic-Tac-Toe game against the computer! 🚀

## 🎲 Play Tic-Tac-Toe

Click on an empty cell (⬜) to place your **X**. The computer will respond with **O**. *Wait a few seconds and refresh the page to see the updated board!*

|   |   |   |
|---|---|---|
|[{}](#move-0)|[{}](#move-1)|[{}](#move-2)|
|[{}](#move-3)|[{}](#move-4)|[{}](#move-5)|
|[{}](#move-6)|[{}](#move-7)|[{}](#move-8)|

<script>
document.querySelectorAll('a[href^="#move-"]').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const move = link.getAttribute('href').split('-')[1];
    fetch(`https://api.github.com/repos/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches`, {
      method: 'POST',
      headers: {
        'Authorization': `token ${localStorage.getItem('github-token') || 'YOUR_PERSONAL_ACCESS_TOKEN'}`,
        'Accept': 'application/vnd.github.v3+json'
      },
      body: JSON.stringify({ ref: 'main', inputs: { move: move } })
    }).then(() => alert('Move sent! Refresh the page in a few seconds.'));
  });
});
</script>

*Note*: After clicking a cell, wait 10-30 seconds and refresh the page to see the updated board. To reset the game, click [here](#reset).

## 🛠️ Skills
- HTML, CSS, JavaScript
- Python
- SVG Animations

## 📫 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/your-linkedin-profile) *(Replace with your LinkedIn URL)*
- [Email](mailto:your.email@example.com) *(Replace with your email)*

Enjoy the game and explore my projects below! 🚀
""".format(*board)

    with open("README.md", "w") as f:
        f.write(readme_content)

# Main logic
def main():
    load_board()
    move = os.getenv("MOVE")  # Get move from workflow input
    if move and move.isdigit():
        move = int(move)
        if 0 <= move <= 8 and board[move] == "⬜":
            board[move] = "X"  # Player's move
            winner = check_winner()
            if not winner:
                computer_move()  # Computer's move
                winner = check_winner()
            save_board()
            update_readme()
            if winner:
                print(f"Game Over! Winner: {winner}")
            else:
                print("Move recorded, board updated.")
        else:
            print("Invalid move!")
    elif move == "reset":
        global board
        board = ["⬜"] * 9
        save_board()
        update_readme()
        print("Game reset!")
    else:
        print("No move provided or invalid input.")

if __name__ == "__main__":
    main()
