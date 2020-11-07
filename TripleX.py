import random

class Player:
    def __init__(self):
        self.name = ""

    def enter_name(self):
        self.name = input()

    def get_name(self):
        return self.name

    def guess_code(self):
        self.guess = int(input("Guess a Code: "))
        return self.guess

class TripleX:
    def __init__(self, level_difficulty, max_level_difficulty, player):
        self.difficulty = level_difficulty
        self.max_difficulty = max_level_difficulty
        self.level_complete = False
        self.triplex_player = player

    def print_story(self):
        print("\nHello {}".format(self.triplex_player.get_name()))
        print("You are a secret agent breaking into a level {} secure server room...".format(self.difficulty))
        print("You need to enter the correct codes to continue...\n")

    def generate_code(self):
        return int(round(random.random() % self.difficulty + self.difficulty))

    def calc_code_sum(self, code_a, code_b, code_c):
        return code_a + code_b + code_c

    def calc_code_product(self, code_a, code_b, code_c):
        return code_a * code_b * code_c

    def print_exp_result(self, code_sum, code_product):
        print("+ There are 3 numbers in the code")
        print("+ The codes add-up to: {}".format(code_sum))
        print("+ The codes multiply to give: {}\n".format(code_product))

    def is_level_completed(self, guess_sum, exp_code_sum, guess_product, exp_code_product):
        if(guess_sum == exp_code_sum and guess_product == exp_code_product):
            print("\n*** Well done agent! You have extracted a file! Keep going! ***")
            return True
        else:
            print("\n*** You entered the wrong code! Careful agent! Try again! ***")
            return False

    def play_game(self):
        self.print_story()

        code_a = self.generate_code()
        code_b = self.generate_code()
        code_c = self.generate_code()

        exp_code_sum = self.calc_code_sum(code_a, code_b, code_c)
        exp_code_product = self.calc_code_product(code_a, code_b, code_c)

        self.print_exp_result(exp_code_sum, exp_code_product)

        guess_a = self.triplex_player.guess_code()
        guess_b = self.triplex_player.guess_code()
        guess_c = self.triplex_player.guess_code()

        guess_sum = self.calc_code_sum(guess_a, guess_b, guess_c)
        guess_product = self.calc_code_product(guess_a, guess_b, guess_c)

        return self.is_level_completed(guess_sum, exp_code_sum, guess_product, exp_code_product)

    def run(self):
        print("Welcome to TripleX")
        print("Enter your name to begin")
        self.triplex_player.enter_name()
        random.seed()
        while(self.difficulty <= self.max_difficulty):
            self.level_complete = self.play_game()
            # do I need clear and ignore for invalid chars?

            if(self.level_complete):
                self.difficulty += 1

        print("\n*** Great work agent! You got all the files! Now get out of there! ***\n")

if __name__ == "__main__":
    game_player = Player()
    game = TripleX(1, 5, game_player)

    game.run()
