import random

#Pictures
def run():
    hangmanpic = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    #words
    words = [
        "python",
        "javascript",
        "c++",
        "c#",
        "java",
        "rust"
    ]

    #start of the game
    word = random.choice(words)
    attemps = 6
    spaces = ["_"] * len(word)

    #process of the game
    while True:
        print(''.join(spaces))
        print(hangmanpic[attemps])
        choise = input("Select a: ")
        found = False
        for i, character in enumerate(word):
            if choise == character:
                spaces[i] = choise
                found = True
        if found == False:
            attemps -= 1
        #End
        if attemps <= 0:
            print("\n***you lose!!***\n")
            break
        if "_" not in ''.join(spaces):
            print(word)
            print("\n***you win!!***\n")
            break

#?
if __name__ == '__main__':
    run()