/*  Midterm Project: Student Profile and Grades (Login)
    Dean Harold P. Abad
    October 28, ~12 PM - 29, 9:17 PM

    Pseudocode:
    1. Display main menu with sections: main_menu()
    2. Prompt what section: switch statement
    3. Display login section: username(); password()
    4. Display back or quit after logging in: if-else statement

    Goal:
    - Just make a mockup of login and make it work in sections
*/
#ifdef _WIN32
#include <windows.h>
#elif _WIN64
#include <windows.h>
#else
#include <unistd.h>
#endif
#include <iostream>
using namespace std;

// UI and logic functions
void header(), sections_and_others_list(), login(), username_input(), password_input(), student_account(), CLI_clear(), info(), quit();
int main(), os_name();

// Section functions
void bs1ma(), bs2ma(), bs3ma(), bs4ma(), bs5ma();

std::string sections_and_others_list_choice, student_username, student_password;

// Menu numbers checker
bool quitting;
int goto_menu_number, current_menu_number, previous_menu_number;

char const *usernames[16] = {
    "albao781",       // BS1MA 1
    "consejero715",   // BS1MA 2
    "tomas226",       // BS1MA 3
    "abad013",        // BS2MA 1
    "domodon365",     // BS2MA 2
    "fortes001",      // BS2MA 3
    "baclaan041",     // BS3MA 1
    "fabella076",     // BS3MA 2
    "pulmano057",     // BS3MA 3
    "castillo089",    // BS4MA 1
    "nepacena077",    // BS4MA 2
    "villafuerte101", // BS4MA 3
    "bonavente152",   // BS5MA 1
    "latoja109",      // BS5MA 2
    "pasildo136"      // BS5MA 3
};

// UI Pseudoboxdrawings
//                 "|    Asian Institute of Computer Studies (AICS) 2021     |\n";
std::string hdb =  "+========================================================+\n"; // horizontal_double_border
std::string hdbs = "+============================+===========================+\n"; // horizontal_double_border_split

/*
    *Reusable back-to-previous-session function
    *Just instance this per function, and inside this contains the logic of switching menus
    *Menu numbers:
        # - Name            - Function
        0 - Main Menu       - main()
        1 - BS1MA           - bs1ma()
        2 - BS2MA           - bs2ma()
        3 - BS3MA           - bs3ma()
        4 - BS4MA           - bs4ma()
        5 - BS5MA           - bs5ma()
        6 - Student Account - student_account()
        7 - Info            - info()
*/
void back_or_not(int goto_menu, int current_menu, int previous_menu) {
    goto_menu_number = goto_menu;
    current_menu_number = current_menu;
    previous_menu_number = previous_menu;

    std::cout << "|    Do you want to go back?                             |\n";
    std::cout << hdb;
    std::cout << "     Yes or no: ";

    std::string back;
    std::cin >> back;

    // Check the menu number
    if(back == "Yes" || back == "yes" || back == "YES" || back == "y" || back == "Y") {
        // If yes, go back to one of the following menus
        switch(goto_menu_number) {
            case 0:
                main();
                break;
            case 1:
                bs1ma();
                break;
            case 2:
                bs2ma();
                break;
            case 3:
                bs3ma();
                break;
            case 4:
                bs4ma();
                break;
            case 5:
                bs5ma();
                break;
            case 6:
                student_account();
                break;
            case 7:
                info();
                break;
        }
    }
    else if(back == "No" || back == "no" || back == "NO" || back == "n" || back == "N") {
        // If no, display the same menu again ONLY IF NOT IN SECTION
        // While in section:
        if(
            current_menu_number == 1 ||
            current_menu_number == 2 ||
            current_menu_number == 3 ||
            current_menu_number == 4 ||
            current_menu_number == 5
        ) {
            login();
        }
        // Not in section:
        else {
            switch(current_menu_number) {
                case 1:
                    bs1ma();
                    break;
                case 2:
                    bs2ma();
                    break;
                case 3:
                    bs3ma();
                    break;
                case 4:
                    bs4ma();
                    break;
                case 5:
                    bs5ma();
                    break;
                case 6:
                    student_account();
                    break;
                case 7:
                    info();
                    break;
            }
        }
    }
    else {
        std::cout << hdb;
        std::cout << "     Invalid input. Please try again.\n";
        std::cout << hdb;
        Sleep(800);
        
        // After 3 seconds of delay, switch to the current menu
        switch(current_menu_number) {
            case 0:
                main();
                break;
            case 1:
                bs1ma();
                break;
            case 2:
                bs2ma();
                break;
            case 3:
                bs3ma();
                break;
            case 4:
                bs4ma();
                break;
            case 5:
                bs5ma();
                break;
            case 6:
                student_account();
                break;
            case 7:
                info();
                break;
        }
    }
}


void header() {
    //           "+============================+===========================+\n";
    std::cout << hdb;
    std::cout << "|    Asian Institute of Computer Studies (AICS) 2021     |\n";
    std::cout << "|    Midterm Project: Student Profile and Grades         |\n";
    std::cout << "|    Version: 2.5.918                                    |\n";
    std::cout << hdb;
}


