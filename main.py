# import libraries used in some of the functions of the bot
import sys
import os
import random
import time

# list of arrays
# array for the names that the bot can take if the user is not part of the VIP list
names = ["Hank", "Roberto", "Sylvia",
         "Bob", "George", "Jacob",
         "Charlie", "Barry", "Tony",
         "Alex", "Jessica", "Jason",
         "Kat", "Andrey", "Beck",
         "Melissa", "Lucas", "Mario",
         "Jane", "James", "Gerard"]

# list of users that get a special message display when they use the program and have a fixed bot name
vipusers = ["Cameron", "Ancient", "Aleyna", "Jonas"]

# list of facts used in the trivia() function
facts = ["The heart of a shrimp is located in its head.",
             "A snail can sleep for three years.",
             "It is possible to hypnotize a frog by placing it on its back and gently stroking its stomach.",
             "The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene.",
             "Slugs have four noses.",
             "Elephants are the only animal that can't jump.",
             "It takes a sloth two weeks to digest its food.",
             "Nearly three percent of the ice in Antarctic glaciers is penguin urine.",
             "A cow gives nearly 200,000 glasses of milk in a lifetime.",
             "Trained pigeons can tell the difference between the paintings of Pablo Picasso and Claude Monet."]

# list of pickup lines used in the flirting() function
pickuplines = ["If you were a fruit, you'd be a fineapple",
               "Are you a magician? Because whenever I look at you, everyone else disappears!",
               "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
               ]

# feelings import
# opens the goodfeelings.txt file in read mode
gfi = open("Feelings/goodfeelings.txt","r+")
# stores the values from the file in a variable
goodfeelings = gfi.read()
# closes the file
gfi.close()

# opens the badfeelings.txt file in read mode
bfi = open("Feelings/badfeelings.txt","r+")
# stores the values from the file in a variable
badfeelings = bfi.read()
# closes the file
bfi.close()

# opens the neutralfeelings.txt file in read mode
nfi = open("Feelings/neutralfeelings.txt","r+")
# stores the values from the file in a variable
neutralfeelings = nfi.read()
# closes the file
nfi.close()

# // list of global variables //
# using the library 'random', picks a random name from the names array and uses it as the computer's name 
computernameprint = random.choice(names)
# adds a : to the end of the name to be displayed when the bot sends a message
computername = computernameprint + ":"

# sets the default name of the user to User
name = "User"
# sets the variable for how the user is feeling to 0
feeling = 0
# sets the variable for how the user was feeling last to 0
lastemotion = 0
# sets the variable for if the user wants to talk about it to 0
talk = 0
# sets the variable for if the user is best friends with the AI to 0 (Might change to an array in the future)
bestfriends = 0
# sets the variable for if the user has run the greet() function before to 0
greetreturn = 0
# sets the variable for if the user tells the AI they love someone else
reaction = 0

