def total_calc(bill_amount,tip_perc):
    total= bill_amount*(1+ 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")

    x = int(input("Please ennter the amount of the bill:  "))
    y = int(input("Enter the denominations of coins used (in cents): "))