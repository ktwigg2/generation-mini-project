import pandas as pd 
from sys import exit

# File locations stored as global variables
products = "C:/Users/Generation UK&I/generation python course/mini project 1/data/products.csv"
couriers = "C:/Users/Generation UK&I/generation python course/mini project 1/data/couriers.csv"
orders = "C:/Users/Generation UK&I/generation python course/mini project 1/data/orders.csv"



def main_menu():                                      
    print("\nMAIN MENU\n")
    print("Type 0 to close")
    print("Type 1 for product menu options")
    print("Type 2 to go to orders menu")
    print("Type 3 to go to couriers menu")
    main_menu_option = input("Type here: ")
    if main_menu_option == "0":
        exit()
    elif main_menu_option == "1":
        product_menu()
    elif main_menu_option == "2":
        orders_menu() 
    elif main_menu_option == "3":
        couriers_menu()

def product_menu():                                     
    print("\nPRODUCT MENU\n")
    print("Type 0 to return to main menu")
    print("Type 1 to display the list of products")
    print("Type 2 to add a new product")
    print("Type 3 to update a product")
    print("Type 4 to delete a product")
    product_menu_option = input("Type here: ")
    if product_menu_option == "0":
        main_menu()
    elif product_menu_option == "1":
        print("\nList of products:")
        df = pd.read_csv(products)
        print(df)
        input("\nPress enter to return to products menu.")
        product_menu()
    elif product_menu_option == "2":
        add_product_menu()
    elif product_menu_option == "3":
        update_product_menu()
    elif product_menu_option == "4":
        delete_product_menu()

def add_product_menu():
    df = pd.read_csv(products)
    print(df)
    new_pname = input("Please enter the new product name or press enter to return to product menu: ")
    if new_pname == "": # No input will redirect to product menu
        product_menu()
    else:
        new_pid = df.index # I chose to implement product ID by index because I was struggling to implement other methods
        new_pprice = input("Please enter the new product price: ")
        new_product = [new_pname, float(new_pprice), new_pid] # Storing the product name, price, and product ID in new_product
        print(new_product)
        df.loc[-1] = new_product # using df.loc[-1] to place the new_product dictionary at the last index
        df = df.reset_index(drop = True) # resets index
        df['p_id'] = range(1, 1+len(df)) # To be honest I'm not sure how this works, but it allows my p_id to be stored properly
        df.to_csv(products, index=False) 
        print(df)
        input("Press enter to return to products menu.")
    product_menu()

def update_product_menu():
    df = pd.read_csv(products)
    print(df)
    update_product = input("Please enter the index number of the product you would like to add or press enter to return to previous menu: ")
    if update_product == "":
        product_menu()
    new_product = input("Please enter the new product name or press enter to skip: ") # new_product is the name of the replacement item 
    if new_product == "":
        pass # Using pass allows to skip this without overwriting anything, should the user only want to access the price
    else:
        df.loc[int(update_product), "product"] = new_product # Placing new_product at the location of the chosen index and in the product column
    new_price = input("Please enter the new product price or press enter to skip: ")
    if new_price == "":
        pass
    else:
        df.loc[int(update_product), "price"] = float(new_price) 
        print(df)
    df.to_csv(products, index = False) 
    input("Press enter to return to product menu: ")
    product_menu()

def delete_product_menu():
    print("\nList of products")
    df = pd.read_csv(products)
    print(df)
    delete_product = input("Please enter the index number of the product you want to delete or press enter to return to the previous menu: ")
    if delete_product == "":
        pass
    else:
        df = df.drop(labels=int(delete_product), axis = 0) 
        df.to_csv(products, index=False) # When saving a csv file, 'index=False is important to avoid pandas writing the index values to a new column in the CSV.
        print(df)
        input("Press enter to return to product menu.")
    product_menu()    

def orders_menu():
    print("\nORDERS MENU\n")
    print("Type 0 to return to main menu")
    print("Type 1 to display the list of orders")
    print("Type 2 to add a new order")
    print("Type 3 to update an orders status")
    print("Type 4 to update an order")
    print("Type 5 to delete an order")
    orders_menu_option = input("Type here: ")
    if orders_menu_option == "0":
        main_menu()
    elif orders_menu_option == "1": 
        df = pd.read_csv(orders)
        print(df)
        sortby = input("\nTo return to previous menu press enter, to sort orders by courier type 1, to sort by delivery status type 2: ")
        if sortby == "": 
            orders_menu()
        elif sortby == "1":
            sorteddf = df.sort_values("Courier") # A function provided by Pandas library lets you sort by values, in this case the column "Courier"
            print(sorteddf) # I store the sorted values in sorteddf and print that 
            input("To return to the couriers menu press enter")
            orders_menu()
        elif sortby == "2":
            sorteddf = df.sort_values("Status")
            print(sorteddf)
            input("To return to the orders menu press enter")
            orders_menu()
    elif orders_menu_option == "2":
        add_order()
    elif orders_menu_option == "3":
        update_order_status()
    elif orders_menu_option == "4":
        update_order()
    elif orders_menu_option == "5":
        delete_orders_menu()

