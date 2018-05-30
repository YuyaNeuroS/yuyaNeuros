def hangman(word):
    wrong=0
    stages=["",
            "__________         ",
            "|                  ",
            "|         |        ",
            "|         o        ",
            "|        /|\       ",
            "|        / \       ",
            "|                  "
            ]
    rletters=list(word)
    bord=["_"]*len(word)
    win=False
    print("Welcome to the hangman")
