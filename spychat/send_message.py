#Importing Packages
from select_friend import select_friend

from steganography.steganography import Steganography
from datetime import datetime
from spy_details import friends, ChatMessage

import re

from termcolor import colored

def send_message():
#Choosing Friends
    friend_choice = select_friend()
#Using Regex
    original_image = raw_input("Enter the name of image : ")
    pattern_i = '^[a-zA-Z]+\.jpg$'

    if re.match(pattern_i,original_image)!=None:
        print" Image Name entered "
    else:
        print " Please Enter a valid Image name"
    output_image = raw_input("Provide the name of the output image  : ")
    pattern_o = '^[a-zA-Z]+\.jpg$'

    if re.match(pattern_o,original_image)!=None:
        print" Image Name entered "
    else:
        print " Please Enter a valid Image name"
    text = raw_input("Enter your message here : ")
#Encoding the Message
    Steganography.encode(original_image, output_image, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print (colored("Your message encrypted successfully.", 'red'))
#Dictionary
    new_chat = {
        'message': text,
        'time': datetime.now(),
        'sent_by_me': True
    }

    friends[friend_choice].chats.append(new_chat)
    print (colored("your secret message is ready.",'yellow'))

    # users input validations
    if (re.match(pattern_i, original_image) != None and re.match(pattern_o, output_image) != None):
        print (colored('All perfect','red'))
    else:
        print (colored('Sorry! Invalid entry. We can\'t validate your input and output\n ', 'blue'))
        print (colored('The convention to follow is: \n ', 'blue'))
        print (colored('1. Input should ends with (.jpg) format.\n ', 'blue'))
        print (colored('2. Output should also ends with (.jpg) format.\n ', 'blue'))
        print (colored('Keep in mind and Try Again\n\n ', 'blue'))
