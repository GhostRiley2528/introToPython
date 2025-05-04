def calculate_stay_cost(days, price_per_day):
    return days * price_per_day

def calculate_ticket_cost(ticket_price, people):
    return ticket_price * people

def calculate_vehicle_cost(daily_rent, days_rented, discount_percent):
    total = daily_rent * days_rented
    discount = total * (discount_percent / 100)
    return total - discount

def total_trip_expenditure():
    print("Trip Expenditure Calculator\n")

    days_stayed = int(input("Enter number of days stayed: "))
    stay_price_per_day = float(input("Enter price of stay per day: "))
    ticket_price = float(input("Enter cost of one ticket per person: "))
    num_people = int(input("Enter total number of people: "))
    vehicle_daily_rent = float(input("Enter daily cost of rented vehicle: "))
    vehicle_rent_days = int(input("Enter number of days vehicle was rented: "))

    discount_percent = 10  

    stay_cost = calculate_stay_cost(days_stayed, stay_price_per_day)
    ticket_cost = calculate_ticket_cost(ticket_price, num_people)
    vehicle_cost = calculate_vehicle_cost(vehicle_daily_rent, vehicle_rent_days, discount_percent)

    total = stay_cost + ticket_cost + vehicle_cost

    print("\n------ Trip Expenditure Bill ------")
    print(f"Stay cost ({days_stayed} days x ₹{stay_price_per_day}): ₹{stay_cost}")
    print(f"Ticket cost ({num_people} people x ₹{ticket_price}): ₹{ticket_cost}")
    print(f"Vehicle rent cost (with {discount_percent}% discount): ₹{vehicle_cost:.2f}")
    print("-----------------------------------")
    print(f"Total Expenditure: ₹{total:.2f}")


total_trip_expenditure()
