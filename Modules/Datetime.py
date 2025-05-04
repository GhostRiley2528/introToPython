from datetime import date  , time , datetime
today = date.today()
now = datetime.now()
print(f"Current date is {today}")
print(f"\n Current date and Time is : {now}" )
print(f"\n Date components are :" , today.year, today.month, today.day )