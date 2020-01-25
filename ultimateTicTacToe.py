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
import collections
#returns hash table object that maps string names to coordinates tuples
    #(i.e. "MR" -> (1, 2))
def initializeHashTable(namesList: list):
    nameTable = collections.defaultdict(tuple)
    row = 0
    column = 0
    for name in namesList:
        nameTable[name] = (row, column)
        column += 1 #increment the column
        if column == 3:
            row += 1   #increment the row
            column = 0 #reset the column
    return nameTable
#------------------------------------------------------------------------------------
#an individual, tictactoe object
class TicTacToe:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        namesList = ["TL", "TM", "TR",
                    "ML", "MM", "MR",
                    "BL", "BM", "BR"]
        self.hashTable = initializeHashTable(namesList)
    #------------------------------
    def printBoard(self):
        print("A more general view: \n")
        for i in range(0, 3):
            for j in range(0, 3):
                print("  ", self.board[i][j], end="   ║" if j != 2 else "")    
            print("")
            print("═══════╬═══════╬═══════" if i != 2 else "")
    #------------------------------
    #puts given character in given position
    #if position is already occupied, returns False
    def makeMove(self, character="z", positionString="empty"):
        #----------------------------------------------------
        #make Move
        if character == "z": #charater check
            print("No x or o entered!")
            return False

        if positionString == "empty": #position check
            # print("No position String entered!")
            return False
    
        if self.checkIfFull(): #is the board full check
            print(" ▞ Sorry, but this board is full! ▞ ")
            return "full"

        tuplePosition = self.hashTable[positionString.upper()]
        
        i = tuplePosition[0]
        j = tuplePosition[1]
        if self.board[i][j] == " ": #if slot is empty
            self.board[i][j] = character.lower()
        else:
            # print("Sorry, that spot is already taken!")
            return False
        #----------------------------------------------------
        #check if anyone has won
        check = self.checkIfWinner()
        full = self.checkIfFull()
        if check == "x" and full:
            self.makeX() #lol doing this makes a board not full
        elif check == "o" and full:
            self.makeO() #doing this makes a board not full
        
        return True
    #------------------------------
    def getCharacter(self, i, j):
        return self.board[i][j]
    #------------------------------
    def makeX(self):
        self.reset("x")
        self.board[0][1] = "-"
        self.board[1][0] = "-"
        self.board[1][2] = "-"
        self.board[2][1] = "-"
    #------------------------------
    def makeO(self):
        self.reset("o")
        self.board[1][1] = "-"
    #------------------------------
    def reset(self, character=" "):
        for row in range(0, 3):
            for column in range(0, 3):
                self.board[row][column] = character
    #------------------------------
    #returns given winning character if there is a winner
    #otherwise returns False
    def checkIfWinner(self):
        rowResult = self.checkRow()
        if rowResult:
            return rowResult

        columnResult = self.checkColumn()
        if columnResult:
            return columnResult

        diagonalResult = self.checkDiagonal()
        if diagonalResult:
            return diagonalResult
        #else:
        return False
    
    def checkRow(self):
        for row in self.board:
            if row[0] != " ": #row cannot be complete with a blank
                if len(set(row)) == 1:
                    return row[0]
        return False

    def checkColumn(self):
        for col in range(0, 3):

            columnArray = [" ", " ", " "]
            i = 0
            for row in self.board:
                columnArray[i] = row[col]
                i += 1

            if columnArray[0] != " ": #column cannot be complete with a blank
                if len(set(columnArray)) == 1:
                    return columnArray[0]
        return False

    def checkDiagonal(self):
        #first diagonal
        diagArray = [" ", " ", " "]
        i = 0
        for d in range(0, 3):
            diagArray[i] = self.board[d][d]
            i += 1
        if diagArray[0] != " ": #diagonal cannot be complete with a blank
            if len(set(diagArray)) == 1:
                return diagArray[0]
        #second diagonal
        diagArray = [" ", " ", " "]
        i = 0
        for d in range(0, 3):
            diagArray[i] = self.board[d][2 - d]
            i += 1
        if diagArray[0] != " ":
            if len(set(diagArray)) == 1:
                return diagArray[0]

        return False   
    #------------------------------
    def checkIfFull(self):
        for row in range(0, 3):
            for column in range(0, 3):
                if self.board[row][column] == " ":
                    return False
        else:
            return True
    #------------------------------