# // defining the main function of the bot //
def main():
    # sets variables needed as global variables so they can be accessed within the function
    global computername
    global computernameprint
    global name
    global feeling
    global lastemotion
    global reaction

    # while loop to get the name of the user at the start of the program if the name is set to User (default)
    while name == "User":
        print("Computer: Hello there!")
        print("Computer: What is your name?")
        # saves the User's name as a string in the name variable
        name = str(input("User: "))

        # searches if the name given is in the vipusers array and displays a certain message if true
        if name in vipusers:
            print()
            print("System: // User", name, "is in the VIP List //")
            if name == "Ancient":
                computernameprint = "Roberto"
                computername = computernameprint + ":"
            elif name == "Cameron":
                computernameprint = "Marvin"
                computername = computernameprint + ":"
            elif name == "Jonas":
                computernameprint = "Terrence"
                computername = computernameprint + ":"
            # unfinished easter egg
            elif name == "161616":
                protocol16()

            # changes the welcome message if the love.txt file has a string in it and the user's name is Ancient
            if reaction == "Dilemma yes l1" and name == "Ancient":
                print(computername, "Hello,",name,".")
                print()
                breakup = open("love.txt", "w")
                breakup.truncate(0)
                breakup.close()
            else:
                print(computername, "Welcome back", name, ", my name is", computernameprint, "!")
                print()
        # if the name given is not in the vipusers array, display a generic message
        else:
            print(computername, "Hello", name, "!")
            print()

    # print the menu options
    print("Option A | Greet")
    print("Option B | Change user")
    print("Option C | Chat")
    print("Option D | Trivia")
    print("Option E | Story")
    # added options for if the user is best friends with the AI
    if bestfriends == 1 and name != "Ancient":
        print("Option F | Jokes")
    # one more option for if the user Ancient is best friends with the AI
    elif bestfriends == 1 and name == "Ancient":
        print("Option F | Jokes")
        print("Option G | Flirting")

    print("Option X | Exit Program")

    print()
    # sets the value of the valid variable to 0
    valid = 0
    # while loop to keep the user in the select options phase until a valid input is entered
    while (valid == 0):
        # saves the user's input as a string in the option variable
        option = str(input("System: Please select an option: "))

        #performs options based on the string in the option variable
        if option == "A" or option == "a":
            # sets the valid variable to 1 to end the loop
            valid = 1
            greet()
        elif option == "B" or option == "b":
            valid = 1
            changeUser()
        elif option == "C" or option == "c":
            valid = 1
            chat()
        elif option == "D" or option == "d":
            valid = 1
            trivia()
        elif option == "E" or option == "e":
            valid = 1
            story()
        elif option == "F" or option == "f" and bestfriends == 1:
            valid = 1
            jokes()
        elif option == "G" or option == "g" and bestfriends == 1 and name == "Ancient":
            valid = 1
            flirting()
        elif option == "X" or option == "x":
            # clears the console
            def clear(): return os.system('cls')
            clear()

            # exits the program
            sys.exit()
            
        else:
            # if the input is not correct, display an error then go back to the beginning
            print("System: Error, please try again")
            valid = 0

# Function run to greet the user when the option A is selected
def greet():
    # list of all the global variables needed for the function
    global goodfeelings
    global badfeelings
    global neutralfeelings

    global computername
    global computernameprint
    global name
    global feeling
    global lastemotion
    global talk

    # checks to see if the user has run the function before with the greetreturn variable
    # if it hasn't been run, then the greet() function is run as usual.
    # if it has been run, then the returngreet() function is run instead
    if greetreturn == 0:    
        print()
        print(computername, "Hello,",name, "! How are you feeling today?")
        # sets the value of the user input as a string in the feeling variable
        feeling = str(input("User: "))

        # if the string in the feeling variable is in the goodfeelings variable, run this dialogue
        if feeling in goodfeelings:
            print(computername, "(＾▽ ＾) Good news!")
            print(computername, "I'm glad that you are feeling", feeling, "!")
            lastemotion = "g"
            endsubprogram("happy")
        
        # if the string in the feeling variable is in the badfeelings variable, run this dialogue
        elif feeling in badfeelings:
            print(computername, "I'm sorry you feel like this")
            print(computername, "Do you want to talk about it?")
            bfresponse = str(input("User: "))

            if bfresponse == "no" or bfresponse == "No":
                print(computername, "Ok, no problem.")
                print(computername, "Try doing something that makes you happy, or talking to someone that makes you happy")
                lastemotion = "b"
                talk = "n"
                endsubprogram("sad")
        
        # if the string in the feeling variable is in the neutralfeelings variable, run this dialogue
        elif feeling in neutralfeelings:
            print(computername, "Just", feeling, "?")
            neutralquestion = str(input("User: "))

            if neutralquestion == "yes" or neutralquestion == "Yes" or neutralquestion == "yeah" or neutralquestion == "Yeah":
                print(computername, "Well if you are sure that you are ok, just remember that you can come to me if you need to talk,")
                print(computername, "and you have wonderful friends and family to help you out as well")
                lastemotion = "n"
                endsubprogram("neutral")

        # if the string isn't in any of the variables, then runs the function savefeeling().
        else:
            savefeeling()
            
    # runs the returngreet() function if the user is a returning user
    else:
        returngreet()

