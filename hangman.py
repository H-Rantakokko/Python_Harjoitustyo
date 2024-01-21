def hangman():
        
        from endpage import end
        import random
        #Creating hangman that will be shown during the game
        HANGMAN_PICS = ['''
                +
                |
                |
                |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
                |
                |
                |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
        O       |
                |
                |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
        O       |
        |       |
                |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
        O       |
       /|       |
                |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
        O       |
       /|\      |
                |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
        O       |
       /|\      |
       /        |
                |
        ¤¤¤¤¤¤¤¤¤''','''
        +=======+
        O       |
       /|\      |
       / \      |
                |
        ¤¤¤¤¤¤¤¤¤''']

        #Words that will be used in the game
        words = "vappu jamk python blue green".split()

        #draw random word to player to quess
        def random_word(words):
                Theword=random.randint(0, len(words)-1)
                return words[Theword]

        #What will print in the screen when playing
        def displayletters(wrongletters, correctletters, rightword):
                print(HANGMAN_PICS[len(wrongletters)])
                print ()

                #Print wrong guessed letters
                print("Wrong letters: ", end=" ")
                for letter in wrongletters:
                        print(letter, end=" ")
                print()

                #blanks that show how long the word is
                blanks= "_" * len(rightword)

                #if the right letter is given
                for i in range(len(rightword)):
                        if rightword[i] in correctletters:
                                blanks = blanks[:i] + rightword[i] + blanks[i+1:]
                for letter in blanks:
                        print(letter, end=" ")
                print()

        #What will happen when asking letters
        def inputguess(alreadyguessed):
                while True:
                        guess = input("Guess a letter: ")
                        guess = guess.lower()
                        if len(guess) != 1:
                                print("Please enter only one letter!")
                        elif guess in alreadyguessed:
                                print("You have already given this letter, please try again.")
                        elif guess not in "abcdefghijklmnoppgrstuvwxyz":
                                print("Please enter a letter from english alphabet. ")
                        else:
                                return guess
       #The "game" starts
        print("H A N G M A N")
        wrongletters = " "
        correctletters=" "
        rightword=random_word(words)
        gameisdone= False

        
        while True:
                displayletters(wrongletters, correctletters, rightword)

                #Asking player to guess the word
                guess=inputguess(wrongletters+correctletters)

                #If letter is right
                if guess in rightword:
                        correctletters=correctletters+guess

                        #What happens when player wins.
                        alllettersright = True
                        for i in range(len(rightword)):
                                if rightword[i] not in correctletters:
                                        alllettersright = False
                                        break
                        if alllettersright:
                                print("Gorrect, the right word is ", rightword, " You have won!")
                                gameisdone=True
                #If the letter is wrong
                else:
                        wrongletters=wrongletters+guess

                        #What happens if player loses.
                        if len(wrongletters)==len(HANGMAN_PICS)-1:
                                displayletters(wrongletters, correctletters, rightword)
                                print("You have run out of guesses!" + str(len(wrongletters)-1) + " missed guesses and " + str(len(correctletters)-1) + " correct guesses, the word was " + rightword + " ")
                                gameisdone = True
                #Game is ending
                if gameisdone:
                        break
        #Goes to the endpage and player can choose do they want to play again or stop there.
        end()


        
