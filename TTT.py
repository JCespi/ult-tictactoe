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
        self.maximizeOTable = {"o" : 1, "x" : -1, "tie" : 0 }
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
    def ai(self, char):
        move = self.bestMove(char)
        i = move[0]
        j = move[1]
        self.board[i][j] = char
        return move
    
    def bestMove(self, char):
        bestScore = float("-inf")
        move = [0, 0]
        for i in range(0, 3):
            for j in range(0, 3):
                #spot available?
                if self.board[i][j] == " ":
                    self.board[i][j] = char
                    score = self.miniMax(-1, float("-inf"), float("inf"), False)
                    #undo move
                    self.board[i][j] = " "
                    if score > bestScore:
                        bestScore = score
                        move[0] = i
                        move[1] = j
        return move
    
    def isSpotAvailable(self, i, j):
        if self.board[i][j] == " ":
            return True
        else:
            return False

    def miniMax(self, depth, alpha, beta, isMaximizing):
        #if current board state is a terminal state:
            #return value of the board
        winner = self.checkIfWinner()
        if depth == 0 or winner:
            if winner:   
                #o (computer) is the maximizing
                value = self.maximizeOTable[winner]
                return value
                
            else:
                if isMaximizing:
                    return float("-inf")
                else:
                    return float("inf")

        if isMaximizing:
            bestScore = float("-inf")
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.isSpotAvailable(i, j):
                        self.board[i][j] = "o"
                        score = self.miniMax(depth - 1, alpha, beta, False)
                        self.board[i][j] = " "
                        bestScore = max(score, bestScore)
                        #------------------------
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
                        #------------------------
            return bestScore
        else:
            bestScore = float("inf")
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.isSpotAvailable(i, j):
                        self.board[i][j] = "x"
                        score = self.miniMax(depth - 1, alpha, beta, True)
                        self.board[i][j] = " "
                        bestScore = min(score, bestScore)
                        #------------------------
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
                        #------------------------
            return bestScore
    #------------------------------
