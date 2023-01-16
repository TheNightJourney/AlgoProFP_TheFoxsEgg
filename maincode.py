from reusablefunctions import *
from text_art import *
import os
import pandas as pd
from datetime import datetime


def mainMenu():
    
    ### Clear the screen and print out the main menu.
    os.system('cls')
    print('''
==================================================================\n\
|                                                                |\n\
|                    Welcome to the Fox's Egg!    ████           |\n\
|                What would you like to do today?█  ██           |\n\
|                                           ████    ██           |\n\
|            ___________________________██████_______░██         |\n\
|            |[0]  NEW DATA                        | ░██         |\n\
|            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾░██         |\n\
|           ████                      ██░░██      ░░░░██         |\n\
|         ██░░░░██████                ██░░██    ░░░░  ████       |\n\
|         ██ ________________________________________░██████████ |\n\
|          ██|[1]  VIEW / EDIT YOUR FINANCES        |██░░░░░░░░░ |\n\
|          ██‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾░░██░░░░░░░ |\n\
|          ██░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░ |\n\
|          ██░░      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░ |\n\
|          ██________________________________________████░░░░░░░ |\n\
|            |[2] DOWNLOAD DATA                     |░░  ██░░░░░ |\n\
|            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾░    ██░░░░░|\n\
|             ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      ██░░░░░|\n\
|             ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██  --    ██░░░░█|\n\
|               ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██  --   ██████░ |\n\
|               ██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██ --   ██░░░░░░░|\n\
|                 ████  ░░░░░░░░░░░░░░░░░░░░░░░░░░--  ██░░░░░░░░░|\n\
|  ____________     ██    ░░██████░░░░░░░░░░░░░░    ██░░  ░░░░░░░|\n\
|  |[3] GUIDE |   ██  -----     ████░░░░░░░░░░    ██  ░░  ░░     |\n\
|  ‾‾‾‾‾‾‾‾‾‾‾‾      ██  ------            ██  ████  ░░          |\n\
|  ____________        ██    ----              ██  ██            |\n\
|  |[5] EXIT  |          ██████████████████████    ██            |\n\
|  ‾‾‾‾‾‾‾‾‾‾‾‾       ██        ██        ██                     |\n\
==================================================================\
                                    
_________________                 ||
| [1]  [2]  [3] |===================
|               |''')
    menu_choice = int(input(("|______[ ]______|\x1B[9D")))
    os.system('cls')
    
    ### Take the user input for the menu choice.
    try:
        if menu_choice ==  5:
            exit()
        elif menu_choice == 0:
            newData()
        elif menu_choice == 1:
            editData()
        elif menu_choice == 2:
            downData()
        elif menu_choice == 3:
            usageGuide()
        else:
            print("Unknown choice made. Try again.")
            mainMenu()
    except ValueError:
        print("Unknown choice made. Please try again.")
        mainMenu()



def newData():
    
    ### Read the CSV file.
    file_df = pd.read_csv("data/finances.csv")
    most_recent_startbal = file_df.at[file_df.index[-1],'finalbal']
    
    # Initial screen.
    os.system('cls')
    print(data_entry_screen)
    print("    ||")
    
    # All the variables that will be appended to the CSV file.
    data_date = dateInput()
    data_ioe = ioeInput(data_date)
    if data_ioe == 0:
        str_ioe = "income"
    elif data_ioe == 1:
        str_ioe = "expense"
    data_amount = amountInput(data_date, str_ioe)
    data_notes = notesInput(data_date, str_ioe, data_amount)
    data_amount_str = str(data_amount)
    os.system('cls')
    
    ### Check whether to add or subtract from the balance.
    if data_ioe == 0:
        new_finalBal = most_recent_startbal + data_amount
    elif data_ioe == 1:
        new_finalBal = most_recent_startbal - data_amount
        
    ### Final Data Entry Form
    buildFooterHeader(0.001)
    buildRows(1, 0)
    x = '''|              Alright! Here's the Data Entry form!              |
|       Check over the details, and make sure it's alright!      |\n'''
    type_it_down_uwu(x)
    buildRows(2,0.03)
    print("|        date[yyyy/mm/dd]:   ",data_date,"                          |",sep="")
    buildRows(2,0.03)
    print("|        income / expense:   ",str_ioe.ljust(7," "),"                             |",sep="")
    buildRows(2,0.003)
    print("|        amount:             IDR ",data_amount_str.ljust(9," "),"                       |",sep="")
    buildRows(2,0.03)
    print("|        notes:              ",data_notes.ljust(34, " "),"  |",sep="")
    buildRows(2,0.03)
    print("|----------------------------------------------------------------|")
    buildRows(2, 0.03)
    print("|        starting balance:  IDR ",(str(most_recent_startbal)).ljust(9, " "),"                      |")
    buildRows(2, 0.03)
    print("|        ending balance:    IDR ",(str(new_finalBal)).ljust(9, " "),"                      |")
    buildRows(3,0.03)
    buildFooterHeader(0.001)
    y = int(input("\nIs this the correct data? Enter [0] for Yes, and [1] for No: "))
    if y == 1:
        input("That's alright. Press Enter to reset the form and try again.")
        mainMenu()
    elif y == 0:
        new_data = {'date': [data_date], 'startingbal': [most_recent_startbal], 'flow': [str_ioe], 'amount': [data_amount],\
            'finalbal': [new_finalBal], 'notes': [data_notes]}
        new_file_df = pd.DataFrame(new_data)
        file_df = pd.concat([file_df, new_file_df], ignore_index=True)
        file_df.to_csv('data/finances.csv', index=False)
        print("Addition Success! Here's the inputted data:\n")
        print("=============================================")
        print(file_df.iloc[-1])
        print("=============================================")
        if new_finalBal < 0:
            print("Also, quick note. That's a negative balance, so I would suggest working that out.")
            time.sleep(2)
        mainMenu()
        



