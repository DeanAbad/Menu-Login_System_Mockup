# Midterm Project: Student Menu and Grades
# Dean Harold P. Abad, O-BS1MA, ODL
# October 27 - October 30, 4:12 PM

import os   # To be able to manipulate the Command Line Interface (CLI)
import time # Time module for timer method

# Pseudocode:
# 1. Display main menu with sections: main_menu()
# 2. Prompt what section: match-case statement
# 3. Display list of students and ID numbers: catalog()
# 4. Enter student name: input("Enter student name or ID: ")
# 5. Display student name, ID, and grades in 1st semester: student_profile()
#    5.1. Display attendance week 1-5 only
#    5.2. Display if passed or failed
# 6. Prompt if user is going back or not to main menu: if-else
#    6.1. If no, remain in the same section: return void
#    6.2. If yes, go back to main menu: main_menu()

# Note:
# 1. 3 students only per section
# 2. Add pictures via module if possible
# 3. To self: You really need to come up with proper names for border presets
# 4. Forgot that the dictionary below is kind of CSV, and applied it the same to the array of usernames ugh
# 5. Array = []; Dictionary/CSV/JSON = {}

# Make a dictionary of ASCII characters and their unicode for reference; for User Interface in CLI and IDLE
# The 'bd' stands for 'box_drawings'; refer to https://www.unicode.org/charts/PDF/U2500.pdf
# Shortcut example: DDR = Double Down and Right of Box Drawings (bd) 
bd = {
    # Shortcut: Unicode | Name                                              | Symbol 
    "DDR": u'\u2554',   # BOX DRAWINGS DOUBLE DOWN AND RIGHT                  ╔
    "DV": u'\u2551',    # BOX DRAWINGS DOUBLE VERTICAL                        ║
    "DUR": u'\u255a',   # BOX DRAWINGS DOUBLE UP AND RIGHT                    ╚
    "DDL": u'\u2557',   # BOX DRAWINGS DOUBLE DOWN AND LEFT                   ╗
    "DUL": u'\u255d',   # BOX DRAWINGS DOUBLE UP AND LEFT                     ╝
    "DH": u'\u2550',    # BOX DRAWINGS DOUBLE HORIZONTAL                      ═
    "DVR": u'\u2560',   # BOX DRAWINGS DOUBLE VERTICAL AND RIGHT              ╠
    "DVL": u'\u2563',   # BOX DRAWINGS DOUBLE VERTICAL AND LEFT               ╣
    "DDH": u'\u2566',   # BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL             ╦
    "DUH": u'\u2569',   # BOX DRAWINGS DOUBLE UP AND HORIZONTAL               ╩
    "VDRS": u'\u255F',  # BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE       ╟
    "VDLS": u'\u2562',  # BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE        ╢
    "DSHD": u'\u2564',  # BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE      ╤
    "USHD": u'\u2567',  # BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE        ╧
    "LV": u'\u2502',    # BOX DRAWINGS LIGHT VERTICAL                         │
    "LH": u'\u2500',    # BOX DRAWINGS LIGHT HORIZONTAL                       ─
    "LDH": u'\u252c',   # BOX DRAWINGS LIGHT DOWN AND HORIZONTAL              ┬
    "LUH": u'\u2534',   # BOX DRAWINGS LIGHT UP AND HORIZONTAL                ┴
    "LVH": u'\u253c',   # BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL          ┼
    "VSHD": u'\u256a'   # BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE  ╪
}

# Each one contains 62 characters (excluding the first two)
# Variable                        | Output
odl = bd["LH"] * 60               # ─────
hdl = bd["DH"] * 60               # ═════
tdl = bd["DDR"] + hdl + bd["DDL"] # ╔═══╗
mdl = bd["DVR"] + hdl + bd["DVL"] # ╠═══╣
bdl = bd["DUR"] + hdl + bd["DUL"] # ╚═══╝
mcsdl = bd["DVR"] + (bd["DH"] * 30) + bd["USHD"] + (bd["DH"] * 29) + bd["DVL"]
mcddl = bd["VDRS"] + odl + bd["VDLS"]