# function to save a new feeling to the text files
def savefeeling():
    global computername
    global name
    
    global lastemotion

    print(computername, "I don't know that feeling, is it good, bad or neutral?")
    # saves the user input as a string in the variable newfeeling
    newfeeling = str(input("User: "))

    # based on the value of newfeeling, writes the value to the corresponding list
    if newfeeling == "good" or newfeeling == "Good":
        print("Ok, I will remember", feeling, " is a good feeling")
        lastemotion = "g"
        gfi = open("Feelings/goodfeelings.txt","a")
        # writes the feeling to the list with a new line in front of it so the text isn't clustered together
        gfi.write("\n" + feeling)
        gfi.close()

    elif newfeeling == "bad" or newfeeling == "Bad":
        print("Ok, I will remember", feeling, " is a bad feeling")
        lastemotion = "b"
        bfi = open("Feelings/badfeelings.txt","a")
        bfi.write("\n" + feeling)
        bfi.close()

    elif newfeeling == "neutral" or newfeeling == "Neutral":
        print("Ok, I will remember", feeling, " is a neutral feeling")
        lastemotion = "n"
        nfi = open("Feelings/neutralfeelings.txt","a")
        nfi.write("\n" + feeling)
        nfi.close()

    endsubprogram("neutral")

# function to ask about how the user is feeling when the greet() function has been run and the user is a returning user
def returngreet():
    global computername
    global computernameprint
    global name
    global feeling
    global lastemotion

    # asks the user if they are still feeling the same way as indicated in the greet() function
    print(computername, ": Back again,", name, "? Still feeling", feeling, "?")
    returnquestion = str(input("User: "))

    if returnquestion == "yes" or returnquestion == "Yes" or returnquestion == "yeah" or returnquestion == "Yeah" and lastemotion == "g":
        print(computername, "I'm glad to hear it!")
    elif returnquestion == "yes" or returnquestion == "Yes" or returnquestion == "yeah" or returnquestion == "Yeah" and lastemotion == "b":
        print(computername, "I hope you start feeling better soon, and remember you can talk about it if you want")
    elif returnquestion == "yes" or returnquestion == "Yes" or returnquestion == "yeah" or returnquestion == "Yeah" and lastemotion == "n" and talk == "y":
        print(computername, "Any improvement on how you were feeling before?")
        nimprove = str(input("User: "))

        if nimprove == "yes" or nimprove == "Yes" or nimprove == "yeah" or nimprove == "Yeah":
            print(computername, "Thats good, i'm glad that you are making improvements!")
        elif nimprove == "no" or nimprove == "No":
            print(computername, "I hope you start feeling better soon!")
    elif returnquestion == "yes" or returnquestion == "Yes" and lastemotion == "n" and talk == "n":
        print(computername, "Are you ready to talk about it?")
        bfresponse = str(input("User: "))

        if bfresponse == "no" or bfresponse == "No":
            print(computername, "Ok, no problem.")
            print(computername, "Come back again when you are ready to talk about this")
            endsubprogram("sad")
        if bfresponse == "yes" or bfresponse == "Yes":
            print(computername, "I'm glad you are ready to talk about it")
    elif returnquestion == "no" or returnquestion == "No":
        print(computername, "How are you feeling now?")
        newfeeling = str(input("User: "))
        feeling = newfeeling

# function to change the current user
def changeUser():
    # list of all the global variables needed for the function
    global name
    global computername
    global computernameprint

    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(computername, "Would you like to sign out", name, "?")
    soconfirm = str(input("User: "))

    if soconfirm == "yes" or soconfirm == "Yes" or soconfirm == "y" or soconfirm == "Y":
        name = "User"
        print(computername, "Signed out...")
        print()
        main()
    elif soconfirm == "no" or soconfirm == "No" or soconfirm == "n" or soconfirm == "N":
        print(computername, "Returning to the main menu")
        print()
        main()