// Separated text to prevent confusion with the menu logic
void section_and_others_list_text() {
    std::cout << "|    Main Menu: Sections and Others                      |\n";
    std::cout << hdbs;
    std::cout << "|    Sections                |    Others                 |\n";
    std::cout << hdbs;
    std::cout << "|    1. BS1MA                |    i. Info                |\n";
    std::cout << "|    2. BS2MA                |    q. Quit                |\n";
    std::cout << "|    3. BS3MA                |                           |\n";
    std::cout << "|    4. BS4MA                |                           |\n";
    std::cout << "|    5. BS5MA                |                           |\n";
    std::cout << hdbs;
    std::cout << "|    What would you like to do?                          |\n";
    std::cout << hdb;
    std::cout << "     Enter the character or name of your choice: ";
}


void main_menu_goto(string choice) {
    // Use the choice to navigate through the other menus e.g. sections, others, etc.
    if(choice == "1" || choice == "BS1MA" || choice == "Bs1ma" || choice == "bs1ma") {
        bs1ma();
    }
    else if(choice == "2" || choice == "BS2MA" || choice == "Bs2ma" || choice == "bs2ma") {
        bs2ma();
    }
    else if(choice == "3" || choice == "BS3MA" || choice == "Bs3ma" || choice == "bs3ma") {
        bs3ma();
    }
    else if(choice == "4" || choice == "BS4MA" || choice == "Bs4ma" || choice == "bs4ma") {
        bs4ma();
    }
    else if(choice == "5" || choice == "BS5MA" || choice == "Bs5ma" || choice == "bs5ma") {
        bs5ma();
    }
    else if(choice == "i" || choice == "I" || choice == "Info" || choice == "info" || choice == "INFO") {
        info();
    }
    else if(choice == "q" || choice == "Q" || choice == "Quit" || choice == "quit" || choice == "QUIT") {
        quit();
    }
    else {
        std::cout << "Invalid input. Please enter one from the given options.\n";
        Sleep(800);
        main();
    }
}


void sections_and_others_list() {
    CLI_clear();
    header();
    section_and_others_list_text();

    std::string choice;
    std::cin >> choice;

    // Check if there is an input or none
    if(choice != "") {
        sections_and_others_list_choice = choice; // Only add a value to this global variable if there is an input
        main_menu_goto(sections_and_others_list_choice);
    }
    else {
        main();
    }
}


int main() {
    CLI_clear();
    
    previous_menu_number = 0;
    // Check if this function returns a value first (indicator if used already or not)
    sections_and_others_list();

    return 0;
}


void login() {
    username_input();
}


void username_input() {
    std::string username;
    std::cout << "     Enter username: ";
    std::cin >> username;

    student_username = username;

    if(
        student_username == usernames[0] ||
        student_username == usernames[1] ||
        student_username == usernames[2] ||
        student_username == usernames[3] ||
        student_username == usernames[4] ||
        student_username == usernames[5] ||
        student_username == usernames[6] ||
        student_username == usernames[7] ||
        student_username == usernames[8] ||
        student_username == usernames[9] ||
        student_username == usernames[10] ||
        student_username == usernames[11] ||
        student_username == usernames[12] ||
        student_username == usernames[13] ||
        student_username == usernames[14]
    ) {
        student_username = username;
        password_input();
    }
    else {
        std::cout << "     Invalid username. Please enter again.\n";
        Sleep(800);
        login();
    }
}


void password_input() {
    std::string password;
    std::cout << "     Enter password: ";
    std::cin >> password;

    student_password = password;

    student_account();
}


void bs1ma() {
    CLI_clear();
    header();

    // Not the 'main', but 'itself'
    previous_menu_number = 1;

    std::cout << "|    BS1MA Section: Students                             |\n";
    std::cout << hdbs;
    std::cout << "|    Names                   |    IDs                    |\n";
    std::cout << hdbs;
    std::cout << "|    Albao, Melvin James     |    170781                 |\n";
    std::cout << "|    Consejero, Viviane      |    180715                 |\n";
    std::cout << "|    Tomas, Aljean Santos    |    141226                 |\n";
    std::cout << hdbs;

    back_or_not(0, 1, 0);
}


void bs2ma() {
    CLI_clear();
    header();

    previous_menu_number = 2;

    std::cout << "|    BS2MA Section: Students                             |\n";
    std::cout << hdbs;
    std::cout << "|    Names                   |    IDs                    |\n";
    std::cout << hdbs;
    std::cout << "|    Abad, Dean Harold       |    210013                 |\n";
    std::cout << "|    Domodon, Althea         |    190365                 |\n";
    std::cout << "|    Fortes, Jhon Emerson    |    210001                 |\n";
    std::cout << hdbs;

    back_or_not(0, 2, 0);
}


