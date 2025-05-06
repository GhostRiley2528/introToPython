# rainy = 1  , sunny = 0 , predict the weather using tuple

x = (1 , 0 , 0 , 0 ,1 , 1 , 0)
s = 0
r = 0
for i in x:
    if i ==1:
        s += 1
    else:
        r += 1
print("The number of sunny days are: ", s)
print("The number of rainy days are: ", r)
if s > r:
    print("The weather will most probably be sunny")
elif s == r:
    print("The weather is unpredictable")
else:
    print("The weather will most probably be rainy")

