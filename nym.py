# Jamshed Ashurov
# 10/06/2017
# nym.py
# This program creates a game of Nim

import random


def body(pile_1, pile_2):
    """
    This function is used for the human turns of the game. It makes sure that the human makes legal moves and after he
    makes it, this function also calculates the number of stones left in each pile.
    :param pile_1:
    :param pile_2:
    :return:
    """
    print("Pile 1 =", pile_1)
    print("Pile 2 =", pile_2)
    pile = input("Which pile? (1 or 2)")
    if int(pile) == 1:
        print("How many stones?")
        num_of_stones = int(input())
        while True:
            if num_of_stones > 3 or num_of_stones < 1:
                num_of_stones = int(input("Wrong, please input a number between 1 and 3"))
            elif num_of_stones > pile_1:
                print("Please, make sure the number does not go below zero")
                num_of_stones = int(input())
            else:
                break
        pile_1 = pile_1 - num_of_stones
    if int(pile) == 2:
        print("How many stones?")
        num_of_stones = int(input())
        while True:
            if num_of_stones > 3 or num_of_stones < 1:
                num_of_stones = int(input("Wrong, please input a number between 1 and 3"))
            elif num_of_stones > pile_2:
                print("Please, make sure the number does not go below zero")
                num_of_stones = int(input())
            else:
                break
        pile_2 = pile_2 - num_of_stones
    print("You have", pile_1, "left in Pile 1")
    print("You have", pile_2, "left in Pile 2")
    return pile_1, pile_2


def comp(pile_1, pile_2):
    """
    This function is used for the turn of the computer. The computer will randomly pick a number and take a legal
    number of stones fom the pile.
    :param pile_1:
    :param pile_2:
    :return:
    """
    if pile_1 == 0:
        number_of_stones = random.randint(1, 3)
        while True:
            if number_of_stones > pile_2:
                number_of_stones = random.randint(1, 3)
            else:
                break
        pile_2 = pile_2 - number_of_stones
    elif pile_2 == 0:
        number_of_stones = random.randint(1, 3)
        while True:
            if number_of_stones > pile_1:
                number_of_stones = random.randint(1, 3)
            else:
                break
        pile_1 = pile_1 - number_of_stones
    else:
        pile = random.randint(1, 2)
        if pile == 1:
            number_of_stones = random.randint(1, 3)
            while True:
                if number_of_stones > pile_1:
                    number_of_stones = random.randint(1, 3)
                else:
                    break
            pile_1 = pile_1 - number_of_stones
        elif pile == 2:
            number_of_stones = random.randint(1, 3)
            while True:
                if number_of_stones > pile_2:
                    number_of_stones = random.randint(1, 3)
                else:
                    break
            pile_2 = pile_2 - number_of_stones
    print("You have", pile_1, "left in Pile 1")
    print("You have", pile_2, "left in Pile 2")
    return pile_1, pile_2


def main():
    play = input("Would you like to play a game of Nim? (y/n)")
    while play == "y":
        print("Let's go!")
        pile_1 = random.randint(1, 10)
        pile_2 = random.randint(1, 10)
        while True:
            result_1, result_2 = body(pile_1, pile_2)
            if result_1 == 0 and result_2 == 0:
                print("Congratulations! You won")
                break
            pile_1, pile_2 = comp(result_1, result_2)
            if pile_1 == 0 and pile_2 == 0:
                print("Computer won")
                break
        play = input("Would you like to play a game of Nim? (y/n)")
    print("Oh well, next time then")


main()
