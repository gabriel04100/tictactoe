import numpy as np
from game import Game


playing=1
while playing ==1:
    game1=Game()
    while game1.Won == False:
        print("what symbol do you want to play : ")
        symbol=str(input())
        print("what lign")
        lign=int(input())
        print("What column")
        col=int(input())
        game1.place_symbol(symbol,lign,col)
        game1.display_board()


    print("Do you want to play a new game ?")
    print("Yes-1 No -0")
    playing=int(input())






