import math
import csv
import os

FILE = "datas.csv"      #creating constant variable for file name
users = []      #creating the ampty list for users


#this function gives us a number that will be used on different lines in code. we need this function to dont write the same code everytime we need to take number from user
def get_number(text, minimum = -math.inf, maximum = math.inf):      #creating function with parameters to get number from users
    while True:
        try:        #trying to get correct number from user
            print(text)
            number = float(input("-->"))
        except ValueError:    #if we dont get correct number from user, program will ask again to change number
            print("Please enter correct number number")
            continue
            
        if number < minimum or number > maximum:        #setting range for number
            print(f"Number must be in range of {minimum} and {maximum}")
            continue
        
        return number       #returning number, which will be used 
    
    
    
def update_data():
    with open(FILE, "w", encoding="UTF-8") as f:
        f.write("id, name, balance\n")
        for user in users:
            f.write(f"{user["id"]},{user["name"]},{user["balance"]}\n")
            


def loading_users():
    with open(FILE) as f:
        f.readline()
        for line in csv.reader(f):
             id_, name, balance, = line
             id_ = int(id_)
             balance = float(balance)
             users.append({
                 "id": id_,
                 "name": name,
                 "balance": balance
             })



def register_user():
    print("Enter your name")
    name = input("-->")
    initial_deposit = get_number("enter amount of initial deposit", 0)
    users.append({
        "id": len(users) + 1,
        "name": name,
        "balance": initial_deposit
    })
    update_data()
    print(f"New user, {name}, was succssesfully registered")



def display_user():
    for user in users:
        print(f"Your ID: {user["id"]}\n{user["name"]}\nYour balance: ${user["balance"]}")


   
def change_balance(user, amount):
    user["balance"] += amount


   
def find_user(id_):
    for user in users:
        if user["id"] == id_:
            return user
    
    return None



def find_and_deposit():
    id_ = get_number("Enter user ID", 1)
    user = find_user(id_)
    if user is None:
        print("Could not find user")
        return
    amount = get_number("Enter amount to deposit:", 0)
    change_balance(user, amount)
    update_data()
    print("Deposit made succssesfully")


    
def find_and_withdraw():
    id_ = get_number("Enter user ID", 1)
    user = find_user(id_)
    if user is None:
        print("Could not find user")
        return
    amount = get_number("Enter amount to withdraw:", 0)
    if user["balance"] < amount:
        print("Not enough money on balance")
        return
    change_balance(user, -amount)
    update_data()
    print("succssesfully withdraw")
    
    

def transfer():
    from_ = get_number("Enter Your ID", 1)
    sender = find_user(from_)
    if sender is None:
        print("Could not find user")
        return
    to_who = get_number("Enter receiver's ID", 1)
    receiver = find_user(to_who)
    if receiver is None:
        print("Could not find user")
        return
    amount = get_number("Enter amount to transfer", 0)
    if sender["balance"] < amount:
        print("Not enough money on balance")
        return
    change_balance(sender, -amount)
    change_balance(receiver, amount)
    update_data()
    print(f"${amount} transfered succssesfully")
    
    
def main():
    if os.path.exists(FILE):
        loading_users()
    while True:
        print("\n", "-" * 30, "\n", sep="")
        command = input("Enter command for operation:\n-->")
        if command == "add":
            register_user()
        if command == "list":
            display_user()
        if command == "deposit":
            find_and_deposit()
        if command == "withdraw":
            find_and_withdraw()
        if command == "transfer":
            transfer()
        else:
            print("Commant does not match any possible operation")
            
main()