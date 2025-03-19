print("Enter marks of all 5 subjects:")
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

t = s1+s2+s3+s4+s5
avg = t/5

if avg>=95 and avg <= 100:
print("Your Grade is A+")

elif avg>=90 and avg<94:
print("Your Grade is A")

elif avg>=80 and avg<89:
print("Your Grade is B")

elif avg>=70 and avg<79:
print("Your Grade is B-")

elif avg>=51 and avg<61:
print("Your Grade is C")

elif avg>=41 and avg<51:
print("Your Grade is C-")

else:
    print("F")
    