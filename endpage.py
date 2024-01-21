#"end" of this game
def end():
    from frontpage import frontpage
    #Asks player do they want to play more?
    print("Do you want to play again or try different game?")
    print("You can return to the start if you answer yes, if you want to stop playing answer no.")
    vastaus=input("yes or no? ")

    #If no game will end
    if vastaus == "no":
        print("Goodbye and thanks for playing :)")
    
    #if yes game will go back to the beginning
    elif vastaus == "yes":
        print("...Starting again...")
        frontpage()
    #Anything else, will ask you again
    else:
        print("Something went wrong plase try again")
        end()
    
