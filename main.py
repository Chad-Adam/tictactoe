import board
import random
import time
running = True


print(board.logo)
time.sleep(2)

while running:
    print(board.call_board())
    player_choice = input("Please Choose a Grid Location!")
    board.draw_choice(player_choice)
    if board.check_tt():
        time.sleep(1)
        running = False

    if running:
        print("Cpu Thinking..")
        time.sleep(1)
        print("Cpu Chose.")
        board.cpu_choice(random.randrange(0, 8))
        if board.check_tt():
            time.sleep(1)
            running = False
