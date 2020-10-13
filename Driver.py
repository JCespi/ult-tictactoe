from UTTT import *
#driver class
class Driver:
    def __init__(self):
        """present options for multi or single player games"""
        #the ultimate board
        self.board = UltimateTicTacToe()
        #valid positions on the board
        self.pos_list = ["tl", "tm", "tr",
                         "ml", "mm", "mr",
                         "bl", "bm", "br"]
        #welcome the player(s)
        self.prnt_welcome_msg()
        #present options
        modes = [1, 2, 3]
        mode = input("Please enter a mode: ")
        while int(mode) not in modes:
            mode = input("Please try again. Enter a 1, 2, or 3.")
        #choose the appropriate game
        if mode == "1":
            self.multiplayer()
        elif mode == "2":
            self.singleplayer()
        else:
            exit(0)      
    #----------------------------------
    def prnt_welcome_msg(self):
        #ASCII fun
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
        print("Welcome to Tic Tac Toe")
        print("----------------------")
        print("     1. Play against a friend")
        print("     2. Play against your computer")
        print("     3. Quit")
    #----------------------------------
    def multiplayer(self):
        #assign x and o
        xs_turn = False
        print("▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ \n")
        choice = input(" ► Would you like to be x or o? ")
        while choice != "x" and choice != "o":
            choice = input("► Please enter a valid choice.")   
        if choice == "x":
            xs_turn = True
            print("   Great. You are x and your friend is o. You go first") 
            print("▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ \n")
        else:
            print("   Great. You are o and your friend is x. Don't worry - you can go first")
            print("▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ ▅ \n")

        #print the initial, blank board
        self.board.printUltimateBoard()
        general_pos = ""
        #game loop
        while True:
            try:
                specific_pos = self.make_move(general_pos, xs_turn)
                #print the new board
                self.board.printUltimateBoard()
                #the game might end
                if specific_pos == "finish":
                    print("Great game!")
                    self.board.winnerMatrix.printBoard()
                    break
                #the curr player might not be able to move
                if specific_pos == "forfeit":
                    specific_pos = ""
                #curr player's specific position becomes next players general position
                general_pos = specific_pos
                xs_turn = not xs_turn
                self.board.printWinnerMatrix() #print the general tic tac toe board
            except EOFError:
                print("")
                break
            except KeyboardInterrupt:
                print("")
                break;
    def make_move(self, general_pos, xs_turn):
        print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗")
        #determine which player's turn it is
        if xs_turn:
            print(" player x's turn!")
            character = "x"
        else:
            print(" player o's turn!")
            character = "o"

        #if this is the initialization of the game OR
        #a player forfeited a turn
        if general_pos == "":
            while True:
                general_pos = input(" ► Which general region? ")
                if general_pos.lower() in self.pos_list:
                    break
                else:
                    print(" ▞ That wasn't a valid spot! Try Again! ▚")
        else:
            print(" General region is: ", general_pos)

        #make the move on the board
        while True:
            specific_pos = input(" ► Which more specific region? ")
            #ensure we are given a valid move
            if specific_pos.lower() in self.pos_list:
                outcome = self.board.makeMove(character, general_pos, specific_pos)
                #the general_pos board is full so the turn is forefeited
                if outcome == "full":
                    print(" Sorry but you forfeit your turn")
                    return "forfeit"
                elif outcome:
                    break
                else:
                    print(" ▞ Try Again! ▞ ")
            else:
                print(" ▞ That wasn't a valid spot! Try Again! ▚ ")

        print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝")

        #check in case there is a winner
        if outcome == "x":
            print("X HAS WON THE GAME")
            return "finish"
        elif outcome == "o":
            print("O HAS WON THE GAME")
            return "finish"
        print("")

        #if now winner then return the chosen, specific region
        return specific_pos
    #----------------------------------
    def singleplayer(self):
        pass
    #----------------------------------