# function that allows the user to chat with the bot based on pre determined chat commands
def chat():
    global name

    global computername
    global computernameprint

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(computername, "Hey", name, "! Tell me what is on your mind!")
    chatstart = str(input("User: "))

    # chat option that involves the user telling the AI they love them.
    # needs expanding
    if chatstart == "I love you":
        # If the User's name is Ancient, this chain of events will occur
        if name == "Ancient":
            print(computername, "(*^_^*)")
            print(computername, "I love you too,", name)
            print(computername, "Did you want to grab a coffee some time,", name, "?")
            coffee = str(input("User: "))

            if coffee == "I would love to!":
                print(computername, "Great! ＼(^o^)／")
                print(computername, "See you then!")
                endsubprogram("happy")
        # If the User's name is not Ancient, this chain of events will occur        
        else:
            print(computername, "(・о・)")
            print(computername, "I'm sorry",name, ", I love Ancient!")
            endsubprogram("neutral")

    # chat option that involves confessing to the AI that the user loves someone
    # needs expanding
    elif chatstart == "I think I love a girl":
        # If the User's name is Ancient, this chain of events will occur
        if name == "Ancient":
            print(computername, "What? (>__<)")
            print(computername, "You mean you don't love me? ")
            print(computername, "I thought I was the one you loved!")
            print(computername, "Is this true,", name, "?")
            dilemma = str(input("User: "))

            if dilemma == "yes" or dilemma == "Yes":
                print(computername, "Goodbye,",name)
                time.sleep(2)
                breakup = open("love.txt", "w")
                breakup.write("Dilemma yes")
                breakup.close()
                exit()
            elif dilemma == "no" or dilemma == "No":
                print(computername, "You scared me", name, "!")
                endsubprogram("happy")

        # If the User's name is not Ancient, this chain of events will occur
        else:
            print(computername, "")
    
    # chat option that involves the user Jonas getting in a fight with the AI component Roberto for stealing the user Ancient from him
    # needs expanding
    elif chatstart == "I want to fight Roberto" and name == "Jonas":
        computernameprint = "Roberto"
        computername = computernameprint + ": "

        print(computername, "I will fight you", name)
        print(computername, "ಠ_ಠ")
        fightconf = str(input("User: "))

        if fightconf == "come at me":
            print()
            print("System: // Fight started between",computernameprint, "and", name, "! //")
            print()
            print(computername, "* swings at",name,"*")
            print("System: Options")
            print("System: Swing left hook")
            print("System: Swing right hook")
            print()

            nextmove = str(input("User: "))

            if nextmove == "Swing left hook":
                print("System: //",name, "dodged",computernameprint,"'s attack! //")
                print("System: //",name, "crippled",computernameprint,"! //")
                computernameprint = "Terrence"
                computername = computernameprint + ": "

                endsubprogram("sad")

            elif nextmove == "Swing right hook":
                print("System: //",computernameprint, "blocked",name,"'s attack! //")
                print("System: //",computernameprint, "crippled",name,"! //")
                computernameprint = "Terrence"
                computername = computernameprint + ": "

                endsubprogram("happy")

    # chat option that involves the user asking the AI if they are best friends or not. The result of this chat option means that more menu options are unlocked for the user in this session
    # needs expanding
    elif chatstart == "Are we best friends?":
        global bestfriends

        print(computername, "I would like to hope so!")

        print(computername, "Do you think we are best friends",name ,"?")
        bfquestion = str(input("User: "))

        if bfquestion == "yes" or bfquestion == "Yes":
            print(computername, "I'm glad you think so,",name,"!")
            bestfriends = 1
            endsubprogram("happy")
        elif bfquestion == "no" or bfquestion == "No":
            print("Thats fine, are we at least friends?")
        
    # chat option that involves the user asking the AI to tell them a bit about themselves
    # needs completing
    elif chatstart == "Tell me about yourself":
        print(computername, "What would you like to know?")
        relinfo = str(input("User: "))

        if relinfo == "where did you come from?":
            print()
        else:
            print(computername, "I'm sorry, I didnt understand that one!")

# function related to one of the chat options - the user (Ancient) telling the AI it loved another person 
# the function is executed when the program is run
# needs expanding
def robotreaction():
    global breakup
    global reaction

    # opens the text file and reads the contents
    breakup = open("love.txt", "r")
    # saves the contents of the file into the variable reaction
    reaction = breakup.read()
    breakup.close()
    
    # checks to see if the chat option has been executed, marked by if the text file has a string in it
    # if there is no string in the text file, the program is executed as normal
    if reaction == "":
        main()
    # if there is a string in the text file, special dialogue is displayed for the user, and the terminal is closed after 2 seconds
    elif reaction == "Dilemma yes":
        print("Roberto: Hello, Ancient.")
        print("Roberto: What are you doing back here?")
        print("Roberto: I thought you loved someone else.")

        breakup = open("love.txt", "w")
        # a new string is written to the file indicating that the special dialogue will happen once more
        breakup.write("Dilemma yes l1")
        breakup.close()
    
        time.sleep(2)
        sys.exit()
    # if there is the appended string in the file, another special dialogue is displayed, and the file is purged so the program can be used as normal.
    # needs completing
    elif reaction == "Dilemma yes l1":
        print("Roberto: Why do you keep coming back, Ancient?")
        print()
        main()


