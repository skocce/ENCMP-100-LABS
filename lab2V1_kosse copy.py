#%% LAB 2  ENCMP 100 Computer Programming for Engineers
#
# Student name:
# Student CCID:
# Others:
#
# To avoid plagiarism, list the names of others, Version 0 author(s)
# aside, whose code, words, ideas, images, or data you incorporated.
# To avoid unauthorized collaboration, list all others, excluding
# lab instructor and TAs, who gave compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the source's contributions in percent. Supply these
# numbers, which must add to 100%, to receive a nonzero mark.
#
# For obscure and anonymous or known and non-human sources, enter
# pseudonyms or names in uppercase, e.g., DARKWEB or CHATGPT, followed
# by percentages. Send one email to the lab instructor with copies of
# obscure and anonymous sources when you submit your assignment.
#
#%% DECODE  Steganography, Detecting and Decoding a Secret Message
#
# Steganography has been used over millennia to hide information in
# plain sight. This assignment concerns the determination of a secret
# message, about an international rescue, from a list of university
# phone numbers. Each student writes a script to detect if a number
# likely represents a message and, if so, to decode the secret.
#
# Copyright (c) 2024, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
import numpy as np

#%% PARSE INPUT
numStr = input("Enter a number to check:: ")

# Convert the input string into an array of integers (digits)
digits = np.array(list(numStr), dtype=int)

# RULES 1 TO 4
# Rule 1: Check if the number has exactly 11 digits
if len(digits) != 11:
    print("Decoy number: Not eleven digits")

else:
    # Rule 2: Check if the sum of the first five and last five digits are even
    if sum(digits[:5]) % 2 != 0 or sum(digits[6:11]) % 2 != 0:
        print("Decoy number: A digit sum is odd")
    else:
        # Rule 3: Calculate the rescue day number
        rescue_day = digits[8] * digits[7] - digits[6]

        # Map rescue day number to a day of the week
        if rescue_day == 1:
            day = "Sunday"
        elif rescue_day == 2:
            day = "Monday"
        elif rescue_day == 3:
            day = "Tuesday"
        elif rescue_day == 4:
            day = "Wednesday"
        elif rescue_day == 5:
            day = "Thursday"
        elif rescue_day == 6:
            day = "Friday"
        elif rescue_day == 7:
            day = "Saturday"
        else:
            print("Decoy number: Invalid rescue day")
            day = None

        if day:
            # Rule 4: Calculate the rescue place number
            if digits[5] % 3 == 0:
                rescue_place_num = digits[10] - digits[9]
            else:
                rescue_place_num = digits[9] - digits[10]

            # Map rescue place number to a location
            if rescue_place_num == 1:
                place = "medical centre"
            elif rescue_place_num == 2:
                place = "railway station"
            elif rescue_place_num == 3:
                place = "nearest airport"
            elif rescue_place_num == 4:
                place = "village bridge"
            elif rescue_place_num == 5:
                place = "village library"
            elif rescue_place_num == 6:
                place = "village church"
            elif rescue_place_num == 7:
                place = "bus terminal"
            else:
                print("Decoy number: Invalid rescue place")
                place = None

            if place:
                # PRINT OUTPUT: Final rescue message
                print(f"Rescue on {day} at the {place}")
