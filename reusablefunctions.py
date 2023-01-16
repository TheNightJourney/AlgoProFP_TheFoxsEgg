import time
import sys
import datetime

### Quick reusable function to build the "===" header.

def buildFooterHeader(delay):
    uwu_header = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
        " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
        " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
        " ", " ", "=", " ", " ", " ", " ", " ", " ", " ", 
        " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", 
        " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    uwu_count = 0
    uwu_editpos = 3
    while uwu_count != 34:
        delete_last_line()
        uwu_header[uwu_editpos+uwu_count] = "="
        uwu_header[uwu_editpos-uwu_count] = "="
        print(''.join(map(str, uwu_header))) 
        uwu_count += 1
        time.sleep(delay)


### Function to build the vertical borders.

def buildRows(number_of_rows, animation_delay):
    owo_count = 0
    while owo_count != number_of_rows:
        print("|                                                                |")
        owo_count += 1    
        time.sleep(animation_delay)
        
### Function to delete the last written line.        

def delete_last_line():
    
    # Move the cursor up one line.
    sys.stdout.write('\x1b[1A')
    # Delete everything from the cursor to the end of the line.
    sys.stdout.write('\x1b[2K')
    
### Function for animating the words and making them appear one by one.
### The function takes each letter (in this case 'i'), and forces them into the terminal.

def type_it_down_uwu(the_words):
    for i in the_words:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00001)
        
header_slash_footer = "=================================================================="
empty_row = "|                                                               |"

### Function to check if the date format is correct.
### Simply put, the "date" string (in this case the data_date variable) is formatted into
### yyyy/mm/dd, so that the date is properly entered into the text.
### Additionally, try except was used to make sure that any formatting error does not crash the program.

def format_check(date, fmt):
    try: datetime.datetime.strptime(date, fmt)
    except: return False
    else: return True

### Animation Code for download.

def downloadAnimation():
    buildFooterHeader(0)
    buildRows(4,0.05)
    downanim = 0
    while downanim != 14:
        print("|                          =============                         |")
        time.sleep(0.05)
        downanim += 1
    print("|              =====================================             |")
    time.sleep(0.05)
    print("|                   ===========================                  |")
    time.sleep(0.05)
    print("|                       ==================                       |")
    time.sleep(0.05)
    print("|                          =============                         |")
    time.sleep(0.05)
    print("|                             =======                            |")
    time.sleep(0.05)
    print("|                               ===                              |")
    buildRows(3,0.05)
    buildFooterHeader(0)
    print("\n")
    print("                                                    Downloading...")
