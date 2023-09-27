from prettytable import PrettyTable
import json
from termcolor import colored
import datetime
import datetime
import random
import time


def main():
    ascii_art = """
███████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗ ██████╗      ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ██╗██╗ ██████╗██╗     ███████╗███████╗
╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗    ██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗  ██║██║██╔════╝██║     ██╔════╝██╔════╝
  ███╔╝ ██║   ██║██╔████╔██║███████║   ██║   ██║   ██║    ██║     ███████║██████╔╝██║   ██║██╔██╗ ██║██║██║     ██║     █████╗  ███████╗
 ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║   ██║    ██║     ██╔══██║██╔══██╗██║   ██║██║╚██╗██║██║██║     ██║     ██╔══╝  ╚════██║
███████╗╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝    ╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚████║██║╚██████╗███████╗███████╗███████║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝╚══════╝╚══════╝
                                                                                                                                        
                                                                                                                       
                                                                    
    """
    print(ascii_art)


main()

 
menu_options = [
    "Menu List",
    "Add A Snack",
    "Delete A Snack",
    "Update Availability of a Snack",
    "Update the Price of a Snack",
    "Record a Sale",
    "Take an Order",
    "Update order Status",
    "Sell Record",
     "Review Orders"
]


styles = [
    {"color": "green", "attrs": ["bold"]},
    {"color": "cyan", "attrs": ["bold"]},
    {"color": "red", "attrs": ["bold"]},
    {"color": "yellow", "attrs": ["bold"]},
    {"color": "magenta", "attrs": ["bold"]},
    {"color": "blue", "attrs": ["bold"]},
    {"color": "white", "attrs": ["bold"]},
    {"color": "red", "attrs": ["bold"]},
    {"color": "cyan", "attrs": ["bold"]},
     {"color": "yellow", "attrs": ["bold"]},
]

add_all = ""

for i, option in enumerate(menu_options):
    style = styles[i]
    formatted_option = colored(f"{i + 1}.   {option}", **style)
    add_all =  add_all + formatted_option + "\n"
  


current_date = datetime.date.today().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().time().strftime("%H:%M:%S")



# with open("orderedfood.json", "w") as json_file:
#     json.dump([{"name":"shuhdanshu"}], json_file)



with open("snacks.json", "r") as json_file:
    existing_snacks = json.load(json_file)

with open("order.json", "r") as json_file:
    sell_data = json.load(json_file)
    
    
with open("orderedfood.json", "r") as json_file:
    ordered_data = json.load(json_file)



table = PrettyTable(["ID", "Name", "Price", "Availability"])
saletable= PrettyTable(["ID", "Name", "Total Sell", "Date of Sell","Time of Sell"])
ordertable= PrettyTable(["Order ID", "Customer name", "Food Ordered","Status", "Date of order","Time of order"])


for item in existing_snacks:
    table.add_row([item["id"], item["name"], item["price"], item["availability"]])
    
for item in sell_data:
    saletable.add_row([item["id"], item["name"], item["total sale"], item["date"], item["time"]])

    
for item in ordered_data:
    ordertable.add_row([item["Order ID"], item["Customer name"], item["Food Ordered"], item["Status"],item["date"], item["time"]])


# print(ordertable)

admin = "admin"
canteen_staff = "staff"
cashier = "cashier"

role = input("Enter Your role(admin, cashier, staff): ")