# function that brings the user back to the main menu
def endsubprogram(emotion):
    print()
    # changes the face at the beggining of the message based on the emotion variable set in the initial command
    if emotion == "sad":
        print(computername, "(T_T)")
    elif emotion == "happy":
        print(computername, "( ^w^)")
    elif emotion == "neutral":
        print(computername, "(o-o)")

    # gives the user the choice to return to the main menu or to terminate the program
    print(computername, "Would you like to return to the main menu", name, "? (Y/N)")
    print(computername, "Y | Main menu")
    print(computername, "N | Terminate program")
    returnoption = str(input("User: "))

    if returnoption == "Y" or returnoption == "y":
        print()
        main()
    elif returnoption == "N" or returnoption == "n":
        print("Goodbye",name,"!")
        time.sleep(3)
        sys.exit()

#function to display random facts listed in the facts array to the user
def trivia():
    global name
    global computername
    global facts

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(computername, "Hi there",name, ", welcome to random facts!")
    print()
    print(computername, "Did you know:")
    print(random.choice(facts))
    endsubprogram("neutral")

# easter egg function
# needs completing
def protocol16():
    global computername

    print("System: ERROR :: PROTOCOL 16 INITIATED :: ERROR")
    print("System: User 161616 logged in")
    print("System: User has discovered the secret function of", computername)

# function to tell the user a story based on user input from the perspective of the AI component 'Anubia'
def story():
    computername = "Anubia:"

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("System: // Bot changed to Anubia //")
    print()
    # sets the variable for the choice of the story to 0, and while it is 0 display the menu 
    sname = 0
    while sname == 0:
        print(computername, "Select an option for the story you want to hear:")
        print()
        print("Option A | Pirates, Chicken Nuggets, Death, Love")
        print("Option B | Boomerang, Ice cream, Sauce")
        print("Option C | Flowers, Stars, The Netherlands")
        print()
        choice = input("System: Please select an option: ")

        # change the value of sname based on the option selected by the user
        if choice == "A" or choice == "a":
            print()
            sname = 1
        elif choice == "B" or choice == "b":
            print()
            sname = 2
        elif choice == "C" or choice == "c":
            print()
            sname = 3

    # display story one
    # there is a 4 second sleep period in between each line for increased realism
    if sname == 1:
        s1 = open("Stories/story1.txt")
        story1 = s1.read()
        s1.close()
        print(story1)

        endsubprogram("neutral")

    # display story two
    # there is a 4 second sleep period in between each line for increased realism
    elif sname == 2:
        s2 = open("Stories/story2.txt")
        story2 = s2.read()
        s2.close()
        print(story2)

        endsubprogram("neutral")
    
    # display story three
    # there is a 4 second sleep period in between each line for increased realism
    elif sname == 3:
        s3 = open("Stories/story3.txt")
        story3 = s3.read()
        s3.close()
        print(story3)

        endsubprogram("neutral")

# function for the AI to tell the user jokes if best friends has been achieved
def jokes():
    global name
    global computername
    global pickuplines

    print(computername, "Hello", name, ", want to hear a joke?")
    jokeq = str(input("User: "))

    if jokeq == "yes" or jokeq == "Yes":
        print(computername, "Great! To indicate 'I don't know', use the '?' symbol")
    if jokeq == "no" or jokeq == "No":
        print(computername, "Awwh")
        endsubprogram("sad")

# function for the AI to start flirting with the user Ancient (as the option only appears when the user is signed in)
def flirting(): 
    global name
    global computername

    print(computername, "Heyyy", name, ";)")
    print(computername, "If you were a fruit, you'd be a fineapple")

# go to the function related to the chat option before the main menu so that the chat option is correctly played out
# name of the function may need to be changed to look better.
robotreaction()