# 'cmsl' = 'center single line'
tsl = bd["VDRS"] + (bd["LH"] * 30) + bd["LDH"] + (bd["LH"] * 29) + bd["VDLS"]
bsl = bd["VDRS"] + (bd["LH"] * 30) + bd["LUH"] + (bd["LH"] * 29) + bd["VDLS"]
csl = bd["VDRS"] + (bd["LH"] * 30) + bd["LVH"] + (bd["LH"] * 29) + bd["VDLS"]

# Top single border
wtsl = bd["VDRS"] + odl + bd["VDLS"]

# Bottom double border with single center split
bsdl = bd["DUR"] + (bd["DH"] * 30) + bd["USHD"] + (bd["DH"] * 29) + bd["DUL"]

# Bottom double border
wbsdl = bd["DUR"] + (bd["DH"] * 60) + bd["DUL"]

# Middle double border with single center split
msdl = bd["DVR"] + (bd["DH"] * 30) + bd["VSHD"] + (bd["DH"] * 29) + bd["DVL"]

# Students' usernames
# Use as reference when displaying info at student_account()
un = [
    # Username        | Name                  | ID
    "albao781",       # Albao, Melvin James     170781
    "consejero715",   # Consejero, Viviane      180715
    "tomas226",       # Tomas, Aljean Santos    141226
    "abad013",        # Abad, Dean Harold       210013
    "domodon365",     # Domodon, Althea         190365
    "fortes001",      # Fortes, John Emerson    210001
    "baclaan041",     # Baclaan, Rocel          210041
    "fabella076",     # Fabella, Joshua         210076
    "pulmano057",     # Pulmano, Johnmark       210057
    "castillo089",    # Castillo, Dawn Xyly     210089
    "nepacena077",    # Nepacena, John Jomar    210077
    "villafuerte101", # Villafuerte, Sean       210101
    "bonavente152",   # Bonavente, Timothy      210152
    "latoja109",      # Latoja, Jiggs Venick    210109
    "pasildo136"      # Pasildo, Edmund Paul    210136
]
student_name_or_id = ""
student_password = ""
# Menu navigation
goto_menu_number = 0
current_menu_number = 0
previous_menu_number = 0
# Current section number
current_section_number = 0


# The clear screen only works in terminal/console, not in Python's IDLE
def CLI_clear():
    # Windows
    if os.name == 'nt':
        return os.system('cls')
    # Mac and Linux (os.name = 'posix')
    else:
        return os.system('clear')


# The constant header to be reused for other functions
def header():
    print(tdl)
    print(bd["DV"] +   "      Asian Institute of Computer Studies (AICS) 2021       " + bd["DV"])
    print(bd["DV"] +   "      Midterm Project: Student Menu and Grades              " + bd["DV"])
    print(bd["DV"] +   "      Version: 1.6.412                                      " + bd["DV"])
    print(mdl)


