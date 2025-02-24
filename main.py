import math
import csv
import os

FILE = "datas.csv"      #creating constant variable for file name
users = []      #creating the empty list for users



#this function gives us a number that will be used on different lines in code. we need this function to dont write the same code everytime we need to take number from user
def get_number(text, minimum = -math.inf, maximum = math.inf):      #creating function with parameters to get number from users
    while True:
        try:
            print(text)
            number = float(input("-->"))
        except ValueError:
            print("Please enter correct number number")
            continue
            
        if number < minimum or number > maximum:
            print(f"Number must be in range of {minimum} and {maximum}")
            continue
        
        return number
    
 
    
#this function checks if user enter string or number in input
def get_id_or_name(text):
    print(text)
    name = input("-->")
    try:
        id_ = int(name)
        return id_
    except ValueError:
        print("")
        
    return name
    
    

#after user change data this function will update FILE
def update_data():
    with open(FILE, "w", encoding="UTF-8") as f:
        f.write("id, name, balance\n")
        for user in users:
            f.write(f"{user["id"]},{user["name"]},{user["balance"]}\n")
            


#from the beginning if there is any data in FILE, it will be added in list named users
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



#this function creates loop on users and if function's parameter and any user's name in list have same value, if will return false, which will be used in next function
def unique_user(name):
    for user in users:
        if user["name"] == name:
            print("User is already registered")
            return False
    return True



#this function asks user for name, if user already exists with this name (which will be checked with previous function) it will be stopped. if not user will input first deposit's amount and both, name and deposit will be appended in list with special id. after that FILE will be updated with list's data, at last function will print that new user was registered with it's name
def register_user():
    print("Enter your name")
    name = input("-->")
    if not unique_user(name):
        return
    initial_deposit = get_number("enter amount of initial deposit", 0)
    users.append({
        "id": len(users) + 1,
        "name": name,
        "balance": initial_deposit
    })
    update_data()
    print(f"New user, {name}, was succssesfully registered")



#this function shows every user with id, name and balance
def display_user():
    for user in users:
        print(f"Your ID: {user["id"]}\n{user["name"]}\nYour balance: ${user["balance"]}\n")



#this function changes user's balance, user and amount will be specified with arguments
def change_balance(user, amount):
    user["balance"] += amount



#this function will find user in users list with id
def find_user_by_id(id_):
    for user in users:
        if user["id"] == id_:
            return user
    
    return None



#this function will find user in users list with name
def find_user_by_name(name):
    for user in users:
        if user["name"] == name:
            return user
        
    return None



#this function checks if argument is string or number and with that info user will be found by name or id
def check_int_str(value):
    if type(value) == int:
        user = find_user_by_id(value)
    else:
        user = find_user_by_name(value)
    return user



#we use 5 functions(which are already explained above) in this function. after we will have the user this function will increase user's balance with entered amount
def find_and_deposit():
    info = get_id_or_name("Enter user ID or name")
    user = check_int_str(info)
    if user is None:
        print("Could not find user")
        return
    amount = get_number("Enter amount to deposit:", 0)
    change_balance(user, amount)
    update_data()
    print("Deposit made succssesfully")


    
#this function does and uses same function as previous one but instead of increasing amount, this one will decrease the balance
def find_and_withdraw():
    info = get_id_or_name("Enter user ID or name")
    user = check_int_str(info)
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
    
    

#with this function we will get two users, one will be sender and another will be receiver, we also get amont from sender how many she/he wants to transfer. this function calls change_balance() two times, because we want to update both users balance at the end of this function
def transfer():
    from_ = get_id_or_name("Enter sender's ID or name")
    sender = check_int_str(from_)
    if sender is None:
        print("Could not find user")
        return
    to_who = get_id_or_name("Enter receiver's ID or name")
    receiver = check_int_str(to_who)
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
    
    

#this function will only show the user's balance
def show_balance():
    info = get_id_or_name("Enter name or ID to check your balance")
    user = check_int_str(info)
    print(f"Your balance is ${user["balance"]}")
    
    
def main():
    if os.path.exists(FILE):        #?
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
        if command == "balance":
            show_balance()
        else:
            print("Command does not match any possible operation")
            
main()