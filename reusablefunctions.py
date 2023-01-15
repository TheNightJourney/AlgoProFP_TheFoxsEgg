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
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    
### Function for animating the words and making them appear one by one.

def type_it_down_uwu(the_words):
    for i in the_words:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00001)
        
header_slash_footer = "=================================================================="
empty_row = "|                                                               |"

### Function to check if the date format is correct.

def format_check(date, fmt):
    try: datetime.datetime.strptime(date, fmt)
    except: return False
    else: return True
