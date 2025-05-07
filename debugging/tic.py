#!/usr/bin/python3
def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Avoid printing separator after the last row
            print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]
    
    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]
    
    # Check for tie
    is_full = all(cell != " " for row in board for cell in row)
    if is_full:
        return True, "Tie"
    
    return False, None

def is_valid_move(board, row, col):
    if not (0 <= row < 3 and 0 <= col < 3):
        return False
    return board[row][col] == " "

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    winner = None
    
    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            if is_valid_move(board, row, col):
                board[row][col] = current_player
                game_over, winner = check_winner(board)
                
                if not game_over:
                    # Switch player only if the game is not over
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter valid numbers for row and column!")
        except IndexError:
            print("Row and column must be 0, 1, or 2!")
    
    # Final board state
    print_board(board)
    
    # Announce result
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

if __name__ == "__main__":
    tic_tac_toe()
