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
    print("Select an option:")
    print("1) Enter tracks to find album length")
    print("2) Enter tracks to split album evenly")
    print(" ) Enter tracks to find ideal side length")
    print("4) Convert min:sec to seconds")
    print("5) Convert seconds to min:sec")
    print("6) Find average track length")
    print("Q) Exit calculator")
    choice = input("> ")

    if choice == "1":
        print("(Enter \'q\' to calculate)")
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
        print("Total album length is " + secToTime(total_time) + ".")

    elif choice == "2":
        print("(Enter \'q\' to calculate)")
        tracks = []
        i = 0
        while (True):
            i += 1
            print("Track " + str(i) + " length (min:sec): ")
            choice = input("> ")
            if isTime(choice):
                tracks.append(timeToSec(choice))
            else:
                break
        if len(tracks) == 0:
            print("It'll be really easy to divide the tracks in your album when there are none.")
        elif len(tracks) == 1:
            print("It'll be really easy to divide the tracks in your album when there\'s only one.")
        elif len(tracks) == 2:
            print("The total album length is " + secToTime(sum(tracks)) + ".")
            print("The album will most evenly be split if track 1 is on Side A (" + secToTime(tracks[0]) + "),")
            print("And track 2 is on Side B (" + secToTime(tracks[1]) + ").")
        else:
            halfway_time = sum(tracks) // 2
            halfway_track = -1
            k = 0
            while (k != len(tracks)):
                if sum(tracks[:k + 1]) >= halfway_time:
                    break
                k += 1
            print(str(halfway_time))
            print("The total album length is " + secToTime(sum(tracks)) + ".")
            print("The album will most evenly be split if tracks 1-" + str(k) + " are on Side A (" + secToTime(sum(tracks[:k])) + "),")
            print("And tracks " + str(k+1) + "-" + str(len(tracks)) + " are on Side B (" + secToTime(sum(tracks[k:])) + ").")
            

    elif choice == "4":
        print("Input time in format (min:sec): ")
        choice = input("> ")
        print(timeToSec(choice))

    elif choice == "5":
        print("Input time in seconds: ")
        choice = input("> ")
        print(secToTime(int(choice)))

    elif choice == "6":
        print("(Enter \'q\' to calculate)")
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
        if total_time == 0:
            print("It doesn\'t seem as if you've input any tracks!")
        else:
            print("The average track length (" + secToTime(total_time) + " / " + str(i - 1) + " tracks) is " + secToTime(total_time // (i - 1)) + ".")

    elif choice == str.lower("q"):
        return 0
    
    print("")
    main()

print("* Cassette Calculator *")
main()

