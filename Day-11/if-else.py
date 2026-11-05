'''
data=("krishna@gmail.com","radhakrishna")
gmail=input("Enter the mail: ")
password=input("Enter the password: ")
if (gmail, password) == data:
    print("Login successful")
else:
    print("Invalid Login")
'''




'''
seats={
    "s1":"Booked",
    "s2":"Available",
    "s3":"Available",
    "s4":"Available",
    "s5":"Booked",
    "s6":"Available",
}
seat_number=input("Enter seat_number: ")
if seat_number in seats and seats[seat_number] == "Available":
    seats[seat_number] = "Booked"
    print(f"{seat_number} is booked successfully.")
    print(seats)
else:
    print(f"{seat_number} is already booked. Select another seat.")
'''


products={
    "laptop":{"price":40000,"stock":10},
    "mouse":{"price":400,"stock":0},
    "keyboard":{"price":2000,"stock":3},
    "tab":{"price":20000,"stock":5},
    "phone":{"price":60000,"stock":8},
    
}
search =input("Enter the product: ")
if search in products and products[search]["stock"] > 0:
    print(f"{search} is available. You can buy this product at ${products[search]["price"]}.")
else:
    print(f"{search} is not available.")