# Back function: same as the application in CPP
# Would take 3 arguments i.e. menu to go into, current menu on-screen, and previously visited menu
# Name              Number   Function
# Main Menu         0        main_menu()
# BS1MA             1        bs1ma()
# BS2MA             2        bs2ma()
# BS3MA             3        bs3ma()
# BS4MA             4        bs4ma()
# BS5MA             5        bs5ma()
# Student Account   6        student_account()
# Info              7        info()
def back_or_not(goto_menu, current_menu, previous_menu):
    
    global goto_menu_number
    global current_menu_number
    global previous_menu_number
    global current_section_number
    goto_menu_number = goto_menu
    current_menu_number = current_menu
    previous_menu_number = previous_menu

    print(bd["DV"] + "      Do you want to go back?                               " + bd["DV"])
    print(wbsdl)
    back_to_old = str(input("       Yes or no: "))

    if back_to_old != "":
        if back_to_old == "YES" or back_to_old == "Yes" or back_to_old == "yes" or back_to_old == "y" or back_to_old == "Y":
            match previous_menu_number:
                case 0:
                    main_menu()
                case 1:
                    bs1ma_menu()
                case 2:
                    bs2ma_menu()
                case 3:
                    bs3ma_menu()
                case 4:
                    bs4ma_menu()
                case 5:
                    bs5ma_menu()
                case 6:
                    student_account()
                case 7:
                    info_menu()
        elif back_to_old == "NO" or back_to_old == "No" or back_to_old == "no" or back_to_old == "n" or back_to_old == "N":
            match current_menu_number:
                case 1:
                    current_section_number = 1
                    login()
                case 2:
                    current_section_number = 2
                    login()
                case 3:
                    current_section_number = 3
                    login()
                case 4:
                    current_section_number = 4
                    login()
                case 5:
                    current_section_number = 5
                    login()
                case 6:
                    student_account()
                case 7:
                    info_menu()
        else:
            print("       Invalid input. Please try again.\n")
            print(tdl)
            back_or_not(goto_menu_number, current_menu_number, previous_menu_number)
    else:
        print("       Invalid input. Please try again.\n")
        print(tdl)
        back_or_not(goto_menu_number, current_menu_number, previous_menu_number)


def sections_and_others_text():
    print(bd["DV"] + "      Main Menu                                             " + bd["DV"])
    print(tsl)
    print(bd["DV"] + "      Sections                " + bd["LV"] + "       Others                " + bd["DV"])
    print(csl)
    print(bd["DV"] + "      1. BS1MA                " + bd["LV"] + "       i. Info               " + bd["DV"])
    print(bd["DV"] + "      2. BS2MA                " + bd["LV"] + "       q. Quit               " + bd["DV"])
    print(bd["DV"] + "      3. BS3MA                " + bd["LV"] + "                             " + bd["DV"])
    print(bd["DV"] + "      4. BS4MA                " + bd["LV"] + "                             " + bd["DV"])
    print(bd["DV"] + "      5. BS5MA                " + bd["LV"] + "                             " + bd["DV"])
    print(bsdl)


def sections_and_others():
    header()
    sections_and_others_text()

    choice = str(input("       Enter your character or name of option: "))
    
    match choice:
        # Sections: BS1MA-BS5MA
        case '1':
            bs1ma_menu()
        case 'BS1MA':
            bs1ma_menu()
        case 'Bs1ma':
            bs1ma_menu()
        case 'bs1ma':
            bs1ma_menu()
            
        case '2':
            bs2ma_menu()
        case 'BS2MA':
            bs2ma_menu()
        case 'Bs2ma':
            bs2ma_menu()
        case 'bs2ma':
            bs2ma_menu()
            
        case '3':
            bs3ma_menu()
        case 'BS3MA':
            bs3ma_menu()
        case 'Bs3ma':
            bs3ma_menu()
        case 'bs3ma':
            bs3ma_menu()
            
        case '4':
            bs4ma_menu()
        case 'BS4MA':
            bs4ma_menu()
        case 'Bs4ma':
            bs4ma_menu()
        case 'bs4ma':
            bs4ma_menu()
            
        case '5':
            bs5ma_menu()
        case 'BS5MA':
            bs5ma_menu()
        case 'Bs5ma':
            bs5ma_menu()
        case 'bs5ma':
            bs5ma_menu()
            
        # Others: Info and Quit
        case 'i':
            info_menu()
        case 'I':
            info_menu()
        case 'INFO':
            info_menu()
        case 'Info':
            info_menu()
        case 'info':
            info_menu()
            
        case 'q':
            quit_menu()
        case 'Q':
            quit_menu()
        case 'QUIT':
            quit_menu()
        case 'Quit':
            quit_menu()
        case 'quit':
            quit_menu()
            
        # Go back to main menu again after displaying the message of error
        case _:
            print("       Invalid input. Please try again.\n")
            time.sleep(1)
            main_menu()


