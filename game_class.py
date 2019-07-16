# -*- coding: utf-8 -*-

import game_functions as gf
        
class ABguess:

    # initialize a list of all four-digit numbers without duplicates and choose one to be guessed by user
    def __init__(self):
        self.candidate = gf.Initialize_candidates()
        self.target = gf.get_rand_num(self.candidate)

    # compare the user's guess with target         
    def input_user_guess(self,guess):
        guess_list = gf.num2list(guess)
        target_list = gf.num2list(self.target)
        a,b = gf.check_AB(guess_list,target_list)
        return a,b
    
    # generate computer's guess
    def output_computer_guess(self):
        cguess = gf.get_rand_num(self.candidate)
        return cguess
    
    # update candidate list 
    def renew_candidates(self,computer_guess,ca,cb):
        self.candidate = gf.renew(computer_guess,ca,cb,self.candidate)
        
    

