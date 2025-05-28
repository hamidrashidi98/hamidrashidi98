```python
import random
import os
import json

# Initialize the game board
board = ["⬜"] * 9

# Load board state if it exists
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
I'm Hamid Rashidi (he/him), a passionate developer from Iran. Welcome to my GitHub profile! Below, you can play an interactive Tic-Tac-Toe game against the computer! 🚀

## 🎲 Play Tic-Tac-Toe

Click on an empty cell to make your move (X). The computer will respond with O. *Refresh the page after each move to see the updated board!*

|   |   |   |
|---|---|---|
|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=0)|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=1)|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=2)|
|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=3)|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=4)|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=5)|
|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=6)|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=7)|[{}](https://github.com/hamidrashidi98/hamidrashidi98/actions/workflows/update_game.yml/dispatches?move=8)|

*Note*: After clicking a cell, wait a few seconds and refresh the page to see the computer's move. To reset the game, click [here](#).

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
    move = os.getenv("MOVE")  # Get move from GitHub Actions input
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
    else:
        print("No move provided or invalid input.")

if __name__ == "__main__":
    main()
```