# The main menu contains the list of sections to choose from
def main_menu():
    CLI_clear() # Clear the screen first (CLI only, not IDLE)
    sections_and_others()


# Login function - sets the current nth of section for later use
# Section   Number
# BS1MA     1
# BS2MA     2
# BS3MA     3
# BS4MA     4
# BS5MA     5
def login():
    name_or_id_input()


def password_input():
    global student_password
    password = str(input("       Enter password: "))

    if password != "":
        student_password = password
        student_account()
    else:
        print("       Invalid input. Please try again.\n")
        time.sleep(1)
        password()


def name_or_id_input():
    global student_name_or_id
    name_or_id = str(input("       Enter name_or_id: "))

    # Check first if there is an input
    if name_or_id != "":
        # Check if in the appropriate section menu
        match current_section_number:
            case 1:
                # Check the student name or id if matches from the given
                match name_or_id:
                    # BS1MA Student 1
                    case 'Albao, Melvin James':
                        student_name_or_id = un[0]
                        password_input()
                    case 'Melvin James Albao':
                        student_name_or_id = un[0]
                        password_input()
                    case '170781':
                        student_name_or_id = un[0]
                        password_input()
                        
                    # BS1MA Student 2
                    case 'Consejero, Viviane':
                        student_name_or_id = un[1]
                        password_input()
                    case 'Viviane Consejero':
                        student_name_or_id = un[1]
                        password_input()
                    case '180715':
                        student_name_or_id = un[1]
                        password_input()
                        
                    # BS1MA Student 3
                    case 'Tomas, Aljean Santos':
                        student_name_or_id = un[2]
                        password_input()
                    case 'Aljean Santos Tomas':
                        student_name_or_id = un[2]
                        password_input()
                    case '141226':
                        student_name_or_id = un[2]
                        password_input()

                    # None of the following
                    case _:
                        print("       Invalid input. Please try again.\n")
                        time.sleep(1)
                        login(current_section_number)
            case 2:
                match name_or_id:
                    case 'Abad, Dean Harold':
                        student_name_or_id = un[3]
                        password_input()
                    case 'Dean Harold Abad':
                        student_name_or_id = un[3]
                        password_input()
                    case '210013':
                        student_name_or_id = un[3]
                        password_input()

                    case 'Domodon, Althea':
                        student_name_or_id = un[4]
                        password_input()
                    case 'Althea Domodon':
                        student_name_or_id = un[4]
                        password_input()
                    case '190365':
                        student_name_or_id = un[4]
                        password_input()

                    case 'Fortes, John Emerson':
                        student_name_or_id = un[5]
                        password_input()
                    case 'John Emerson Fortes':
                        student_name_or_id = un[5]
                        password_input()
                    case '210001':
                        student_name_or_id = un[5]
                        password_input()

                    case _:
                        print("       Invalid input. Please try again.\n")
                        time.sleep(1)
                        login(current_section_number)
            case 3:
                match name_or_id:
                    case 'Baclaan, Rocel':
                        student_name_or_id = un[6]
                        password_input()
                    case 'Rocel Baclaan':
                        student_name_or_id = un[6]
                        password_input()
                    case '210041':
                        student_name_or_id = un[6]
                        password_input()

                    case 'Fabella, Joshua':
                        student_name_or_id = un[7]
                        password_input()
                    case 'Joshua Fabella':
                        student_name_or_id = un[7]
                        password_input()
                    case '210076':
                        student_name_or_id = un[7]
                        password_input()

                    case 'Pulmano, Johnmark':
                        student_name_or_id = un[8]
                        password_input()
                    case 'Johnmark Pulmano':
                        student_name_or_id = un[8]
                        password_input()
                    case '210057':
                        student_name_or_id = un[8]
                        password_input()

                    case _:
                        print("       Invalid input. Please try again.\n")
                        time.sleep(1)
                        login(current_section_number)
            case 4:
                match name_or_id:
                    case 'Castillo, Dawn Xyly':
                        student_name_or_id = un[9]
                        password_input()
                    case 'Dawn Xyly Castillo':
                        student_name_or_id = un[9]
                        password_input()
                    case '210089':
                        student_name_or_id = un[9]
                        password_input()

                    case 'Nepacena, John Jomar':
                        student_name_or_id = un[10]
                        password_input()
                    case 'John Jomar Nepacena':
                        student_name_or_id = un[10]
                        password_input()
                    case '210077':
                        student_name_or_id = un[10]
                        password_input()

                    case 'Villafuerte, Sean':
                        student_name_or_id = un[11]
                        password_input()
                    case 'Sean Villafuerte':
                        student_name_or_id = un[11]
                        password_input()
                    case '210101':
                        student_name_or_id = un[11]
                        password_input()

                    case _:
                        print("       Invalid input. Please try again.\n")
                        time.sleep(1)
                        login(current_section_number)
            case 5:
                match name_or_id:
                    case 'Bonavente, Timothy':
                        student_name_or_id = un[12]
                        password_input()
                    case 'Timothy Bonavente':
                        student_name_or_id = un[12]
                        password_input()
                    case '210152':
                        student_name_or_id = un[12]
                        password_input()

                    case 'Latoja, Jiggs Venick':
                        student_name_or_id = un[13]
                        password_input()
                    case 'Jiggs Venick Latoja':
                        student_name_or_id = un[13]
                        password_input()
                    case '210109':
                        student_name_or_id = un[13]
                        password_input()

                    case 'Pasildo, Edmund Paul':
                        student_name_or_id = un[14]
                        password_input()
                    case 'Edmund Paul Pasildo':
                        student_name_or_id = un[14]
                        password_input()
                    case '210136':
                        student_name_or_id = un[14]
                        password_input()

                    case _:
                        print("       Invalid input. Please try again.\n")
                        time.sleep(1)
                        login(current_section_number)
            case _:
                print("       Invalid section. Try to input in another section or try other name.\n")
                time.sleep(1)
                login(current_section_number)
    else:
        print("       Invalid input. Please try again.\n")
        time.sleep(1)
        login(current_section_number)


