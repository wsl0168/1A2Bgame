# -*- coding: utf-8 -*-

"""This code is user playing 1A2B game with computer.
User and computer will each select four different digits as target and try to guess each others targets. 
The response A means there's a right number at the right position, B means there's a right number at the wrong position.
For example, if the guess is 1234 and the target is 1320, the response should be 1A2B.
After each game, user can choose to play again or end the program.
""" 

import game_functions as gf
import game_class as gc
        
play = 'y'

while play == 'y':
    print("Welcome to the 1A2B game! Please choose four different digits, remeber it or write it down, this will be the target for computer to guess.")
    game = gc.ABguess()
    ua = ub = ca = cb = 0
    while ua != 4 and ca != 4 and len(game.candidate) > 0:
        
        # user guess computer's target
        user_guess = input("Please enter your guess: ")
        while not gf.check_no_duplicate(user_guess) or len(user_guess) != 4:
            user_guess = input("You entered an invalid number, please enter again: ")
        ua, ub = game.input_user_guess(int(user_guess))
        print("The result of your guess: ",ua,"A",ub,"B")
        
        # computer guess user's target
        computer_guess = game.output_computer_guess()
        print("Computer guessed: ","%04d" % computer_guess)
        user_report = input("Please enter A and B for computer's guess (ex: 1A2B): ")
        while len(user_report) != 4 or user_report[1] != 'A' or user_report[3] != 'B':
            user_report = input("You entered an invalid result, please enter again: ")
        ca = int(user_report[0])
        cb = int(user_report[2])
        game.renew_candidates(computer_guess,ca,cb)
        
    if ua == 4:
        if ca == 4:
            print("Tie!")
        else:
            print("You win!")
    elif ca == 4:
        print("Computer win...")
        print("The number your are guessing is: ","%04d" % game.target)
    else:
        print("The AB results you provided were not consistent.")
    
    play = input("Play again?(y/n)")