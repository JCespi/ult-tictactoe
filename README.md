# ult-tictactoe
Ultimate Tic Tac Toe Board Game: it is a large tic tac toe with 9 slots, per usual, with individual, tic tac toe games going on in each slot. 
Upon making a move in a certain area (i.e. top right), the opposing player must move in the top right slot of the larger tic tac toe board.
This continues until a player achieves a typical tic tac toe win on the larger board.
    
    Represenation of board:

                ┃        ┃                             ┃        ┃       
           ╋╋   ┃   ╋╋   ┃   ╋╋                   TL   ┃   TM   ┃   TR 
                ┃        ┃                             ┃        ┃        
        ━━━━━━━━╋━━━━━━━━╋━━━━━━━━             ━━━━━━━━╋━━━━━━━━╋━━━━━━━━
                ┃        ┃                             ┃        ┃       
           ╋╋   ┃   ╋╋   ┃   ╋╋                   ML   ┃   MM   ┃   MR
                ┃        ┃                             ┃        ┃
        ━━━━━━━━╋━━━━━━━━╋━━━━━━━━             ━━━━━━━━╋━━━━━━━━╋━━━━━━━━
                ┃        ┃                             ┃        ┃  
           ╋╋   ┃   ╋╋   ┃   ╋╋                   BL   ┃   BM   ┃   BR
                ┃        ┃                             ┃        ┃ 
        
        where TL -> Top Left, MM -> Middle Middle, BR -> Bottom Right, etc.
