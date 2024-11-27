import random

words = ["apple", "banana", "orange", "mango"]

random_word = random.choice(words)

scrambled_word = "".join(random.sample(random_word, len(random_word)))

attemps = 5

print("welcome to the word scramble game")
print(f"try to guess the original word from scrambled word: {scrambled_word}")
print(f"you have {attemps} attemps.\n")

while attemps > 0:
    guess = input("enter your guess: ").strip()
    if not guess:
        print("invalid input, please enter a word")
        continue
    if guess.lower() == random_word:
        print("congratolations you guessed the correct word")
        break
    else:
        attemps -= 1
        if attemps > 0:
            print(f"incorect, try again. you have {attemps} attemps left.")
        else:
            print(f"you're out of attemps, the correct word was: {random_word}.")