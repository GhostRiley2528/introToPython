import time
import random

def randate (startDate , endDate):
    print(f"Printing random date between {startDate} and {endDate}")
    randomd = random.random()
    dateFormat = '%d/%m/%Y'
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + randomd * (endTime - startTime)
    randomDate = time. strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", randate("1/1/2016", "12/12/2018"))