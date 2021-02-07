def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "        | ",
              "|       |",
              "|       0",
              "|      /|\ ",
              "|      / \ ",
              "| "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловат на казнь!\n")

    while wrong < len(stages) - 1:
        print()
        guess = input("Угадайте букву:\n")
        if guess in rletters:

            letterInd = rletters.index(guess)
            board[letterInd] = guess
            print("Вы угадали!\n")
            print("".join(board))
            rletters[letterInd] = '$'
        else:
            wrong += 1
            print("Вы не угадали!\n")
            e = wrong + 1
            print("\t\t\t\t\t", "\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы победили!\nЗагадано было слово\n {}".format(word))
            win = True
            break

    if not win:
        print("Вы проиграли!\n")
        print("\t\t\t\t\t", "\n".join(stages))
        print("Загадано было слово\n {}".format(word))


hangman("cat")
