#Ultimate Tic Tac Toe board game
    #it is a large tic tac toe with 9 slots, per usual,
    #with individual, tic tac toe games going on in each slot
    #upon making a move in a certain area (i.e. top right), then
    #the opposing player must move in the top right slot of the larger tic tac toe
    #Represenation of board:

        #         ┃        ┃                             ┃        ┃       
        #    ╋╋   ┃   ╋╋   ┃   ╋╋                   TL   ┃   TM   ┃   TR 
        #         ┃        ┃                             ┃        ┃        
        # ━━━━━━━━╋━━━━━━━━╋━━━━━━━━             ━━━━━━━━╋━━━━━━━━╋━━━━━━━━
        #         ┃        ┃                             ┃        ┃       
        #    ╋╋   ┃   ╋╋   ┃   ╋╋                   ML   ┃   MM   ┃   MR
        #         ┃        ┃                             ┃        ┃
        # ━━━━━━━━╋━━━━━━━━╋━━━━━━━━             ━━━━━━━━╋━━━━━━━━╋━━━━━━━━
        #         ┃        ┃                             ┃        ┃  
        #    ╋╋   ┃   ╋╋   ┃   ╋╋                   BL   ┃   BM   ┃   BR
        #         ┃        ┃                             ┃        ┃ 
        #
        #where TL -> Top Left, MM -> Middle Middle, BR -> Bottom Right, etc.
#------------------------------------------------------------------------------------
from UTTT import *
#the actual game and its rules
def welcome():
    printWelcomeMessage()
    print("Welcome to Tic Tac Toe")
    print("----------------------")
    print("Would you like to play against a Computer or another player?")
    print("▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ \n")
    choice = input(" ► Would you like to be x or o? ")
    if choice == "x":
        print("   Great. You are x and your friend is o. You go first") 
        print("▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ \n")
        return True
    elif choice == "o":
        print("   Great. You are o and your friend is x. Don't worry - you can go first")
        print("▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ \n")
        return False
    else:
        print("Nothing valid entered. Try again") #put in something to try again

def printWelcomeMessage():
    # ╭ ╮
    # ╰ ╯
    # │
    # ┅
     
    print(" ╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮         ╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮          ╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮             ")
    print(" │                       │         │                       │          │                       │             ")
    print(" │                       │         │                       │          │                       │             ")
    print(" ╰┅┅┅┅┅┅┅╮       ╭┅┅┅┅┅┅┅╯         ╰┅┅┅┅┅┅┅╮       ╭┅┅┅┅┅┅┅╯          ╰┅┅┅┅┅┅┅╮       ╭┅┅┅┅┅┅┅╯             ")
    print("         │       │    ╭┅┅╮                 │       │                          │       │           ╭┅┅┅┅┅┅┅╮ ")
    print("         │       │    ╰┅┅╯                 │       │      ╭┅┅┅╮               │       │           │ ╭┅┅┅╮ │ ")
    print("         │       │  ╭┅┅┅┅┅┅╮  ╭┅┅┅┅┅╮      │       │  ╭┅┅┅┅   │  ╭┅┅┅┅┅╮      │       │  ╭┅┅┅┅┅╮  │ ╰┅┅┅╯ │ ")
    print("         │       │  │      │  │ ╭┅┅┅╯      │       │  │ ╭ ╮   │  │ ╭┅┅┅╯      │       │  │ ╭ ╮ │  │  ╭┅┅┅┅╯ ")
    print("         │       │  │      │  │ ╰┅┅┅╮      │       │  │ ╰ ╯   │  │ ╰┅┅┅╮      │       │  │ ╰ ╯ │  │  ╰┅┅┅┅╮ ")
    print("         ╰┅┅┅┅┅┅┅╯  ╰┅┅┅┅┅┅╯  ╰┅┅┅┅┅╯      ╰┅┅┅┅┅┅┅╯  ╰┅┅┅┅┅╯┅╯  ╰┅┅┅┅┅╯      ╰┅┅┅┅┅┅┅╯  ╰┅┅┅┅┅╯  ╰┅┅┅┅┅┅┅╯ ")

def movePrompt(board, stringPositionLarge="", bool=None):
    print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗")
    if bool:
        print(" player x's turn!")
        character = "x"
    else:
        print(" player o's turn!")
        character = "o"

    namesList = ["tl", "tm", "tr",
                 "ml", "mm", "mr",
                 "bl", "bm", "br"]

    if stringPositionLarge == "":
        while True:
            stringPositionLarge = input(" ► Which general region? ")
            if stringPositionLarge.lower() in namesList:
                break
            else:
                print(" ▞ That wasn't a valid spot! Try Again! ▚")
    else:
        print(" General region is: ", stringPositionLarge)


    while True:

        stringPositionSmall = input(" ► Which more specific region? ")
        if stringPositionSmall.lower() in namesList:
            #if valid make the move
            outcome = board.makeMove(character, stringPositionLarge, stringPositionSmall)
            if outcome == "full":
                print(" Sorry but you forfeit your turn")
                # break
                return "forfeit"
            elif outcome:
                break
            else:
                print(" ▞ Try Again! ▞ ")

        else:
            print(" ▞ That wasn't a valid spot! Try Again! ▚ ")
        

    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝")
    if outcome == "x":
        print("X HAS WON THE GAME")
        return "finish"
    elif outcome == "o":
        print("O HAS WON THE GAME")
        return "finish"
    print("")
    board.printUltimateBoard()
    return stringPositionSmall


def main():
    choice = welcome()
    print("")
    ultimateBoard = UltimateTicTacToe()
    ultimateBoard.printUltimateBoard()
    stringPositionLarge = ""
    while True:
        try:
            newGeneralPosition = movePrompt(ultimateBoard, stringPositionLarge, choice)
            if newGeneralPosition == "finish":
                print("Great game!")
                ultimateBoard.winnerMatrix.printBoard()
                return
            elif newGeneralPosition == "forfeit":
                newGeneralPosition = ""
            #elif newGeneralPosition === "yoItsFull": stringPositionLarge = ""

            stringPositionLarge = newGeneralPosition
            choice = not choice
            ultimateBoard.winnerMatrix.printBoard()  
        except EOFError:
            print("")
            break
    

if __name__ == "__main__":
    main()     