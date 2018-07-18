
from spy_details import friends

from termcolor import colored

def select_friend():
#Selecting Friend
    counter = 1

    for friend in friends:
        print str(counter) + ". " + friend.name + "Age : " + str(friend.age)

        counter = counter + 1

    result = int(raw_input(colored("\nSelect from the list : ", 'blue')))
    return result - 1