def bs1ma_menu():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    current_menu_number = 1
    previous_menu_number = 0
    
    print(bd["DV"] + "      BS1MA Students                                        " + bd["DV"])
    print(tsl)
    print(bd["DV"] + "      Student Name            " + bd["LV"] + "       Student Number        " + bd["DV"])
    print(csl)
    print(bd["DV"] + "      Albao, Melvin James     " + bd["LV"] + "       170781                " + bd["DV"])
    print(bd["DV"] + "      Consejero, Viviane      " + bd["LV"] + "       180715                " + bd["DV"])
    print(bd["DV"] + "      Tomas, Aljean Santos    " + bd["LV"] + "       141226                " + bd["DV"])
    print(mcsdl)

    back_or_not(goto_menu_number, current_menu_number, previous_menu_number)


def bs2ma_menu():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    current_menu_number = 2
    previous_menu_number = 0
    
    print(bd["DV"] + "      BS2MA Students                                        " + bd["DV"])
    print(tsl)
    print(bd["DV"] + "      Student Name            " + bd["LV"] + "       Student Number        " + bd["DV"])
    print(csl)
    print(bd["DV"] + "      Abad, Dean Harold       " + bd["LV"] + "       210013                " + bd["DV"])
    print(bd["DV"] + "      Domodon, Althea         " + bd["LV"] + "       190365                " + bd["DV"])
    print(bd["DV"] + "      Fortes, Jhon Emerson    " + bd["LV"] + "       210001                " + bd["DV"])
    print(mcsdl)

    back_or_not(goto_menu_number, current_menu_number, previous_menu_number)