def editData():
    
    file_df = pd.read_csv("data/finances.csv")
    
    print(\
'''
==================================================================\n\
|                          The Fox's Egg                         |\n\
|                  Your Finances for this Period                 |\n\
''')
    buildFooterHeader(0)
    ### Print a new row and divider for each entry. Caps at 11 to ensure no screen overflowing.
    i_val = 1
    for index, row in file_df[['date', 'startingbal', 'flow','amount','finalbal']].iterrows():
        print("| ",row,"|")
        buildFooterHeader(0)
        i_val += 1
        if i_val >11:
            pass
    print("\n")
    x = int(input("To clear the app, enter [0]. To return to the main menu, enter [1]: "))
    if x == 0:
        ### Deletes everything except the initial entry, which is the format.
        file_df = file_df.iloc[[0]]
        file_df.to_csv("data/finances.csv",index=False)
        input("Done! Press Enter to Continue.")
        mainMenu()
    elif x == 1:
        mainMenu()
    else:
        mainMenu()
    
    


def downData():
    
    ### Gets the current date and time to show what the
    ### date is on the saved CSV file.
    
    file_df = pd.read_csv("data/finances.csv")
    
    current_date = datetime.now()
    
    date_time = current_date.strftime("%m_%d_%Y")
    
    file_direc = "previous_data/"
    
    file_df.to_csv(file_direc + "finances_" + date_time + ".csv", index=False)
    
    down_count = 0
    
    while down_count != 3:
        
        os.system('cls')
        
        downloadAnimation()
        
        time.sleep(2)
        
        down_count += 1
    
    os.system('cls')
    
    print(fox_logo_saved)
        
        
        
        
        
        
    
    input("File saved! Press enter to continue.")
    
    mainMenu()



def usageGuide():
    
    ### Basic Usage Guide.
    
    os.system('cls')
    print("Press Enter to go to the next text.\n")
    x = "This, unfortunately, is not some complicated app.\n\
While designed to be a 'replace-it-all' financial\n\
application, it really just is a daily finance tracker.\n\
There are plans to implement importing from other banks\n\
and e-wallet apps, but for now, the input is manual.\n"
    type_it_down_uwu(x)
    input("")
    y = "Currently, 'Add Data', 'Clear Data', and\n\
'View Data' are the only three implementations. Any\n\
misinput will close the app, so be sure to enter \
the right values.\n"
    type_it_down_uwu(y)
    input("")
    z = "Thanks for your patronage! This app is in the early\n\
stages, so expect a bug or two!\n"
    type_it_down_uwu(z)
    input("\nPress Enter to return to the Main Menu.")
    mainMenu()
    
    



def usageGuideAsk():
    
    ### Ask if the user wants a guide on the app on launch.
    
    os.system('cls')
    print(header_slash_footer)
    buildRows(11,0)
    print(
'''|         Would you like a guide on using the Fox's Egg?         |
|                                                                |
|                Press Y for Yes, and N for No.                  |''')
    buildRows(11,0)
    print(header_slash_footer)
    x = input("What will it be?: ")
    if len(x) == 1:
        if x.lower() == "y":
            usageGuide()
        elif x.lower() == "n":
            mainMenu()
        else:
            print("\nSomething went wrong. Please try again.")
            input("Enter to continue...")
            os.system('cls')
            usageGuideAsk()
    else:
        print("\nMore than a single value entered. Try again.")
        input("Enter to continue...")
        os.system('cls')
        usageGuideAsk()
    

    
    
