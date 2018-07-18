#Importing Packages
from select_friend import select_friend
from spy_details import friends
from read_message import read_message
from datetime import datetime
from termcolor import colored

def read_chat_history():
    read_chat = select_friend()

    print '\n'

    for chat in friends[read_chat].chats:
#Using DateTime Package
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M"))+ ", ", 'yellow')),
            print (colored("You said: ", 'red')),
            print str(chat.message)
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M"))+ ", ", 'yellow')),
            print (colored(str(friends[read_chat].name)+"You said: ", 'red')),
            print str(chat.message)