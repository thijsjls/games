import random
import time

class PaardenRace:
    def __init__(self):
        self.board = [1, 2, 3, 4] + [' '] * 48
        self.numplayers = 0

        self.horsenames = {1: 'Pony van Knolwijk tot Paardstra', 2: 'Henk', 3: 'Noorderwind', 4: 'Simply the Best'}
        self.horsepos = {1: 0, 2: 1, 3: 2, 4: 3}

        self.playernames = []
        self.player = []
        self.players = {}

        self.form = '''
            \t| %s | %s | %s | %s |
            \t=================
            \t=================
        	| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            \t-----------------
            \t| %s | %s | %s | %s |
            '''

    def printboard(self):
        temp = list(reversed(self.board))
        print(self.form % tuple(temp[0:4] + temp[4:8] + temp[8:12] + temp[12:16] + temp[16:20] + temp[20:24] + temp[24:28] + temp[28:32] + temp[32:36] + temp[36:40] + temp[40:44] + temp[44:48] + temp[48:52]))

    def set_up(self):
        # welcome        
        print('\n\n\n\n\n\n                                   Paarden Race')
        print('                       een zuip-app van Sloet INC.\n\n') 
        print('    Amice! Laten we een partij onredelijk veel fluiten trappen met een pot Paarden Race.\n\n')
        # explain rules

        # get numplayers
        self.numplayers = int(input('    Met hoeveel van uw amices wilt u spelen? '))
        # get player names + bets + possibly name a the betted horse
        self.players = self.get_player_info()

    def get_player_info(self):
        print('\n    Dan nu eens kijken met wie we aan de borreltafel staan.')
        players = {}
        for player in range(self.numplayers):
            # kies naam
            name = input('\n    Amice, zou ik kennis met u mogen maken? ')
            if name in ['HJ1', 'HJ2', 'HJ', 'hj1', 'hj2', 'hj', 'Willem', 'Willie', 'Willy', 'willem', 'willie', 'willy']:
                print('    Waardeloos.')
            else:
                print('    Wat mooi dat u erbij bent amice %s. Ik beloof u, u gaat kotsen vanavond.' % name)
            # kies paard + paardnaam
            horse = int(input('\n    Amice, op welk paard wilt u inzetten, harten (1), klaver (2), ruiten (3) of schoppen (4)? '))
            if horse < 1 or horse > 4:
                while not (horse < 1 or horse > 4):
                    horse = input('\n    Kiest u één van de aangegeven getallen svp.')
            new_name = input('\n    Ah een zeer mooie keuze amice! Wilt u het paard toevallig ook een naam geven? [y/n] \n    Zo niet wordt dit uiteraard voor u geregeld. ')
            if new_name == 'y':
                self.horsenames[horse] = input('\n    Initiatief wordt beloond amice. Hoe moet de knol gaat heten? ')
            # place bet
            bet = input('\n    Dan moet u alleen nog beslissen hoeveel u durft in te zetten. We tellen uiteraard in volle bakken. ')
            # assert players_dict
            players[name] = [horse, bet]
        return players

    def turn(self):
        time.sleep(3)
        # draw card
        # move
        self.move(random.randint(1, 4))
        self.printboard()
        # if 4-in-a-row -> draw sidecard
        for i in range(len(self.board)):
            if (i%4 == 0) and (' ' not in self.board[i:i+3]):
                time.sleep(3)
                print('\n    De paarden zitten dicht op elkaar.')
                self.move_back(random.randint(1, 4))
                self.printboard()
                break
        # commentary

    def move(self, horse):
        print('\n    %s demarreert!' % self.horsenames[horse])
        self.board[self.horsepos[horse]] = ' '
        self.board[self.horsepos[horse] + 4] = horse
        self.horsepos[horse] += 4

    def move_back(self, horse):
        print('\n    %s verliest de controle in de drukte.. wat een prutspaard!' % self.horsenames[horse])
        self.board[self.horsepos[horse]] = ' '
        self.board[self.horsepos[horse] - 4] = horse
        self.horsepos[horse] -= 4

    def check_win(self):
        if self.board[48:52] != [' '] * 4:
            print('\n    Winneeeeeeeee')
            return True
        return False

    def game(self):
        # init: get player info + horsenames
        self.set_up()
        # playturns untill someone wins
        win = False
        while not win:
            win = self.check_win()
            if win:
                break
            self.turn()
        # handle win

def main():
    paardenrace = PaardenRace()
    paardenrace.game()

if __name__ == "__main__":
    main()