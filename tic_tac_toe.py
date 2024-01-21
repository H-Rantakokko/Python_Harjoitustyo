#with this game can be played
def tictactoe():
    from endpage import end
    import random

    class TicTacToe:

        def __init__(self):
            self.gameboard = []
            #create gameboard

        def create_gameboard(self):
            for i in range(3):
                row = []
                for j in range(3):
                    row.append('-')
                self.gameboard.append(row)
                #Gameboard size (3*3)

        def firstplayer(self):
            return random.randint(0, 1)
            #Given numbers of players

        def fix_spot(self, row, column, player):
            self.gameboard[row][column] = player
            #Given names to variables that will be used

        #What it will take to win this game:
        def winning(self, player):
            win = None

            n = len(self.gameboard)
            #lenght is 3/3

            for i in range(n):
                win = True
                for j in range(n):
                    if self.gameboard[i][j] != player:
                        win = False
                        break
                if win:
                    return win

            for i in range(n):
                win = True
                for j in range(n):
                    if self.gameboard[j][i] != player:
                        win = False
                        break
                if win:
                    return win

            win = True
            for i in range(n):
                if self.gameboard[i][i] != player:
                    win = False
                    break
            if win:
                return win

            win = True
            for i in range(n):
                if self.gameboard[i][n - 1 - i] != player:
                    win = False
                    break
            if win:
                return win
            return False

        #What happens when all the space on gameboard is taken.
        def gameboard_full(self):
            for row in self.gameboard:
                for item in row:
                    if item == '-':
                        return False
            return True

        #Change between players
        def change_turn(self, player):
            return 'X' if player == 'O' else 'O'

        #Print gameboard
        def show_gameboard(self):
            for row in self.gameboard:
                for item in row:
                    print(item, end=" ")
                print()

        #Basic game with earlier def
        def start(self):
            self.create_gameboard()

            player = 'X' if self.firstplayer() == 1 else 'O'
            while True:
                print(f"Player {player} turn")

                self.show_gameboard()

                row, column = list(
                    map(int, input("Enter row and column numbers to put your mark to the board, leave space between. Like this: 1 1: ").split()))
                print()

                self.fix_spot(row - 1, column - 1, player)

                if self.winning(player):
                    print(f"Player with {player} wins the game!")
                    break

                if self.gameboard_full():
                    print("Tie!")
                    print("Try again if you want to know who wins :)")
                    break

                player = self.change_turn(player)

            print()
            self.show_gameboard()

    #These two play the game
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

    #Goes to the endpage and you can end or start game again.
    end()
          