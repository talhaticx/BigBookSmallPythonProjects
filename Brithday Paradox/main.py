import random
import datetime
from rich.progress import track

SIMULATION = 100_000

def getBirthdays(num=50):
    """Return a list of random dates

    Args:
        num (int): Number of Birthdays

    Returns:
        list: birthdays list
    """
    birthdays = []
    for i in range(num):
        startOfYear = datetime.date(2000,  1, 1)
        randomDays = datetime.timedelta(random.randint(0, 364))
        
        birthday = startOfYear + randomDays
        birthdays.append(birthday)
    
    return birthdays

def  printBDays(bdays):
    """Prints Dates

    Args:
        bdays (list): list of dates to be printed
    """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for bday in range(len(bdays)):
        if bday % 4 == 0:
            print()
        if bday == len(bdays) - 1:
            print("{} %2d".format(months[bdays[bday].month-1]) % (bdays[bday].day))
            # print("{} {}".format(months[bdays[bday].month-1], bdays[bday].day))
            # print("{} {}".format(bdays[bday].month, bdays[bday].day))
        else:
            print("{} %2d".format(months[bdays[bday].month-1]) % (bdays[bday].day), end=",   ")
            # print("{} {}".format(bdays[bday].month, bdays[bday].day), end=", ")
    print()

def check(bdays):
    """
    Check if there are any duplicate birthdays in the given list.

    Args:
    bdays (list): A list of datetime.date objects representing birthdays.

    Returns:
    bool: True if there are duplicate birthdays, False otherwise.
    """
    if len(bdays) == len(set(bdays)):
        return False
    return True

def findCommon(bdays):
    common = []
    for i in range(len(bdays)):
        for j in range(i+1, len(bdays)):
            if bdays[i] == bdays[j]:
                common.append(bdays[i])
    return common

def main():
    while True:
        print("Enter the number of Birthdays: ", end="")
        numBDays = input()
        if numBDays.isdecimal and int(numBDays) > 0:
            numBDays = int(numBDays)
            break
    bdays = getBirthdays(numBDays)
    
    printBDays(bdays)
    common = findCommon(bdays)
    if len(common) == 0:
        print("No common birthday found.")
    else:
        print("The common birthday(s) are:  ")
        printBDays(list(set(common)))
    
    print(f"Ready to run simulation {SIMULATION} times...")
    input("Press Enter to continue...")
    
    counter = 0
    for i in track(range(SIMULATION), description="Simulating"):
        bdays = getBirthdays(numBDays)
        if check(bdays):
            counter += 1
    
    print("\nSimulation completed. {} out of 100,000 simulations resulted in a common birthday.".format(counter))
    print("\nThe probability of having a common birthday is: {:.2f}%".format(counter / SIMULATION * 100))
    
if __name__ == "__main__":
    main()