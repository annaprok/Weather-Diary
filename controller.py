from model import *


def printDay(elem):
    print("id: " + str(elem["id"]) + " Date:" + elem['date'] + " t = " + str(elem['temperature']) + " in the yard is" + elem['weather'])


while True:
    x = 0
    while x < 1 or x > 4:
        print("---weather forecast---")
        print("1) get all the data from the diary")
        print("2) get by id")
        print("3) add new day")
        print("4) delete some day")
        x = int(input())
        if x < 1 or x > 4:
            print("enter 1, 2, 3 or 4")
    if x == 1:
        days = getAll()
        for day in days:
            printDay(day)
        r = input("press x to exit or any key to go back ")
        if r == "x":
            break
    else:
        if x == 2:
            id = int(input("Enter id"))
            printDay(getById(id))
            r = input("press x to exit or any key to go back ")
            if r == "x":
                break
        else:
            if x == 3:
                id = int(input("Enter id "))
                t = int(input("Enter temperature "))
                w = input("Enter weather type ")
                if add(id, t, w):
                    print("Added")
                else:
                    print("not added")
                r = input("press x to exit or any key to go back ")
                if r == "x":
                    break
            else:
                if x == 4:
                    id = int(input("Enter id "))
                    if getById(id):
                        print("Deleted element:")
                        printDay(delById(id))
                    else:
                        print("Error")
                    r = input("press x to exit or any key to go back ")
                    if r == "x":
                        break
