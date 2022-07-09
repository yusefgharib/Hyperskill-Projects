  import random


class Hangman:

    def __init__(self):
        self.words = ['python', 'java', 'swift', 'javascript']
        self.guesses = []
        self.lives = 8
        self.wins = 0
        self.losses = 0
        self.user = ''
        self.rand_word = random.choice(self.words)
        self.hint = '-' * len(self.rand_word)
        self.tmp = self.rand_word

    def new_game(self):
        self.rand_word = random.choice(self.words)
        self.hint = '-' * len(self.rand_word)
        self.tmp = self.rand_word
        self.lives = 8
        print('H A N G M A N\n')
        self.user = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:\n')

    def results(self):
        print(f"You won: {self.wins} times")
        print(f"You lost: {self.losses} times\n")
        self.new_game()

    def game(self):
        while True:
            letter = input(f'{self.hint}\nInput a letter: \n')
            if len(letter) > 1 or len(letter) == 0:
                print("Please, input a single letter.\n")
            elif letter.isupper() or not letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.\n")
            else:
                if letter in self.rand_word:
                    for i in range(len(self.rand_word)):
                        if self.rand_word[i] == letter:
                            self.hint = self.hint[:i] + letter + self.hint[i + 1:]
                            self.rand_word = self.rand_word.replace(letter, ' ', 1)
                elif letter in self.guesses:
                    print("You've already guessed this letter.\n")
                if letter not in self.tmp:
                    print("That letter doesn't appear in the word\n")
                    self.lives -= 1
                self.guesses.append(letter)
                if self.lives == 0:
                    self.losses += 1
                    print("You lost!")
                    self.user = ''
                    break
                if self.hint in self.words:
                    self.wins += 1
                    print(f"You guessed the word {self.hint}! \nYou survived!\n")
                    self.user = ''
                    break


h = Hangman()
while True:
    if h.user == '':
        h.new_game()
    if h.user == 'play':
        h.game()
    if h.user == 'results':
        h.results()
    if h.user == 'exit':
        break
