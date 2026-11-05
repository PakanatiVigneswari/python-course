'''pin=12345 
for i in range(5):
    e_pin=int(input("Enter the pin: "))
    if e_pin==pin:
        print("Login Successful.")
        break
    else:
        print("Invalid pin")
else:
    print("Max attempts reached! Try after 20 seconds.")
'''


'''l=[12,53,75,79,90,36,58,70]
num=int(input("Enter the number: "))
for i in range(len(l)):
    if l[i] == num:
        print(f"{num} is found at {i}")
        break
else:
    print(f"{num} is not found")'''


#enumerate
'''s = "Krishna"
for i in enumerate(s):
    print(i)'''


'''c = {1,23,56,87,79}
for i in enumerate(c):
    print(i[0],i[1])'''



c = {"k1":"v1","k2":"v2","k3":"v3"}
for i in enumerate(c):
    print(i[0],i[1],c[i[1]])