def dateInput():
    
    # Date input
    
    data_date = input("    === enter the date of transaction: ")
    
    ### Will check if the format is correct. If not, the app closes.
    
    if not format_check(data_date, '%Y/%m/%d'):
        print("\nSomething went wrong.\n\
              Please ensure the date is in the format YYYY/MM/DD.")
        input("Please press enter to continue...")
        exit()
    else:
        return data_date



def ioeInput(data_date):
    
    ### Check if Income or Expense so amount can be added/subtracted from balance.
    
    os.system('cls')
    buildFooterHeader(0)
    buildRows(1, 0)
    print('''|              Alright! Here's the Data Entry form!              |
|           Take your time filling it, no need to rush.          |''')
    buildRows(2,0)
    print("|        date[yyyy/mm/dd]:   ",data_date,"                          |",sep="")
    print('''|                                                                |
|                                                                |
|        income / expense:                                       |
|                                                                |
|                                                                |
|        amount:                                                 |
|                                                                |
|                                                                |
|        notes:                                                  |
|                                                                |
|                                                                |
|----------------------------------------------------------------|
|                                                                |
|                                                                |
|        starting balance:                                       |
|                                                                |
|                                                                |
|        final balance:                                          |
|                                                                |
|                                                                |
==================================================================
    ||
    ||''')
    print("    ||  === [0] for income, [1] for expense.")
    data_ioe = int(input("    ||  === income or expense?: "))
    try:
        if data_ioe == 0:
            return data_ioe
        elif data_ioe == 1:
            return data_ioe
        else:
            print("An error occured. Closing.")
            exit()
    except ValueError:
        print("An unknown value was added. Please press Enter and try again.")
        exit()



def amountInput(data_date, str_ioe):
    
    ### Input the amount of money spent.
    
    os.system('cls')
    buildFooterHeader(0)
    buildRows(1, 0)
    print('''|              Alright! Here's the Data Entry form!              |\n\
|           Take your time filling it, no need to rush.          |''')
    buildRows(2,0)
    print("|        date[yyyy/mm/dd]:   ",data_date,"                          |",sep="")
    buildRows(2,0)
    print("|        income / expense:   ",str_ioe.ljust(7," "),"                             |",sep="")
    print('''|                                                                |
|                                                                |
|        amount:                                                 |
|                                                                |
|                                                                |
|        notes:                                                  |
|                                                                |
|                                                                |
|----------------------------------------------------------------|
|                                                                |
|                                                                |
|        starting balance:                                       |
|                                                                |
|        final balance:                                          |
|                                                                |
|                                                                |
==================================================================
    ||
    ||''')
    try:
        data_amount = int(input("    === enter the amount you earned / spent: "))
        if data_amount == 999999999:
            os.system('cls')
            print("That's... I-... awesome, I guess? I look forward to the note.")
        elif data_amount > 999999999:
            os.system('cls')
            print("That's great, but I cannot handle that much. Forgive me for that.")
            words_written_2 = "(Wish I could, but the system won't work. So please don't.)"
            type_it_down_uwu(words_written_2)
            time.sleep(1.5)
            exit()
        else:
            pass
        return data_amount
    except ValueError:
        print("Something went wrong. Closing.")
        exit()
        
        
        
def notesInput(data_date, str_ioe, data_amount):
    
    ### Extra notes function for later use, maximum of 28 characters.
    
    os.system('cls')
    data_amount_str = str(data_amount)
    buildFooterHeader(0)
    buildRows(1, 0)
    print('''|              Alright! Here's the Data Entry form!              |\n\
|           Take your time filling it, no need to rush.          |''')
    buildRows(2,0)
    print("|        date[yyyy/mm/dd]:   ",data_date,"                          |",sep="")
    buildRows(2,0)
    print("|        income / expense:   ",str_ioe.ljust(7," "),"                             |",sep="")
    buildRows(2,0)
    print("|        amount:             IDR ",data_amount_str.ljust(9," "),"                       |",sep="")
    print(
'''|                                                                |
|                                                                |
|        notes:                                                  |
|                                                                |
|                                                                |
|----------------------------------------------------------------|
|                                                                |
|                                                                |
|        starting balance:                                       |
|                                                                |
|                                                                |
|        final balance:                                          |
|                                                                |
|                                                                |
==================================================================
   ||
   ||''')
    data_notes = input("    === Enter your notes [ MAX 28 CHARACTERS ]: ")
    if len(data_notes) > 28 or len(data_notes) < 0: 
        input("\nUnfortunately, that's a bit much. Closing.")
        exit()
    else:
        return data_notes
    