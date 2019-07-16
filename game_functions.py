# -*- coding: utf-8 -*-

import random

def num2list(num):
    ain = [0] * 4
    for i in range(4):
        ain[i] = num // 10**i % 10
    return ain

def check_no_duplicate(ain):
    for i in range(len(ain)):
      if ain[i] in ain[i+1:]:
          return False
    return True

def Initialize_candidates():
    avail = list(range(10**4))
    ind = 0
    while ind < len(avail):
        if not check_no_duplicate(num2list(avail[ind])):
            avail.remove(avail[ind])
        else:
            ind = ind + 1
    return avail

def get_rand_num(inlist):
    return(inlist[random.randint(0,len(inlist)-1)])
    
def check_AB(ain,atar):
    a = 0
    b = 0
    for i in range(len(ain)):
        if ain[i] == atar[i]:
            a = a + 1
        elif ain[i] in atar:
            b = b + 1
    return a,b

def renew(guess,a,b,candidate):
    ind = 0
    guess = num2list(guess)
    while ind < len(candidate):
        a_,b_ = check_AB(guess,num2list(candidate[ind]))
        if a != a_ or b != b_:
            candidate.remove(candidate[ind])
        else:
            ind = ind + 1
    return candidate