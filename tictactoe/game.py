import numpy as np
class Game:
    Won=False
    last_symbol=None
    valid_symbols=['x','o']
    board = np.array([[""] * 3 for i in range(3)])

    def setup(self):
        self.board=[[""]*3 for i in range(3)]

    def display_board(self):
        for lign in self.board:
            for item in lign:
                print('|', end="")
                print(item,end=" ")
            print()

    def  is_valid(self,symbol,i,j):
        if self.Won==False and self.board[i][j]=="" and symbol in self.valid_symbols and symbol != self.last_symbol:
            self.last_symbol=symbol
            return True
        else:
            return False

    def is_won(self):
        diag1=[self.board[i,i] for i in range(3)]
        diag2=[self.board[2-i,i] for i in range(3)]
        if max(max(np.count_nonzero(self.board ==self.last_symbol,axis=0)),max(np.count_nonzero(self.board ==self.last_symbol,axis=0)),np.count_nonzero(diag1 ==self.last_symbol),np.count_nonzero(diag2 ==self.last_symbol)) ==3:
            return True
        else:
            return False
    def place_symbol(self,symbol,i,j):
        symbol=symbol.lower()
        if self.is_valid(symbol,i,j)==True:
            self.board[i][j]=symbol
            self.last_symbol=symbol
            self.Won = self.is_won()
        else:
            print("please try another symbol")