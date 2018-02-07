#!/usr/bin/python3

import time

def isTime(str):
    try:
        time.strptime(str, '%M:%S')
        return True
    except ValueError:
        return False

def timeToSec(input):
    return int(input.split(":")[0]) * 60 + int(input.split(":")[1])

def secToTime(input):
    return str(input // 60) + ":" + '{:02d}'.format(input % 60)

def main():
    print("* Cassette Calculator *")
    print("Select an option:")
    print("1) Enter tracks to find album length")
    print("2) Enter tracks to split album evenly")
    print("3) Enter tracks to find ideal side length")
    print("4) Convert min:sec to seconds")
    print("5) Convert seconds to min:sec")
    choice = input("> ")

    if choice == "1":
        print("(Enter \'q\' to quit)")
        total_time = 0
        i = 0
        while (True):
            i += 1
            print("Track " + str(i) + " length (min:sec): ")
            choice = input("> ")
            if isTime(choice):
                total_time += timeToSec(choice)
            else:
                break
        print("Total album length is " + secToTime(total_time))
    elif choice == "4":
        print("Input time in format (min:sec): ")
        choice = input("> ")
        print(timeToSec(choice))
    elif choice == "5":
        print("Input time in seconds: ")
        choice = input("> ")
        print(secToTime(int(choice)))

main()

