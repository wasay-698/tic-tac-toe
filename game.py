class Tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to repl 3x3 board
        self.current(winner) = None

    def print_board(self):
        #this is just getting the rows....
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + '| ' + ' | ' )
            
            
