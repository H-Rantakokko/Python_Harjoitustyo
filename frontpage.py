def frontpage():
    from tic_tac_toe import tictactoe
    from hangman import hangman
    #Importing games

    #Telling about the game 
    print("Hello and welcome to the arcade")

    print("You can play two different games.")

    print("If you want to play tic tac toe answer tic")
    print("If you want to play hangman answer hangman")
    #Asking what game player wants to play
    peli=input("Wich game would you like to play? ")

    #If tic, tic tac toe will start
    if peli == "tic":
        tictactoe()

    #if hangman, hangman will start
    elif peli == "hangman":
        hangman()

    #Anything else, asking again
    else:
        ("Something weird happend, try again :)")
        frontpage() 


