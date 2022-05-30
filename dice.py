import random
ok = True
while ok:
    answer = input("Type 'y' if you want to roll the dice : ")
    if answer == "y":
        number = random.randint(1, 6)
        if number == 1:
            print("[     ]")
            print("[  *  ]")
            print("[     ]")
        elif number == 2:
            print("[  *  ]")
            print("[     ]")
            print("[  *  ]")
        elif number == 3:
            print("[  *  ]")
            print("[  *  ]")
            print("[  *  ]")
        elif number == 4:
            print("[ * * ]")
            print("[     ]")
            print("[ * * ]")
        elif number == 5:
            print("[*   *]")
            print("[  *  ]")
            print("[*   *]")
        elif number == 6:
            print("[ * * ]")
            print("[ * * ]")
            print("[ * * ]")
    else:
        ok = False
