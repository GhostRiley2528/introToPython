theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

#  Reference
refBoard = {
    '7': '7', '8': '8', '9': '9',
    '4': '4', '5': '5', '6': '6',
    '1': '1', '2': '2', '3': '3'
}

def printBoard(board):
    print("\nPosition Guide:")
    print(refBoard['7'] + ' | ' + refBoard['8'] + ' | ' + refBoard['9'])
    print('--+---+--')
    print(refBoard['4'] + ' | ' + refBoard['5'] + ' | ' + refBoard['6'])
    print('--+---+--')
    print(refBoard['1'] + ' | ' + refBoard['2'] + ' | ' + refBoard['3'])

    print("\nCurrent Board:")
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

# Main game
def game():
    turn = 'X'
    count = 0

    for i in range(9):
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")
        move = input()

        if move not in theBoard:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nChoose another place.")
            continue

        # Win checker
        if count >= 5:
            win_conditions = [
                ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],
                ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'],
                ['7', '5', '3'], ['1', '5', '9']
            ]
            for condition in win_conditions:
                if theBoard[condition[0]] == theBoard[condition[1]] == theBoard[condition[2]] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print("**** " + turn + " won. ****")
                    return

        # Turn changer
        turn = 'O' if turn == 'X' else 'X'

    # Tie checker
    printBoard(theBoard)
    print("\nGame Over.\n")
    print("It's a Tie!!")

# Run the game
game()
