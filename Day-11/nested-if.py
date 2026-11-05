data = {
    "Krishna":{"status":True,"python": 99,"mysql":98,"fastapi":99},
    "Ram":{"status":True,"python": 93,"mysql":95,"fastapi":98},
    "Shiva":{"status":True,"python": 92,"mysql":94,"fastapi":92},
    "Govinda":{"status":True,"python": 96,"mysql":97,"fastapi":91},
    "Ravi":{"status":False,"python": None,"mysql":None,"fastapi":None},
}
name = input("Enter your name: ")
if name in data:
    if data[name]["status"]:
        total = data[name]["python"]+data[name]["mysql"]+data[name]["fastapi"]
        avg=total/3
        if avg > 80:
            print(f"Congrates {name}. You got the first grade.")
        elif avg > 60:
            print(f"Good work {name}.")
        elif avg > 40:
            print(f"Good {name}. Workhard.")
        elif avg >= 35:
            print(f"You just passed {name}.")
        else:
            print(f"You failed the exam {name}.")
    else:
        print(f"You are absent for the exam {name}. Give the reason for this.")
else:
    print(f"{name} is not found in the data.")



