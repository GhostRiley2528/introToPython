import sys
from time import sleep
import calendar
import time

def slow_type(text, delay=0.1):
    for char in text:
        sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()  

def monthy():
    slow_type("Welcome to the Monthly Calendar Viewer!\n", 0.1)
    year = int(input("Enter year (e.g., 2025): "))
    month = int(input("Enter month (1-12)  [NUMBER FORMAT ONLY]: "))
    slow_type(calendar.month(year, month) , 0.1)
    x = input("Want to try again? (y/n) ")
    if x.lower() == "y":
        monthy()
    else:
        slow_type("Shutting down...", 0.3)
        time.sleep(2)
monthy()