void bs3ma() {
    CLI_clear();
    header();

    previous_menu_number = 3;

    std::cout << "|    BS3MA Section: Students                             |\n";
    std::cout << hdbs;
    std::cout << "|    Names                   |    IDs                    |\n";
    std::cout << hdbs;
    std::cout << "|    Baclaan, Rocel          |    210041                 |\n";
    std::cout << "|    Fabella, Joshua         |    210076                 |\n";
    std::cout << "|    Pulmano, Johnmark       |    210057                 |\n";
    std::cout << hdbs;

    back_or_not(0, 3, 0);
}


void bs4ma() {
    CLI_clear();
    header();

    previous_menu_number = 4;

    std::cout << "|    BS1MA Section: Students                             |\n";
    std::cout << hdbs;
    std::cout << "|    Names                   |    IDs                    |\n";
    std::cout << hdbs;
    std::cout << "|    Castillo, Dawn Xyly     |    210089                 |\n";
    std::cout << "|    Nepacena, John Jomar    |    210077                 |\n";
    std::cout << "|    Villafuerte, Sean       |    210101                 |\n";
    std::cout << hdbs;

    back_or_not(0, 4, 0);
}


void bs5ma() {
    CLI_clear();
    header();

    previous_menu_number = 5;

    std::cout << "|    BS1MA Section: Students                             |\n";
    std::cout << hdbs;
    std::cout << "|    Names                   |    IDs                    |\n";
    std::cout << hdbs;
    std::cout << "|    Bonavente, Timothy      |    210152                 |\n";
    std::cout << "|    Latoja, Jiggs Venick    |    210109                 |\n";
    std::cout << "|    Pasildo, Edmund Paul    |    210136                 |\n";
    std::cout << hdbs;

    back_or_not(0, 5, 0);
}


void student_account() {
    CLI_clear();
    header();

    int student_grade;
    std::string student_completion;
    // Check the grades
    if(
        student_username != usernames[9] ||
        student_username != usernames[10] ||
        student_username != usernames[11] ||
        student_username != usernames[12] ||
        student_username != usernames[14]
    ) {
        student_grade = 97;
    }
    else {
        student_grade = 98;
    }

    if(student_grade <= 74) {
        student_completion = "Failed";
    }
    else {
        student_completion = "Passed";
    }

    std::cout << "|    Student Dashboard                                   |\n";
    std::cout << hdb;
    std::cout << "     Username: " << student_username << "\n";
    std::cout << "     Password: " << student_password << "\n";
    std::cout << "     Grade: " << student_grade << "\n";
    std::cout << "     Completion: " << student_completion << "\n";
    std::cout << hdb;

    back_or_not(previous_menu_number, 6, previous_menu_number);
}


// Check what kind of os the program runs in
// For clearing the screen in console:
int os_name() {
    int system_name;

    #ifdef _WIN32
    return 1;
    #elif _WIN64
    return 2;
    #elif __APPLE__
    return 3;
    #elif __linux__
    return 4;
    #else
    return 0;
    #endif

    return 0;
}


void CLI_clear() {
    switch(os_name()) {
        case 1:
            system("cls");
            break;
        case 2:
            system("cls");
            break;
        case 3:
            system("clear");
            break;
        case 4:
            system("clear");
            break;
        case 0:
            std::cout << "\nOS unidentified; cannot clear screen.\n";
            break;
        default:
            std::cout << "\nOS unidentified; cannot clear screen.\n";
            break;
    }
}


// Info section
void info() {
    CLI_clear();
    header();

    previous_menu_number = 7;

    std::cout << "|    Info: Student Account                               |\n";
    std::cout << hdb;
    std::cout << "|    The student account is provided by the school,      |\n";
    std::cout << "|    and it is fixed. Please make ensure your account's  |\n";
    std::cout << "|    safety.                                             |\n";
    std::cout << "|    You may contact the school for more information:    |\n";
    std::cout << "|    0999-999-9999 or help@aics.edu.ph                   |\n";
    std::cout << hdb;
    std::cout << "|    Student account guide:                              |\n";
    std::cout << "|    The username consists of the surname, which its     |\n";
    std::cout << "|    letters are all in lowercase, and added with the    |\n";
    std::cout << "|    last 3 digits of the student's ID number.           |\n";
    std::cout << "|    Example:                                            |\n";
    std::cout << "|    The name of a student is 'Abad, Dean Harold', and   |\n";
    std::cout << "|    his ID number is '210013', therefore his username   |\n";
    std::cout << "|    is 'abad013'                                        |\n";
    std::cout << hdb;

    back_or_not(0, 7, 0);
}


// Function that terminates the program
void quit() {
    quitting = true;
    std::cout << "     Quiting.\n";
    Sleep(800);
    std::cout << "     Quiting..\n";
    Sleep(800);
    std::cout << "     Quiting...\n";
    Sleep(800);
    std::cout << "     Quiting.\n";
    Sleep(800);
    std::cout << "     Quiting..\n";
    Sleep(800);
    std::cout << "     Quiting...\n";
    Sleep(800);
    system("exit");
}