#the ultimate, tictactoe object
class UltimateTicTacToe:
    def __init__(self):
        #---------------------
        #top
        topLeft = TicTacToe()
        # topLeft.reset("0")
        topMiddle = TicTacToe()
        # topMiddle.reset("1")
        topRight = TicTacToe()
        # topRight.reset("2")
        #---------------------
        #middle
        middleLeft = TicTacToe()
        # middleLeft.reset("3")
        middleMiddle = TicTacToe()
        # middleMiddle.reset("4")
        middleRight = TicTacToe()
        # middleRight.reset("5")
        #---------------------
        #bottom
        bottomLeft = TicTacToe()
        # bottomLeft.reset("6")
        bottomMiddle = TicTacToe()
        # bottomMiddle.reset("7")
        bottomRight = TicTacToe()
        # bottomRight.reset("8")
        #---------------------
        #array of these TicTacToe objects
        self.boardArray = [
            [topLeft, topMiddle, topRight],
            [middleLeft, middleMiddle, middleRight],
            [bottomLeft, bottomMiddle, bottomRight]
        ]
        #this is not optimal, but I'm still figuring out Python's scope
        namesList = ["TL", "TM", "TR",
                    "ML", "MM", "MR",
                    "BL", "BM", "BR"]
        self.hashTable = initializeHashTable(namesList)
        #I need a matrix with all of the winners of each section. This is a ticTacToe Object
        self.winnerMatrix = TicTacToe()
    #------------------------------
    def printUltimateBoard(self):
        
        for bigRow in range(0, 3):

            littleRow = 0

            fakeBigColumn = 0 #used to be able to go to other columns of the larger matrix
            for bigColumn in range(0, 3):
                vL = 0
                littleColumn = 0

                for smallColumn in range(0, 11):
                    
                    if smallColumn == 0:
                        print("        ", end="")

                    if vL == 3 and smallColumn == 3:
                        print("     ┃", end="\t  ")
                        # smallColumn -= 1
                        vL = 0
                    elif vL ==3 and smallColumn == 7:
                        print("     ┃", end="\t    ")
                        vL = 0
                    else:
                        vL += 1
                        if fakeBigColumn == 3:
                            fakeBigColumn = 0
                        print("%s   " %(self.boardArray[bigRow][fakeBigColumn].getCharacter(littleRow, littleColumn)), end="┃   " if vL != 3 else "")
                        # print("%s   " %(self.boardArray[bigRow][bigColumn].getCharacter(littleRow, littleColumn)), end="┃   " if vL != 3 else "")

                        littleColumn += 1
                        if littleColumn == 3:
                            #time to reset
                            littleColumn = 0
                            fakeBigColumn += 1

                littleRow += 1

                print("")

                print("     ━━━━━━━╋━━━━━━━╋━━━━━━━     ┃     ━━━━━━━╋━━━━━━━╋━━━━━━━     ┃     ━━━━━━━╋━━━━━━━╋━━━━━━━    " if bigColumn != 2 else "\t\t\t\t ┃\t\t\t\t   ┃")
    

            #the two big, row dividers
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" if bigRow != 2 else "")
    #------------------------------
    #returns True if someone has won the game
    def makeMove(self, character="z", positionString="empty", smallPosString="empty"):
        tuplePosition = self.hashTable[positionString.upper()]
        I = tuplePosition[0]
        J = tuplePosition[1]

        attemptMove = self.boardArray[I][J].makeMove(character, smallPosString)
        if not attemptMove:
            return False
        elif attemptMove == "full":
            return "full"

        #this might not be necessary/not work?
        check = self.boardArray[I][J].checkIfWinner()
        if check == "x":
            self.markAsWon(positionString, "x")
        elif check == "o":
            self.markAsWon(positionString, "o")

        ultimateCheck = self.winnerMatrix.checkIfWinner()
        if ultimateCheck == "x":
            #x has won the game
            return "x"
        elif ultimateCheck == "o":
            #o has won the game
            return "o"
        
        return True
    #------------------------------
    def markAsWon(self, positionString="empty", winningChar="empty"):
        tuplePosition = self.hashTable[positionString.upper()]
        I = tuplePosition[0]
        J = tuplePosition[1]
        if winningChar == "x":
            # self.boardArray[I][J].makeX() 
            self.winnerMatrix.makeMove("x", positionString) #update Winning Array
        elif winningChar == "o":
            self.winnerMatrix.makeMove("o", positionString) #update Winning Array
        else:
            print("No x or o given!")
    #------------------------------
    def printWinnerMatrix(self):
        self.winnerMatrix.printBoard()
    #------------------------------
#------------------------------------------------------------------------------------
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
            
#add a way to control putting spaces before area or between or after
#find a way to undo a move
#fix bug where a board is filled with big x or big o and then moving says that the spot is taken even though it's not
