print("Welcome to the Weekend Planner")
budget=int(input("Enter your budget: "))
print("You can go for",end=' ')
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort")
elif budget > 2000:
    print("Cafe")
elif budget > 1000:
    print("Movie")
elif budget > 500:
    print("Street Shopping")
else:
    print("You can't have enough budget")
