""" Advent of Code 2023 Day 1: Trebuchet?!

The problem description: 
    --- Day 1: Trebuchet?! ---
    Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

    You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

    As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

    The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

    Consider your entire calibration document. What is the sum of all of the calibration values?

"""

import numpy as np
from pathlib import Path
import re

def get_first_and_last_digit_part1(input_string):
    """Returns the first and last digit of a string which contains alphanumeric characters."""
    # split the string into a numpy array of characters
    characters = np.array(list(input_string))
    # find all the digits in the string
    digits = characters[np.where([c.isdigit() for c in characters])]
    # convert the digits to integers
    digits = digits.astype(int)
    first_digit = digits[0]
    last_digit = digits[-1]
    return first_digit, last_digit

# Edited from https://stackoverflow.com/a/6117042/16164384
def replace_all(text, dic):
    k = np.array([text.find(i) for i, j in dic.items()])
    if np.all(k<0):
        # if no numbers are present, return the text
        return text
    k = np.min(k[k>=0])
    for i, j in dic.items():
        if k == text.find(i):
            text = text.replace(i, j)
    # now recursively call this function until all the substrings have been replaced
    text = replace_all(text, dic)
    return text

number_dict = {"one":"1",
               "two":"2",
               "three":"3",
               "four":"4",
               "five":"5",
               "six":"6",
               "seven": "7",
               "eight": "8",
               "nine": "9"}
all_numbers = ["one","two","three","four","five","six","seven","eight","nine", '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_first_and_last_digit(input_string):
    """Returns the first and last digit of a string which contains alphanumeric characters."""
    print(input_string)
    # first scan the string for substrings of numbers
    ks = [[(m.start(), m.group(0)) for m in re.finditer(t, input_string)] for t in all_numbers]
    # and flatten the list!
    ks = [i for k in ks if len(k)>0 for i in k]
    # Now we know where the numbers are, sort them by the first element of the tuple
    ks.sort(key=lambda x: x[0])
    # and convert it back to a string (I know this is rather silly to convert back and forth)
    number_string = "".join([k[1] for k in ks])

    # and replace them with the corresponding digit
    input_string = replace_all(number_string, number_dict)
    # split the string into a numpy array of characters
    characters = np.array(list(input_string))
    # find all the digits in the string
    digits = characters[np.where([c.isdigit() for c in characters])]
    # convert the digits to integers
    digits = digits.astype(int)
    first_digit = digits[0]
    last_digit = digits[-1]
    return first_digit, last_digit

test_input = ["1abc2",
              "pqr3stu8vwx",
              "a1b2c3d4e5f",
              "treb7uchet"]

test_input_2 = ["two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen"]

if __name__=="__main__":
    test = False #True
    part2 = True
    input_path = Path.cwd().parent / "input.txt"
    print("Looking for input file: ", input_path)
    if input_path.exists() and not test: #is_file():
        print("Input file found.")
        with open(input_path) as f:
            input_data = f.readlines()
    else:
        input_data = test_input_2 if part2 else test_input
        print("Input file not found. Using test input.")
    cals  = []
    for line in input_data:
        first_and_last = get_first_and_last_digit(line)
        cal = int(str(first_and_last[0]) + str(first_and_last[1]))
        #print(cal)
        cals.append(cal)
    print("Sum = ",np.sum(cals))
    print("Done!")
