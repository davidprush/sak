#!/usr/bin/env python3
"""
sak.py
Author: David Rush
License: MIT
Copyright 2022 DAVID RUSH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

The sak is the Swiss Army Knife of Python3 solutions I have developed while
learning Python3. This program is "just for fun" and is only inteded as a
learning tool or proof of work concept. Thank you! And have fun with the sak!
"""
import sys
import os
import platform
import turtle
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

menu_dict = {'--quit': '\t\t\t\tQuit sak',
             '--sys-info': '\t\t\tDisplay system information',
             '--help': '\t\t\t\tDisplay help for sak commands',
             '--bin-convert': '\t\t\tConvert data to binary',
             '--hex-convert': '\t\t\tConvert data to hexadecimal',
             '--test': '\t\t\t\tRun system test',
             '--new-file': '\t\t\tCreate new file',
             '--create-directory': '\t\tCreate new folder (directory)',
             '--advanced-options': '\t\tDisplay advanced options',
             '--draw-polygon': '\t\t\tUse a class to create and draw polygons',
             '--date': '\t\t\t\tDisplay system date',
             '--cal': '\t\t\t\tDisplay system calendar'}


class Polygon:
    def __init__(self, name, sides=4, size=100):
        self.name = name
        self.sides = sides
        self.size = size
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides

    def draw(self):
        for side in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        turtle.done()


def draw_polygon():
    poly_sides = int(input("Enter # of sides for your polygon: "))
    poly_size = int(input("Enter size of your polygon: "))
    my_polygon = Polygon("MyPoly", poly_sides, poly_size)
    my_polygon.draw()
    turtle.clear()


# Defining main function
def main():
    check_os()
    greeting()
    check_args()
    sak_menu()


# greeting() greets the user upon starting the program
# no pre- or post- conditions
def greeting():
    # sets the text colour to green
    os.system("tput setaf 4")
    print("*" * 80)
    print("\tWelcome to")
    print("\t ssssssssss     aaaaaa     kkk    kkk !!!!!!!!!!!!!!")
    print("\tssssssssss   aaaa    aaaa  kkk   kkk  !!!        !!!")
    print("\tsss         aaa        aaa kkk  kkk    !!!      !!!")
    print("\tssss        aaa   oo   aaa kkk kkk      !!!    !!!")
    print("\t   sssss    aaa  oooo  aaa kkkkkk        !!!  !!!")
    print("\t       ssss aaa   oo   aaa kkk kkk        !!!!!!")
    print("\t        sss aaa        aaa kkk  kkk             ")
    print("\t ssssssssss aaa        aaa kkk   kkk      !!!!!!")
    print("\tssssssssss  aaa        aaa kkk    kkk     !!!!!!")
    print("\tsak is the swiss army knife of Python3 programs.")
    print("\tuse sak to do many things!")
    print("*" * 80)


def quit_sak():
    # sets the text color to white
    os.system("tput setaf 7")
    user_choice = input("Are you sure you want to quit (Y/N):")
    if (user_choice == "Y" or user_choice == "y" or user_choice == "Yes"):
        print("Quiting sak!")
        exit()
    else:
        sak_menu()


def user_command(do_this):
    if (do_this == "date" or do_this == "--date"):
        os.system("date")

    elif (do_this == "cal" or do_this == "--cal"):
        os.system("cal")

    elif (do_this == "quit" or do_this == "--quit"):
        quit_sak()
        # os.system("systemctl start httpd")
        # os.system("systemctl status httpd")

    elif (do_this == "sys-info" or do_this == "--sys-info"):
        sys_info()

    elif (do_this == "help" or do_this == "--help"):
        detailed_help()

    elif (do_this == "bin-convert" or do_this == "--bin-convert"):
        print(binary_convert())

    elif (do_this == "hex-convert" or do_this == "--hex-convert"):
        print(hex_convert())

    elif (do_this == "test" or do_this == "--test"):
        user_test = input("This is experimental, type whatever you want: ")
        do_whatever_user_types(user_test)

    elif (do_this == "new-file" or do_this == "--new-file"):
        filename = input("Enter the filename: ")
        f = os.system("sudo touch {}".format(filename))
        if f != 0:
            print("Some error occurred")
        else:
            print("File created successfully")

    elif (do_this == "create-directory" or do_this == "--create-directory"):
        foldername = input("Enter the foldername: ")
        f = os.system("sudo mkdir {}".format(foldername))
        if f != 0:
            print("Some error occurred")
        else:
            print("Folder created successfully")

    elif (do_this == "advanced-options" or do_this == "--advanced-options"):
        display_advanced_options()

    elif (do_this == "draw-polygon" or do_this == "--draw-polygon"):
        draw_polygon()

    elif do_this == 9:
        print("Exiting application")
        exit()
    else:
        print("Oops, that was not a valid command, please try again...")
    print()
    input("Press enter to continue")


def sak_menu():
    # sets the text color to red
    os.system("tput setaf 1")
    print("\tWELCOME TO sak's Main Menu\t\t\t")
    # sets the text color to white
    os.system("tput setaf 7")
    print("-" * 80)
    print("\tCommands can be typed with or without dashes.")
    while True:
        global menu_dict
        for key in menu_dict:
            print("\t", end="")
            print(key, menu_dict[key])

        do_something = input(">>>")
        user_command(match_with_key(do_something))


def match_with_key(match_this):
    # Get first item in dictionary
    greatest_key = next(iter(menu_dict))

    # Calculate first item's fuzzyness
    fuzzy_later = fuzz.ratio(greatest_key, match_this)

    # Copy to new dict for manipulation
    menu_copy = menu_dict

    # Remove first key to prepare for iteration
    menu_copy.pop(greatest_key)

    # Iterate through each remaining item in the dictionary
    for key in menu_copy:
        fuzzy_now = fuzz.ratio(key, match_this)
        # Compare fuzzyness of current iteration and the previous one
        if fuzzy_now > fuzzy_later:
            greatest_key = key
            fuzzy_later = fuzzy_now

    print("Using command: ", greatest_key)
    return greatest_key


def do_whatever_user_types(user_do):
    print("You entered: ", str(user_do))
    ans_cont = input("Do you wish to continue? (Yes/No) ")
    if fuzz.ratio(ans_cont, "Yes") < fuzz.ratio(ans_cont, "No"):
        sak_menu()
    else:
        next_do = match_with_key(user_do)
        print("My best guess is you want ", next_do)
        user_command(next_do)


def sys_info():
    print(platform.machine())
    print(platform.platform())
    print(platform.system())
    print(platform.processor())
    print(platform.version())
    print(platform.uname())


def check_args():
    for a in sys.argv:
        if os.path.basename(__file__) != a:
            user_command(a)


def binary_convert():
    while True:
        try:
            num = float(input("Enter any number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return bin(num).replace("0b", "")


def hex_convert():
    while True:
        try:
            num = float(input("Enter any number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return hex(num).replace("0x", "")


def check_os():
    if os.name != "posix":
        # sets the text color to red
        os.system("tput setaf 1")
        print("Your operating system is not compatible.")
        print("Operating system must be POSIX compliant.")
        quit_sak()
    else:
        # sets the text colour to green
        os.system("tput setaf 2")
        print("\tYour operating system is POSIX compliant.")


def display_advanced_options():
    detailed_help()


def detailed_help():
    print("Detailed Help for sak!")


if __name__ == "__main__":
    main()
