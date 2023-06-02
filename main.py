def print_board2(grid):
    for i in range(len(grid)):
        print("  ", end="")
        for j in range(len(grid[0])):
            if ord(grid[i][j][0]) != 88 and ord(grid[i][j][0]) != 79:
                if j != len(grid[0]) - 1:
                    print(" ", end=" | ")
                else:
                    print(" ", end="")
            elif j != len(grid[0]) - 1:
                print(grid[i][j], end=" | ")
            else:
                print(grid[i][j], end="")
        print("")
        if i != len(grid) - 1:
            s = " ---"
            for k in range(len(grid[0]) - 1):
                s += "+---"
            print(s)


def print_board(grid):
    for i in range(len(grid)):
        print("  ", end="")
        for j in range(len(grid[0])):
            if j != len(grid[0]) - 1:
                print(grid[i][j], end=" | ")
            else:
                print(grid[i][j], end="")
        print("")
        if i != len(grid[0]) - 1:
            s = " ---"
            for k in range(len(grid[0]) - 1):
                s += "+---"
            print(s)


def prompt(board):
    """
    prompts the user for input
    """
    print("Select a place to place your identifier")
    print_board(board)
    move_to = input()
    # print(f"@@@ {move_to} {type(move_to)}")
    try:
        inmove_to = int(move_to)
    except:
        print("Error: Invalid input, try again")
        prompt(board)
    # print(f"@@@ {inmove_to} = {type(inmove_to)}")
    return inmove_to


def win(board):
    """
    returns the identifiere of the player who wins
    if none won then returns NONE
    """
    for i in range(len(board)):
        ans = True
        for j in range(len(board[0]) - 1):
            ans = ans and (board[i][j] == board[i][j + 1])
        if ans is True:
            return board[i][0]

    for j in range(len(board[0])):
        ans = True
        for i in range(len(board) - 1):
            ans = ans and (board[i][j] == board[i + 1][j])
        if ans is True:
            return board[0][j]
    assert len(board) == len(board[0])
    ans = True
    for i in range(len(board) - 1):
        ans = ans and (board[i][i] == board[i + 1][i + 1])
    if ans is True:
        return board[0][0]
    ans = True
    for i in range(len(board) - 1):
        ans = ans and (board[i][len(board) - 1 - i] == board[i + 1][len(board) - 2 - i])
    if ans is True:
        return board[len(board) - 1][0]
    return "NONE"


def decode(move, board):
    return [(move - 1) // len(board), (move - 1) % (len(board))]


status = "p"
while status == "p":
    turn = 0
    sample_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    play_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    while ((win(play_board) == "NONE") and (turn != 9) and (status != "e")) is True:
        print(f"Player{turn%2 + 1}: ", end="")
        tmove = prompt(play_board)
        # print(f"@@@ {type(tmove)}")
        move = decode(tmove, sample_board)
        # now move is a array
        # print(f"@@@{move}")
        con1 = play_board[move[0]][move[1]] == "X"
        con2 = play_board[move[0]][move[1]] == "O"
        while (con1 or con2) is True:
            print("Illegal move try again")
            tmove = prompt(play_board)
            # print(f"@@@ {type(tmove)}")
            move = decode(tmove, sample_board)
            con1 = play_board[move[0]][move[1]] == "X"
            con2 = play_board[move[0]][move[1]] == "O"

        play_board[move[0]][move[1]] = "X"
        if turn % 2 == 1:
            play_board[move[0]][move[1]] = "O"
        print_board2(play_board)
        # print("Enter 'p' to play next move or 'e' to exit the game")
        # status = input()
        # while status != "p" and status != "e":
        #    print("Invalid key entered try again")
        #    print("Enter 'p' to play next move or 'e' to exit the game")
        #    status = input()
        turn = turn + 1

    if status == "e":
        exit()
    # game over
    print("Game Over : ", end="")
    winner = win(play_board)
    if winner == "NONE":
        print("The game is a draw")
    elif winner == "X":
        print("Player1 won")
    else:
        print("Player2 won")
    print("Enter 'p' to play again or 'e' to exit the game")
    status = input()
    while status != "p" and status != "e":
        print("Invalid key entered try again")
        print("Enter 'p' to play again or 'e' to exit the game")
        status = input()
