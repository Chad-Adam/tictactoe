import random

logo = '''888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888'''

r1 = ['-', '-', '-']
r2 = ['-', '-', '-']
r3 = ['-', '-', '-']


def call_board():
    board = f'''       a     b     c
          |     |     
    1  {r1[0]}  |  {r1[1]}  |  {r1[2]}  
     _____|_____|_____
          |     |     
    2  {r2[0]}  |  {r2[1]}  |  {r2[2]}  
     _____|_____|_____
          |     |     
    3  {r3[0]}  |  {r3[1]}  |  {r3[2]}  
          |     |     \n'''
    return board


def draw_choice(choice):
    if choice == "a1":
        if r1[0] != '-':
            print("Location has been selected already!")
            return
        r1[0] = 'X'
        print(call_board())
        return
    elif choice == "a2":
        if r2[0] != '-':
            print("Location has been selected already!")
            return
        r2[0] = 'X'
        print(call_board())
        return
    elif choice == "a3":
        if r3[0] != '-':
            print("Location has been selected already!")
            return
        r3[0] = 'X'
        print(call_board())
        return
    elif choice == "b1":
        if r1[1] != '-':
            print("Location has been selected already!")
            return
        r1[1] = 'X'
        print(call_board())
        return
    elif choice == "b2":
        if r2[1] != '-':
            print("Location has been selected already!")
            return
        r2[1] = 'X'
        print(call_board())
        return
    elif choice == "b3":
        if r3[1] != '-':
            print("Location has been selected already!")
            return
        r3[1] = 'X'
        print(call_board())
        return
    elif choice == "c1":
        if r1[2] != '-':
            print("Location has been selected already!")
            return
        r1[2] = 'X'
        print(call_board())
        return
    elif choice == "c2":
        if r2[2] != '-':
            print("Location has been selected already!")
            return
        r2[2] = 'X'
        print(call_board())
        return
    elif choice == "c3":
        if r3[2] != '-':
            print("Location has been selected already!")
            return
        r3[2] = 'X'
        print(call_board())
        return


def cpu_choice(choice):
    if choice == 0:
        if r1[0] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r1[0] = 'O'
        print(call_board())
        return
    elif choice == 1:
        if r2[0] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r2[0] = 'O'
        print(call_board())
        return
    elif choice == 2:
        if r3[0] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r3[0] = 'O'
        print(call_board())
        return
    elif choice == 3:
        if r1[1] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r1[1] = 'O'
        print(call_board())
        return
    elif choice == 4:
        if r2[1] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r2[1] = 'O'
        print(call_board())
        return
    elif choice == 5:
        if r3[1] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r3[1] = 'O'
        print(call_board())
        return
    elif choice == 6:
        if r1[2] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r1[2] = 'O'
        print(call_board())
        return
    elif choice == 7:
        if r2[2] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r2[2] = 'O'
        print(call_board())
        return
    elif choice == 8:
        if r3[2] != '-':
            print("Location has been selected already!")
            cpu_choice(random.randrange(0, 8))
            return
        r3[2] = 'O'
        print(call_board())
        return


def check_tt():
    if r1[0] == "X" and r2[0] == "X" and r3[0] == "X":
        print("You Win!")
        return True
    if r1[1] == "X" and r2[1] == "X" and r3[1] == "X":
        print("You Win!")
        return True
    if r1[2] == "X" and r2[2] == "X" and r3[2] == "X":
        print("You Win!")
        return True
    if r1[0] == "X" and r2[1] == "X" and r3[2] == "X":
        print("You Win!")
        return True
    if r1[2] == "X" and r2[1] == "X" and r3[0] == "X":
        print("You Win!")
        return True
    if r1[0] == "X" and r1[1] == "X" and r1[2] == "X":
        print("You Win!")
        return True
    if r2[0] == "X" and r2[1] == "X" and r2[2] == "X":
        print("You Win!")
        return True
    if r3[0] == "X" and r3[1] == "X" and r3[2] == "X":
        print("You Win!")
        return True
    if r1[0] == "O" and r2[0] == "O" and r3[0] == "O":
        print("Cpu Wins!")
        return False
    if r1[1] == "O" and r2[1] == "O" and r3[1] == "O":
        print("Cpu Wins!")
        return False
    if r1[2] == "O" and r2[2] == "O" and r3[2] == "O":
        print("Cpu Wins!")
        return False
    if r1[0] == "O" and r2[1] == "O" and r3[2] == "O":
        print("Cpu Wins!")
        return False
    if r1[2] == "O" and r2[1] == "O" and r3[0] == "O":
        print("Cpu Wins!")
        return False
    if r1[0] == "O" and r1[1] == "O" and r1[2] == "O":
        print("Cpu Wins!")
        return False
    if r2[0] == "O" and r2[1] == "O" and r2[2] == "O":
        print("Cpu Wins!")
        return False
    if r3[0] == "O" and r3[1] == "O" and r3[2] == "O":
        print("Cpu Wins!")
        return False

