# Dictionary of countries and their international dialing codes
dialing_codes = {
    "India": "0091",
    "US": "0044",
    "Australia": "0061",
    "Germany": "0049",
    "Japan": "0081",
}

def get_dialing_code(country_name):
    return dialing_codes.get(country_name, "Dialing code not found")

country = input("Enter the country name (United States = US): ")
print(f"The dialing code for {country} is: {get_dialing_code(country)}")