if role == "admin":
    password = input("Enter password:")
    if password == "1234":
        while True:
            print(add_all)
            user_input = input("Select Your Option: ")

            if user_input == "2":
                while True:
                    snack_id = input("Enter Snack ID: ")
                    if snack_id.isdigit():
                        snack_id = int(snack_id)
                        id_present = any(int(item["id"]) == snack_id for item in existing_snacks)
                        if id_present:
                            print(f"ID {snack_id} is already present in the list.")
                        else:
                            break
                    else:
                        print("Invalid input. Please enter a valid snack ID (numeric).")

                snack_name = input("Enter Snack Name: ")

                while True:
                    snack_price = input("Enter Snack Price: ")
                    if snack_price.isdigit():
                        snack_price = int(snack_price)
                        break
                    else:
                        print("Invalid input. Please enter a valid number for the snack price.")

                snack_availability = input("Enter Snack Availability: ")

                new_snack = {
                    "id": snack_id,
                    "name": snack_name,
                    "price": snack_price,
                    "availability": snack_availability
                }

                existing_snacks.append(new_snack)

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)

                table.add_row([new_snack["id"], new_snack["name"], int(new_snack["price"]), new_snack["availability"]])
                print("\n" + str(table))

            if user_input == "3":
                print(table)
                delete_id = input("Enter ID of Snack to Delete: ")
                for item in existing_snacks:
                    if item["id"] ==  int(delete_id):
                        existing_snacks.remove(item)
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))

            if user_input == "4":
                print("")
                print(table)
                availability_update = input("Enter id of Snack to update Availability: ")
                for item in existing_snacks:
                    if item["id"] == int(availability_update):
                        decide_avail =input("Is the Snack available(yes/no)")
                        item["availability"] = decide_avail
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))

            if user_input == "5":
                price_update_by_name = input("Enter name of Snack to update its Price: ")
                for item in existing_snacks:
                    if item["name"] == price_update_by_name:
                        updated_price = input(f"Enter the updated price for {item['name']}: ")
                        item["price"] = updated_price
                        print("")
                        print("Price Updated Successfully")
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))
                    
            if user_input == "6":
                print("")
                print(table)
                snack_sold_id=  input("Enter the snack ID sold: ")
                snack_qty = input("Enter quantity: ")
                snack_total =0
                snack_sold_name=""
                for item in existing_snacks:
                  
                    if int(snack_sold_id) == item["id"]:
                        snack_sold_name = item["name"]
                        snack_total = int(item["price"]) * int(snack_qty)
                        sell_data.append({"id":int(snack_sold_id), "name":item["name"], "total sale": snack_total, "date":current_date , "time": current_time})
                        break
                
                with open("sellrecord.json", "w") as json_file:
                    json.dump(sell_data, json_file)

                saletable.add_row([int(snack_sold_id), snack_sold_name, snack_total , current_date, current_time ])
                print("\n" + str(saletable))
            
            if user_input == "7":
                # order id, name, food anme, status, price, quantity, total 
                
                print(table)
                food_array =[]
                ordered_food =[]
                cutomer_name = input("Enter cutomer's name: ")
                food_names = input("Enter the id food to order : ")
                food_array.append(food_names)
                status = input("Enter food status: ")
                result_array = [int(num) for num in food_array[0].split()]
                random.seed(time.time())
                order_id = random.randint(1, 1000) 
                for i, num in enumerate(result_array):
                    for item in existing_snacks:
                        if num == item["id"]:
                            ordered_food.append(item["name"])
                            # ordered_data.append({"Order ID":1, "Customer name":item["name"], "Food Ordered": ordered_food, "Status":status,  "date":current_date , "time": current_time})
                            if i == len(result_array) - 1:
                                 ordered_data.append({"Order ID": order_id,
                                     "Customer name": cutomer_name,
                                     "Food Ordered": ordered_food,
                                     "Status": status,
                                     "date": current_date,
                                     "time": current_time})
                            break
                        
                print(ordered_food)           
                 
                with open("orderedfood.json", "w") as json_file:
                    json.dump(ordered_data, json_file)

                ordertable.add_row([order_id, cutomer_name,  ordered_food ,  status, current_date, current_time  ])
                print("\n" + str(ordertable))
                
            if user_input =="8":
                print(ordertable)
                status_id= input("Enter the id of food to change the status: ")
                
                for item in ordered_data:
                    if int(status_id) == item["Order ID"]:
                        changed_status = input("Enter the current status: ")
                        item["Status"] = changed_status
                        break
                    
                with open("orderedfood.json", "w") as json_file:
                    json.dump(ordered_data, json_file)
                    
                    ordertable= PrettyTable(["Order ID", "Customer name", "Food Ordered","Status", "Date of order","Time of order"])
                    for item in ordered_data:
                       ordertable.add_row([item["Order ID"], item["Customer name"], item["Food Ordered"], item["Status"],item["date"], item["time"]])
                    print("\n" + str(ordertable))
                        
                              
            if user_input == "9":
                print(saletable)
            
            if user_input == "1":
                print("\n" + str(table) + "\n")
                print("")
            decision = input("Do you want to close the Canteen (yes/no): ")
            if decision.lower() == "yes":
                    break
    else:
        print("Wrong Password!!")
        
if role == "cashier":
    password = input("Enter password:")
    if password == "1234":
        while True:
            print("")
            print(add_all)
            user_input = input("Select Your Option: ")
            
            if user_input == "6":
                print("")
                print(table)
                snack_sold_id = input("Enter the snack ID sold: ")
                snack_qty = input("Enter quantity: ")
                snack_total = 0
                snack_sold_name = ""
                for item in existing_snacks:
                    if int(snack_sold_id) == item["id"]:
                        snack_sold_name = item["name"]
                        snack_total = int(item["price"]) * int(snack_qty)
                        sell_data.append({"id": int(snack_sold_id), "name": item["name"], "total sale": snack_total, "date": current_date, "time": current_time})
                        break

                with open("sellrecord.json", "w") as json_file:
                    json.dump(sell_data, json_file)

                saletable.add_row([int(snack_sold_id), snack_sold_name, snack_total, current_date, current_time])
                print("\n" + str(saletable))

            elif user_input == "9":
                print(saletable)

            else:
                print("You are not authorized!!")
                
            print("")
            decision = input("Do you want to close the Canteen (yes/no): ")
            if decision.lower() == "yes":
                break
    else:
        print("Wrong Password!!")

if role == "staff":
    password = input("Enter password:")
    if password == "1234":
        while True:
            print("")
            print(add_all)
            user_input = input("Select Your Option: ")
            
            if user_input == "1":
                print("\n" + str(table) + "\n")
      
            
            if user_input == "4":
                print("")
                print(table)
                availability_update = input("Enter id of Snack to update Availability: ")
                for item in existing_snacks:
                    if item["id"] == int(availability_update):
                        decide_avail =input("Is the Snack available(yes/no)")
                        item["availability"] = decide_avail
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))
            
            else:
                print("You are not authorized!!")
            
            print("")
            decision = input("Do you want to close the Canteen (yes/no): ")
            if decision.lower() == "yes":
                break  
    else:
        print("Wrong Password!!")       
                       
else:
    print("Wrong Choice!!")
            
                    
                    
    




            



