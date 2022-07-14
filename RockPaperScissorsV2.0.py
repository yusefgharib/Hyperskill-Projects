import random


class RockPaperScissors:

    def __init__(self):
        self.player_points = 0
        self.original_score = 0
        self.name = input('Enter your name: ')
        print(f'Hello, {self.name}!')
        self.scores = []
        self.dict_score = {}
        options = input('\nEnter the options you want separated by a comma with no space (or press enter for classic '
                        'gameplay)\n\n')
        self.options = ['rock', 'paper', 'scissors']
        self.options = options.split(',') if options != '' else self.options
        print('Okay, let\'s start!')

    def game(self):
        print('**type !exit to exit or !rating for score**\n')
        while True:
            player_move = input('Pick your move!\n')
            if player_move in self.options:
                computer_move = random.choice(self.options)
                index = self.options.index(player_move)
                new_sort = [options for options in self.options if options != player_move]
                new_sort = new_sort[index:] + new_sort[0: index]
                losses = [new_sort[i] for i in range(round(len(new_sort) / 2), len(new_sort))]
                wins = [new_sort[i] for i in range(round(len(new_sort) / 2))]
                if computer_move == player_move:
                    print(f'\nThere is a draw ({computer_move})')
                    self.player_points += 50
                elif computer_move in wins:
                    print(f'\nSorry, but the computer chose {computer_move}')
                elif computer_move in losses:
                    print(f'\nWell done. The computer chose {computer_move} and failed')
                    self.player_points += 100
            elif player_move == '!exit':
                print('\nBye!')
                self.write_scoreboard()
                break
            elif player_move == '!rating':
                print(f'\nYour rating: {self.player_points}')
            else:
                print('Invalid input')

    def check_name(self):
        try:
            with open('scoreboard.txt', 'r') as f:
                lines = f.read()
                names = lines.split(' ')
                for name in names:
                    self.scores.append(name.split(':'))
                f.close()
            for score in self.scores:
                self.dict_score[score[0]] = int(score[1])
            if self.name in self.dict_score:
                self.original_score = self.dict_score[self.name]
                self.player_points += self.dict_score[self.name]

        except FileNotFoundError:
            pass

    def write_scoreboard(self):
        if self.name not in self.dict_score and self.dict_score:
            with open('scoreboard.txt', 'a') as f:
                f.write(f' {self.name}:{self.player_points}')
                f.close()
        elif not self.dict_score:
            with open('scoreboard.txt', 'w') as f:
                content = f'{self.name}:{self.player_points}'.strip(' ')
                f.write(f'{self.name}:{self.player_points}'.strip(' '))
                f.close()
        else:
            f = open('scoreboard.txt', 'r')
            content = f.read()
            f.close()
            content = content.replace(f'{self.name}:{self.original_score}', f'{self.name}:{self.player_points}')
            with open('scoreboard.txt', 'w') as f:
                f.write(content)
                f.close()


g = RockPaperScissors()
g.check_name()
g.game()
