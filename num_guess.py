#!/usr/bin/env python3
# Created by Marc Coffi
# Created in March 2022
# This is a guess the number game

import constants


def main():
    print("This is a number guessing game.")

    user_input = input("Enter a number between 0 and 9: ")

    user_num = int(user_input)

    if user_num == constants.NUMBER:
        print("You guessed correctly!")

    if user_num != constants.NUMBER:
        print("You guessed wrong :(")


if __name__ == "__main__":
    main()
