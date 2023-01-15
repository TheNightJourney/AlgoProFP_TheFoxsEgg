from text_art import *
from reusablefunctions import *
import os
import time


# WELCOME LOGO ANIMATION FUNCTION

def welcomelogo():
    os.system('cls')
    time.sleep(3)
    buildFooterHeader(0.03)
    buildRows(28, 0.05)
    buildFooterHeader(0.03)
    os.system('cls')
    delete_last_line()
    print(fox_logo)
    time.sleep(3)
    os.system('cls')
    return 0



### TO CHECK THE TERMINAL SIZE 

def termCheck():
    os.system('cls')
    print("Hello! The recommended viewing size is at least 68 columns and 37 rows.")
    print("Try to have that minimum value, though any larger value is alright.")
    print("You can check your current setting by entering 0, and continuing when entering 1.")
    print("\n")
    try:
        termsize_input = int(input("Please enter your choice: "))
        if termsize_input == 0:
            
            ### Check what the terminal size is, and return to the user.
            
            bakuwidth = os.get_terminal_size().columns
            dekurow = os.get_terminal_size().lines
            print("\nYour terminal width is currently ",bakuwidth,", and your terminal height is ",dekurow,".",sep="")
            input("Press Enter to continue...")
            termCheck()
        elif termsize_input == 1:
            
            ### Check if the terminal size is optimal.
            
            bakuwidth = os.get_terminal_size().columns
            dekurow = os.get_terminal_size().lines
            if bakuwidth < 68 or dekurow < 37:
                print("\nYour screen is still too small to continue for optimal viewing.")
                input("Press Enter to continue.")
                termCheck()
            elif bakuwidth == 68 and dekurow == 37:
                print("\nThat's... exactly the optimal setup. That's pretty cool, huh.")
                print("Alright, thanks, and have fun!")
                time.sleep(3)
                return 0
            else:
                print("\nAlright, that's an optimal setup.\nThanks for understanding!")
                time.sleep(2)
                return 0
    except ValueError:
        print("\nInvalid input. Please try again.")
        input("Press Enter to continue...")
        termCheck()
        


### NAME CALL FUNCTION

def checkUser():
    os.system('cls')
    buildFooterHeader(0.03)
    buildRows(9, 0.05)
    checktext1 = "|       So, may we know who we're dealing with today? :D         |\n"
    checktext2 = "|        Please keep the name between 8 - 22 characters!         |\n"
    type_it_down_uwu(checktext1)
    buildRows(1, 0.05)
    print("|            _______________________________________             |")
    time.sleep(0.00001)
    print("|            | _                                   |             |")
    time.sleep(0.00001)
    print("|            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾             |")
    buildRows(1, 0.0002)
    type_it_down_uwu(checktext2)
    buildRows(12, 0.03)  
    buildFooterHeader(0.03)
    print("\n")
    user_no_namae = input("Awaiting user input: ")
    os.system('cls')
    if len(user_no_namae) < 8 or len(user_no_namae) > 22:
        os.system('cls')
        buildFooterHeader(0.03)
        buildRows(10, 0.05)
        failed_name_check = "|          Well that won't work. Can we try that again?          |\n"
        type_it_down_uwu(failed_name_check) 
        time.sleep(0.03)
        buildRows(15, 0.05)
        buildFooterHeader(0.03)
        time.sleep(2.5)
        checkUser()
    else:
        print(header_slash_footer)
        buildRows(12, 0)
        print("|            _______________________________________             |")
        print("|            | ",user_no_namae.center(36, " "),"|             |", sep="")
        print("|            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾             |")
        buildRows(1, 0.)
        print("|              Is this the correct name you entered?             |")
        buildRows(13, 0)
        print(header_slash_footer)
        print("\n")
        print(controlTop.center(66, " "))
        making_sure = int(input("|______[ ]______|\x1B[9D"))
        os.system('cls')
        try:
            if making_sure == 1:
                        buildFooterHeader(0.01)
                        buildRows(12, 0)
                        print("|            _______________________________________             |")
                        print("|            | ",user_no_namae.center(36, " "),"|             |", sep="")
                        print("|            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾             |")
                        buildRows(1, 0.03)
                        print("|", ("Alright, welcome " + user_no_namae + "!").center(64, " "),"|", sep="")
                        buildRows(13, 0.03)
                        buildFooterHeader(0.01)
            elif making_sure == 0:
                checkUser()
            else:
                print("well, you typed something wrong. let's... try that again.")
                checkUser()
        except ValueError:
            print("well, you typed something wrong. let's... try that again.")
            checkUser()
            
            
        
        
