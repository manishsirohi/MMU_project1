#Importing packages
from select_friend import select_friend
from steganography.steganography import Steganography
from spy_details import friends
from spy_details import spy
from select_message_help import send_message_help
from spy_details import ChatMessage
from  datetime import datetime
import re

from termcolor import colored
from colorama import init

def read_message():
    sender = select_friend()
    encrypted_image = raw_input("Provide encrypted image : ")
    pattern_e = '^[a-zA-Z]+\.jpg$'
    if re.match(pattern_e,encrypted_image)!=None:
        print" Image Name entered "
    else:
        print " Please Enter a valid Image name"

#Decrypting the message
    try:
        secret_message = Steganography.decode(encrypted_image)
        print "The secret message is ",
        print (colored(secret_message, 'red'))
        words = secret_message.split()

        new = (secret_message.upper()).split()

#in case of emergency
        if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new or "ALERT" in new:

            print (colored("!", 'grey', 'on_yellow')),
            print (colored("!", 'grey', 'on_yellow')),
            print (colored("!", 'grey', 'on_yellow'))

            print (colored("The friend who sent this message need your help.", 'cyan'))
            print (colored("You can help your friend by sending helping message.", 'cyan'))
            print (colored("Select the friend to send helping message", 'red'))

        send_message_help()

        print (colored("You just sent a message to help your friend.", 'magenta'))

        new_chat = ChatMessage(secret_message, False)
        friends[sender].chats.append(new_chat)
        print (colored("Your secret message has been saved.", 'cyan'))

    except TypeError:
        print(colored("This image has no secret message. No decoding. Aah!"))

        if (re.match(pattern_e, encrypted_image) != None):
            print (colored('All perfect', 'red'))
        else:
            print (colored('Sorry! Invalid entry. We can\'t validate your input and output\n ', 'blue'))
            print (colored('The convention to follow is: \n ', 'blue'))
            print (colored('1. Encrypted should ends with (.jpg) format.\n ', 'blue'))
            print (colored('Keep in mind and Try Again\n\n ', 'blue'))