def bs3ma_menu():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    current_menu_number = 3
    previous_menu_number = 0
    
    print(bd["DV"] + "      BS3MA Students                                        " + bd["DV"])
    print(tsl)
    print(bd["DV"] + "      Student Name            " + bd["LV"] + "       Student Number        " + bd["DV"])
    print(csl)
    print(bd["DV"] + "      Baclaan, Rocel          " + bd["LV"] + "       210041                " + bd["DV"])
    print(bd["DV"] + "      Fabella, Joshua         " + bd["LV"] + "       210076                " + bd["DV"])
    print(bd["DV"] + "      Pulmano, Johnmark       " + bd["LV"] + "       210057                " + bd["DV"])
    print(mcsdl)

    back_or_not(goto_menu_number, current_menu_number, previous_menu_number)


def bs4ma_menu():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    current_menu_number = 4
    previous_menu_number = 0
    
    print(bd["DV"] + "      BS4MA Students                                        " + bd["DV"])
    print(tsl)
    print(bd["DV"] + "      Student Name            " + bd["LV"] + "       Student Number        " + bd["DV"])
    print(csl)
    print(bd["DV"] + "      Castillo, Dawn Xyly     " + bd["LV"] + "       210089                " + bd["DV"])
    print(bd["DV"] + "      Nepacena, John Jomar    " + bd["LV"] + "       210077                " + bd["DV"])
    print(bd["DV"] + "      Villafuerte, Sean       " + bd["LV"] + "       210101                " + bd["DV"])
    print(mcsdl)

    back_or_not(goto_menu_number, current_menu_number, previous_menu_number)


def bs5ma_menu():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    current_menu_number = 5
    previous_menu_number = 0
    
    print(bd["DV"] + "      BS5MA Students                                        " + bd["DV"])
    print(tsl)
    print(bd["DV"] + "      Student Name            " + bd["LV"] + "       Student Number        " + bd["DV"])
    print(csl)
    print(bd["DV"] + "      Bonavente, Timothy      " + bd["LV"] + "       210152                " + bd["DV"])
    print(bd["DV"] + "      Latoja, Jiggs Venick    " + bd["LV"] + "       210109                " + bd["DV"])
    print(bd["DV"] + "      Pasildo, Edmund Paul    " + bd["LV"] + "       210136                " + bd["DV"])
    print(mcsdl)

    back_or_not(goto_menu_number, current_menu_number, previous_menu_number)


def student_account():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    global current_section_number
    global student_name_or_id
    global student_password
    current_menu_number = 6
    previous_menu_number = current_section_number
    student_name = ""
    student_id = 0
    student_grade = 0
    student_completion = ""
    
    match student_name_or_id:
        case 'albao781':
            student_name = "Melvin James Albao"
            student_id = 170781

        case 'consejero715':
            student_name = "Viviane Consejero"
            student_id = 180715

        case 'tomas226':
            student_name = "Aljean Santos Tomas"
            student_id = 141226


        case 'abad013':
            student_name = "Dean Harold Abad"
            student_id = 210013

        case 'domodon365':
            student_name = "Althea Domodon"
            student_id = 190365

        case 'fortes001':
            student_name = "John Emerson Fortes"
            student_id = 210001


        case 'baclaan041':
            student_name = "Rocel Baclaan"
            student_id = 210041

        case 'fabella076':
            student_name = "Joshua Fabella"
            student_id = 210076

        case 'pulmano057':
            student_name = "Johnmark Pulmano"
            student_id = 210057


        case 'castillo089':
            student_name = "Dawn Xyly Castillo"
            student_id = 210089

        case 'nepacena077':
            student_name = "John Jomar Nepacena"
            student_id = 210077

        case 'villafuerte101':
            student_name = "Sean Villafuerte"
            student_id = 210101


        case 'bonavente152':
            student_name = "Timothy Bonavente"
            student_id = 210152

        case 'latoja109':
            student_name = "Jiggs Venick Latoja"
            student_id = 210109

        case 'pasildo136':
            student_name = "Edmund Paul Pasildo"
            student_id = 210136

    if student_name_or_id != un[9] or student_name_or_id != un[10] or student_name_or_id != un[11] or student_name_or_id != un[12] or student_name_or_id != un[14]:
        student_grade = 97
    else:
        student_grade = 98

    if student_grade <= 74:
        student_completion = "Failed"
    else:
        student_completion = "Passed"

    print(bd["DV"] + "      Student Dashbooard                                    " + bd["DV"])
    print(bdl)
    print("       Name: " + student_name)
    print("       ID: " + str(student_id))
    print("       Password: " + student_password)
    print("       Grade: " + str(student_grade))
    print("       Completion: " + student_completion)

    print(tdl)
    back_or_not(current_menu_number, current_menu_number, previous_menu_number)


