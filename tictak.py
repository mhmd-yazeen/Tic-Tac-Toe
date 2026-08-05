def create_board():
    return [ "1","2","3","4","5","6","7","8","9" ]

def print_board(board):
    print("\n")
    print(f"{board[0]}  | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f"{board[3]}  | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f"{board[6]}  | {board[7]} | {board[8]} ")
    print("\n")

def win(board, symbol):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

def draw(board):
    return all(cell in ["X","O"] for cell in board)

def valid_move(board, player_name, symbol):
    while True:
        user_input = input(f"{player_name} ({symbol}) , Enter a cell number : ").strip()
        if not user_input:
            print("Invalid Input: Enter a number between (1 to 9)") 
            continue
        if not user_input.isdigit():
            print("Invalid Input: Only digits are allowed ")
            continue
        position = int(user_input)

        if position < 1 or position > 9:
            print("Invalid Input : Number in between (1 to 9)")
            continue
        index = position - 1
        if board[index] in ["X","O"]:
            print("Invalid Move: The cell is occupied ")
            continue
        return index

def play_game():
    board = create_board()
    current_player = "Player 1"
    current_symbol = "X"

    print("\n\t---- Welcome to Tic-Tac-Toe ---- ")
    while True:
        print_board(board)

        move_index = valid_move(board , current_player, current_symbol )
        board[move_index] = current_symbol

        if win(board , current_symbol):
            print_board(board)
            print(f"(Congratulation {current_player} ({current_symbol}) Wins )")
            break

        if draw(board):
            print_board(board)
            print("Its a Draw , No emty cells ")
            break

        if current_symbol == "X":
            current_player = "Player 2"
            current_symbol = "O"
        else:
            current_player = "Player 1"
            current_symbol = "X"

def main():
    while True:
        play_game()

        play_again = input("\nWould You like to Play another Round? (Yes/No): ").strip().lower()
        if play_again not in ["yes" , "y"]:
            print("\nThanks for playing Tic-Tac-Toe ")
            break
if __name__ == "__main__":
    main()




