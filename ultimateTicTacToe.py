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
from Driver import *
if __name__ == "__main__":
    Driver()   