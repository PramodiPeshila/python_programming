import random

word_List = ["aardvark" , "baboon" , "camel"]

#randomly select word from the list
chosen_word = random.choice(word_List)
print (chosen_word)

#create the "placeholder" with the same no.of blanks.
placeholder = ""
word_length = len(chosen_word)
for position in range (word_length):
    placeholder += "_"
print(placeholder)

game_over =  False
correct_letters = []
lives = 6

while not game_over:

#guess the letter by user
    guess = input("Guess a Letter: ").lower()

    #check the guessed letter is correct or wrong
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else : 
            display += "_"

    print(display)

if guess not in chosen_word:
    lives -= 1
    if lives == 0 :
        game_over = True
        print("You Lose!")

    if "_" not in display:
        game_over = True
        print("You Won!")