def add_order():
    df = pd.read_csv(orders)
    nname = input("Please enter name: ")
    naddress = input("Please enter address: ")
    nnumber = input("Please enter phone number: ")
    prod_df = pd.read_csv(products)
    print(prod_df) 
    items = input("Please enter the ID of the product you would like to buy, for multiple items separate the IDs by commas: ")
    dfcourier = pd.read_csv(couriers) # Reading and printing the couriers file to display a list of available couriers
    print(dfcourier)
    selected_courier = input("Please enter the index number of the courier you would like to assign: ")
    ncourier = (int(selected_courier))
    nstatus = "PREPARING" # automatically setting order status to preparing
    new_order = [nname, naddress, int(nnumber), int(ncourier), nstatus, items]
    df.loc[-1] = new_order
    df = df.reset_index(drop = True) # resets index
    df.to_csv(orders, index = False)
    print(df)
    orders_menu()

def update_order_status():
    df = pd.read_csv(orders)
    print(df)
    update_status = input("Please select the index number of the order you would like to update: ")
    order_statuses = ["PREPARING", "SHIPPED", "DELIVERED", "CANCELLED"]
    for i, status in enumerate(order_statuses): # using enumerate to print the indices and statuses of order_statuses
        print(i, status)
    new_status = input("Select the new status by typing the index value above: ")
    df.loc[int(update_status), "Status"] = order_statuses[int(new_status)] # Replacing the status of accessed file with that of the selected index value
    df = df.reset_index(drop = True) # resets index. I don't think this is needed now but it fixed an issue I was having with my indexes
    df.to_csv(orders, index = False)
    input("Press enter to return to orders menu.")
    orders_menu()

def update_order():
    df = pd.read_csv(orders)
    print(df)
    update_order = input("Please select the index number of the order you would like to update: ")
    new_name = input("Enter the new name or press enter to skip: ")
    if new_name == "":
        pass
    else:
        df.loc[int(update_order), "Name"] = new_name
    new_address = input("Enter the new address or press enter to skip: ")
    if new_address == "":
        pass
    else:
        df.loc[int(update_order), "Address"] = new_address
    new_phone = input("Enter the new phone number or press enter to skip: ")
    if new_phone == "":
        pass
    else: 
        df.loc[int(update_order), "Phone number"] = new_phone
    courier_df = pd.read_csv(couriers)
    print(courier_df)
    new_courier = input("Please enter the index value of the new courier or press enter to skip: ")
    if new_courier == "":
        pass
    else:
        df.loc[int(update_order), "Courier"] = int(new_courier)
    print(df)
    df.to_csv(orders, index = False)
    input("Press enter to return to orders menu.")
    orders_menu()

def delete_orders_menu():
    print("\nList of orders")
    df = pd.read_csv(orders)
    df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
    print(df)
    delete_order = input("Please enter the index number of the order you want to delete or type 'exit' to return to the previous menu: ")
    if delete_order == "exit":
        orders_menu()
    else:
        df = df.drop(labels=int(delete_order), axis = 0)
        df.to_csv(orders, index=False) # When saving a csv file, 'index=False is important to avoid pandas writing the index values to a new column in the CSV.
    print(df)
    input("Press enter to return to orders menu.")
    orders_menu()

def couriers_menu():
    print("\nCOURIERS MENU\n")
    print("Type 0 to return to main menu")
    print("Type 1 to display the list of couriers")
    print("Type 2 to add a new courier")
    print("Type 3 to update a courier")
    print("Type 4 to delete a courier")
    courier_menu_option = input("Type here: ")
    if courier_menu_option == "0":
        main_menu()
    elif courier_menu_option == "1":
        df = pd.read_csv(couriers)
        print(df)
        input("Press enter to return to couriers menu.")
        couriers_menu()
    elif courier_menu_option == "2":
        add_courier_menu()
    elif courier_menu_option == "3":
        update_courier_menu()
    elif courier_menu_option == "4":
        delete_courier_menu()

def add_courier_menu():
    df = pd.read_csv(couriers)
    print(df)
    new_cname = input("Please enter the courier's name: ")
    new_cnumber = input("Please enter the courier's phone number: ")
    new_courier = [new_cname, int(new_cnumber)]
    print(new_courier)
    df.loc[-1] = new_courier
    df = df.reset_index(drop = True) # resets index
    df.to_csv(couriers, index=False)
    print(df)
    input("Press enter to return to couriers menu.")
    couriers_menu()

def update_courier_menu():
    df = pd.read_csv(couriers)
    print(df)
    update_courier = input("Please select the index number of the courier you would like to update: ")
    update_courier_name = input("Please enter the new courier name or press enter to skip: ")
    if update_courier_name == "":
        pass
    else: 
        df.loc[int(update_courier), "name"] = update_courier_name
    update_courier_number = input("Please enter the new phone number or press enter to skip: ")
    if update_courier_number == "":
        pass
    else: 
        df.loc[int(update_courier), "number"] = update_courier_number
    print(df)
    df.to_csv(couriers, index=False)
    couriers_menu()

def delete_courier_menu():
    print("\nList of couriers")
    df = pd.read_csv(couriers)
    # df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
    print(df)
    delete_courier = input("Please enter the index number of the courier you want to delete or type 'exit' to return to the previous menu: ")
    if delete_courier == "exit":
        orders_menu()
    else:
        df = df.drop(labels=int(delete_courier), axis = 0)
        df.to_csv(couriers, index=False) # When saving a csv file, 'index=False is important to avoid pandas writing the index values to a new column in the CSV.
    print(df)
    input("Press enter to return to couriers menu.")
    couriers_menu()

main_menu()


