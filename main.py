import random
import hangman_words
import hangman_stages

print(hangman_stages.hangman_logo)
print("Words are:-",end=" ")
print(hangman_words.word_list)


chosen_word = random.choice(hangman_words.word_list)

# print(chosen_word)
word_length=len(chosen_word)
word_guess=[]

for _ in range(word_length):
    word_guess+="_"

end=False

lives=6

while not end:

    guess = input("Guess a letter:").lower()

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            end=True
            print("you loose")
            break;

    for position in range(word_length):
        if chosen_word[position] == guess:
            word_guess[position]=chosen_word[position]
    print(word_guess)
    print(hangman_stages.stages[lives-1])
    print("lives",lives)

    

    if "_" not in word_guess:
        end=True
        print("you win")


