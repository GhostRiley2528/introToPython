class char:
    players = 'players'

    def __init__(self,name,age):
        self.name = name
        self.age= age

zorro = char("Zorro", 10)
luffy = char("Luffy", 15)

print("Zorro is a", zorro.players)
print("Luffy is a", luffy.players)

print("Zorro's name is", zorro.name, "and age is", zorro.age)
print("Luffy's name is", luffy.name, "and age is", luffy.age)
