coins = 10
counter =0

print ("Welcome! Do you want to play? Cost: 1 coin.")
wants_play = input ("Press S to start.")
if wants_play == "S" or wants_play == "s":
    restart = True
    while coins > 0:
        while restart == True:
            counter += 1
            import random
            luck = random.randint(1,10)
            if 1 <= luck <= 5:
                print ("No luck!")
                coins -= 1
            if 6 <= luck <=10:
                print (f"Lucky you! You get {luck} more coins!")
                coins = coins + luck
            print (f"Coins total: {coins}. Game played {counter} times." )
            another_game = input ("Want to play again? Press S to retry, press X to exit.")
            if another_game == "S" or another_game == "s":
                restart = True
            else:
                restart = False
                exit()
    else:
        print (f"Sorry, you have no more coins to play :( Gamу played {counter} times.")
