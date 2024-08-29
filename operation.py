from read import *
from write import *
import datetime

def validate_form(method):
    
    if method == "buy":
        message = "purchase"
    else:
        message = "sell"
    while True:
        total_items = store()
        updated_data = item_form(message,total_items)

        if not updated_data:
            continue
        update_store(updated_data,method)
        break


def update_store(item_data, method):

    invoice_data = {
        'items':[],
        'purchase_date_time':''
        }

    while True:
        with open("store.txt","r") as outfile:
            output = outfile.readlines()

    
        with open("store.txt",'w') as f:
            for index,line in enumerate(output,1):           
                if index == item_data['item_number']:   
                    li = line.split(",")
                
                    old_quantity = int(li[3])

                    if len(invoice_data['items']) == 0:
                        invoice_data['items'].append({
                                    'item_name': li[0],
                                    'brand':li[1],
                                    'price': int(li[2][2:]),
                                    'quantity': item_data['quantity']
                            })
                    else:
                        for item in invoice_data['items']:
                            if item['item_name'] == li[0]:
                                item['quantity'] += item_data['quantity']
                            else:
                                invoice_data['items'].append({
                                        'item_name': li[0],
                                        'brand':li[1],
                                        'price': int(li[2][2:]),
                                        'quantity': item_data['quantity']
                                })


                    if method == "buy":
                        new_quantity = old_quantity + item_data['quantity']
                    elif method == "sell":
                        if old_quantity > item_data['quantity']:
                            new_quantity = old_quantity - item_data['quantity']
                        else:
                            print("Stock Not Available!")
                            f.writelines(line)
                            continue
                    else:
                        raise Exception('Invalid method')
            
                    #Adding space for proper formating
                    li[3] = " " + str(new_quantity)
                    updated_line = ",".join(li)

                    f.writelines(updated_line)
                else:
                    f.writelines(line)
                    
        validate = input(f"Do you want to choose more? (y/n): ")

        if validate.lower() == "y":
            total_items = store()
            item_data = item_form("purchase",total_items)
        else:
            break


    invoice_data['purchase_date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    generate_invoice(invoice_data, method)

def item_form(message, total_items):
    item_data = {'item_number':0,'quantity':0}
    item_choose = int(input(f"Please select a laptop of your choice (1-{total_items}):  "))

    if item_choose > 0 and item_choose <= total_items: 

        item_data['item_number'] = item_choose 
        print()
    
        validate = input(f"Are you sure you want to confirm item {item_choose}? (y/n): ")

        if validate.lower() == "y":
            print(f'You have successfully selected item number {item_choose}')
            print()

            item_quantity = int(input(f"Please select the quantity you want to {message}:  "))

            validate_quantity = input(f"Are you sure you want to confirm quantity {item_quantity}? (y/n): ")
            
            if validate.lower() == "y":
                print(f'You will {message} {item_quantity} items')
                print()
                item_data['quantity'] = item_quantity
                return item_data
            else:
                return False
        else:
            return False
    else:
        print('invalid input! Enter the correct input.')