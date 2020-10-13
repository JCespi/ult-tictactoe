from TTT import *
#the ultimate, tictactoe object
class UltimateTicTacToe:
    def __init__(self):
        #---------------------
        #top
        topLeft = TicTacToe()
        topMiddle = TicTacToe()
        topRight = TicTacToe()
        #---------------------
        #middle
        middleLeft = TicTacToe()
        middleMiddle = TicTacToe()
        middleRight = TicTacToe()
        #---------------------
        #bottom
        bottomLeft = TicTacToe()
        bottomMiddle = TicTacToe()
        bottomRight = TicTacToe()
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
    def make_best_move(self, general_pos):
        #get (i, j) position of appropriate 3 x 3 board
        pair = self.hashTable[general_pos]
        I = pair[0]
        J = pair[1]
        move = self.boardArray[I][J].ai("o")
        #return the region (i.e. "tr") based off of move (i.e. (0,2))
        for key, val in self.hashTable.items():
            if val == move:
                return key
    #------------------------------