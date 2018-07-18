#Importing all the necessary
from read_chat_history import read_chat_history
from read_message import read_message
from send_message import send_message
from add_friend import add_friend
from spy_details import spy
from add_status import add_status
from termcolor import colored
status_message=["Hello","Good Life","Its never too late"]
friends_name=[]
friends_age=[]
friends_rating=[]
friends_is_online=[]
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(colored(question, "blue"))
#starting a function
def start_chat(spy_name,spy_age,spy_rating,spy_status):

     current_staus=None
     spy_name = spy.salutation + " " + spy.name
     if spy_age > 12 and spy_age < 50:
        print (colored("Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating),"blue"))
        show_menu=True
        while show_menu:
            menu_choice="What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choice)
            if len(menu_choice)>0:
                menu_choice=int(menu_choice)
                if menu_choice==1:
                    print(colored("So,the spy wants to add a status....","green"))
                    current_status_message=raw_input("Add status..")
                    current_status_message=add_status(current_status_message)
                elif menu_choice==2:
                    print(colored("So,the spy wants to add a friend....","green"))
                    number_of_friends = add_friend()
                    print "You have %d friends" % (number_of_friends)
                elif menu_choice==3:
                    print(colored("Sshh...spy wants to send a secret message","green"))
                    send_message()
                elif menu_choice==4:
                    print(colored("You want to read the secret message","green"))
                    read_message()
                elif menu_choice==5:
                    print(colored("You want to read the chats","green"))
                    read_chat_history()
                elif menu_choice==6:
                    print(colored("Bye spy","green"))
                    show_menu = False
                else:
                    print"Wrong choice"
#Situation when Y is entered
if existing.upper()=="Y":
    start_chat(spy.name,spy.age,spy.rating,spy.is_online)
#Situation when N is entered
elif existing.upper()=="N":
    spy_salutation = raw_input('What should we call you(Mr or Mrs) ?:')
    spy_name = raw_input('What is your name ?:')
    spy_status=True
    if (len(spy_name) == 0):
        print 'A spy needs a Proper Name'
    else:
         print 'Welcome ' + spy_salutation + ' ' + spy_name + ' glad to meet you'
         spy_age = 0
         spy_rating = 0.0
         spy_online = False
         spy_age = int(raw_input("Enter the age"))
         if (spy_age > 17 & spy_age < 50):
                print"Entered"
         else:
                print"Age error"
         spy_rating = float(raw_input("Enter the rating"))
         if spy_rating > 4.5:
            print" Great Ace..!"
            spy_online = True
            print "Authentication Complete..Welcome" + " " + spy_salutation + " " + spy_name + " age: " + str(
           spy_age) + " rating: " + str(spy_rating)

         elif spy_rating >= 2.5 and spy_rating <= 4.5:
             print"You're the one"
             spy_online = True
             print "Authentication Complete..Welcome " + spy_salutation + " " + spy_name + " age: " + str(spy_age) + " rating: " + str(spy_rating)
         else:
             print"Sorry"
         start_chat(spy_name,spy_salutation,spy_age,spy_status)
else:
    print "Wrong choice"

