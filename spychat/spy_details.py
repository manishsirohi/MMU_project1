#Importing Packages
from termcolor import colored
from datetime import datetime

class Spy:
#Constructor
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
#Default Name
spy = Spy('Anant ', 'Mr.', 20, 5.6)
#Friends Names
friend_one = Spy('Mishra ', 'Mr.', 20, 4.9)
friend_two = Spy('Hari ', 'Mr.', 21, 4.39)
friend_three = Spy('Ram ', 'Mr.', 25, 4.95)


friends = [friend_one, friend_two, friend_three]
