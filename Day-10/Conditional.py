'''
product = input("Enter the product: ")
bestseller = eval(input("Enter the status: "))
if bestseller:
    print(f'{product} is best seller.')
'''


'''
battery_charge = int(input("Enter battery: "))
if battery_charge < 20:
    print(f"Battery is low: {battery_charge}, Charge your phone.")
'''


bill=int(input("Enter the bill: "))
status=eval(input("Is it raining? "))
if status:
    bill += 30
    print("Extra Delivary charges applied.")
print(f"Final Bill: {bill}.")