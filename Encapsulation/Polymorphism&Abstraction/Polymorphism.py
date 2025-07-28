# India
class India:
    def capital(self):
        return("New Delhi is the capital of India")
    
    def language(self):
        return("Hindi is the language of India")
    
    def type(self):
        return("India is a developing country")
    
#Germany
class Germany:
    def capital(self):
        return("Berlin is the capital of Germany")

    def language(self):
        return("German is the language of Germany")

    def type(self):
        return("Germany is a developed country")

# Polymorphism
def country_info(country):
    print(country.capital())
    print(country.language())
    print(country.type())


I = India()
G = Germany()

country_info(I)
country_info(G)