def info_menu():
    CLI_clear()
    header()

    global current_menu_number
    global previous_menu_number
    current_menu_number = 7
    previous_menu_number = 0

    print(bd["DV"] + "      Info: Student Account                                 " + bd["DV"])
    print(mcddl)
    print(bd["DV"] + "      The student account is provided by the school,        " + bd["DV"])
    print(bd["DV"] + "      and it is fixed. Please ensure your account's         " + bd["DV"])
    print(bd["DV"] + "      safety.                                               " + bd["DV"])
    print(bd["DV"] + "      You may contact the school for more information:      " + bd["DV"])
    print(bd["DV"] + "      0999-999-9999 or help@aics.edu.ph                     " + bd["DV"])
    print(mcddl)
    print(bd["DV"] + "      Student account guide:                                " + bd["DV"])
    print(bd["DV"] + "      The username consists of the surname, which its       " + bd["DV"])
    print(bd["DV"] + "      letters are all in lowercase, and added with the      " + bd["DV"])
    print(bd["DV"] + "      last 3 digits of the student's ID number.             " + bd["DV"])
    print(bd["DV"] + "      Example:                                              " + bd["DV"])
    print(bd["DV"] + "      The name of a student is 'Abad, Dean Harold', and     " + bd["DV"])
    print(bd["DV"] + "      his ID number is '210013', therefore his username     " + bd["DV"])
    print(bd["DV"] + "      is 'abad013'.                                         " + bd["DV"])
    print(mcddl)
    print(bd["DV"] + "      Currently, username is depreciated and logging in     " + bd["DV"])
    print(bd["DV"] + "      only involves entering the either the full name or    " + bd["DV"])
    print(bd["DV"] + "      student ID, and then the password.                    " + bd["DV"])
    print(bdl)

    print(tdl)
    back_or_not(current_menu_number, current_menu_number, previous_menu_number)


def quit_menu():
    header()

    # Just a little addition ughhh
    print(bd["DV"] + "      Midterm Project: Student Menu and Grades              " + bd["DV"])
    print(bd["DV"] + "      Quitting.                                             " + bd["DV"])
    time.sleep(0.25)
    print(bd["DV"] + "      Quitting..                                            " + bd["DV"])
    time.sleep(0.25)
    print(bd["DV"] + "      Quitting...                                           " + bd["DV"])
    time.sleep(0.25)
    print(bd["DV"] + "      Quitting.                                             " + bd["DV"])
    time.sleep(0.25)
    print(bd["DV"] + "      Quitting..                                            " + bd["DV"])
    time.sleep(0.25)
    print(bd["DV"] + "      Quitting...                                           " + bd["DV"])
    time.sleep(0.25)
    print(bd["DV"] + "      Successfully quitted!                                 " + bd["DV"])
    print(wbsdl)

    # Finally, exit the session with exit CLI command
    return os.system('exit')


# Functions should be here to save global values
main_menu() # Proceed to the main menu


