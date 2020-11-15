import random

level_difficulty = 1
max_level_difficulty = 5

print("Welcome to TripleX")
print("Enter your name to begin")

name = input()

random.seed()
while(level_difficulty <= max_level_difficulty):

    print("\nHello {}".format(name))
    print("You are a secret agent breaking into a level {} secure server room...".format(level_difficulty))
    print("You need to enter the correct codes to continue...\n")

    code_a = int(round(random.random() % level_difficulty + level_difficulty))
    code_b = int(round(random.random() % level_difficulty + level_difficulty))
    code_c = int(round(random.random() % level_difficulty + level_difficulty))

    exp_code_sum = code_a + code_b + code_c
    exp_code_product = code_a * code_b * code_c

    print("+ There are 3 numbers in the code")
    print("+ The codes add-up to: {}".format(exp_code_sum))
    print("+ The codes multiply to give: {}\n".format(exp_code_product))

    guess_a = int(input("Guess a Code: "))
    guess_b = int(input("Guess a Code: "))
    guess_c = int(input("Guess a Code: "))

    guess_sum = guess_a + guess_b + guess_c
    guess_product = guess_a * guess_b * guess_c

    level_complete = False

    if(guess_sum == exp_code_sum and guess_product == exp_code_product):
        print("\n*** Well done agent! You have extracted a file! Keep going! ***")
        level_complete = True
    else:
        print("\n*** You entered the wrong code! Careful agent! Try again! ***")
        level_complete = False

        # do I need clear and ignore for invalid chars?

    if(level_complete):
        level_difficulty += 1

print("\n*** Great work agent! You got all the files! Now get out of there! ***\n")
