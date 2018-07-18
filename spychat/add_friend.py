#Importing packages
from spy_details import Spy
from spy_details import friends
import re

from termcolor import colored

def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)
#Using Regular Expressions
    new_friend.name = raw_input("Please add your friend's name: ")
    pattern_n = '^[a-zA-Z\s]+s'
    if re.match(pattern_n,new_friend.name)!=None:
        print" Friend Name entered "
    else:
        print " Please Enter a valid name"
    new_friend.salutation= raw_input("What to call Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input("Age? "))
    new_friend.rating = float(raw_input("Spy rating? "))

    friends.append(new_friend)
    print (colored('Friend Added!', 'magenta'))

    return len(friends)