#!/usr/bin/python3

import time

def isTime(choice):
    try:
        time.strptime(choice, '%M:%S')
        return True
    except ValueError:
        return False

def main():
    print("* Cassette Calculator *")
    print("Select an option:")
    print("1) Enter tracks to split album evenly")
    print("2) Enter tracks to find ideal side length")
    choice = input("> ")

    if choice == "1":
        print("(Enter \'q\' to quit)")
        tracks = []
        for i in range(1, 1000):
            print("Track " + str(i) + " length (min:sec): ")
            choice = input("> ")
            if isTime(choice):
                tracks += (i, choice)
            if str.lower(choice) == "quit" or str.lower(choice) == "q":
                break
        total_time = 0
        print(tracks[1])
        # for i in range(0, len(tracks)

main()
