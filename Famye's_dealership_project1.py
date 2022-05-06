# Importing Modules
import pymongo
import datetime
import pandas as pd
import csv
import pprint
import json
from pprint import pprint

# Establishing Connection
if __name__ == '__main__':
    try:
        mongo = pymongo.MongoClient(
            host="localhost",
            port=27017,
            serverSelectionTimeoutMS=1000
        )
    except:
        print("Error - Cannot connect to db")

# Creating Mongodb Database
if __name__ == '__main__':
    db = mongo.Famye['dealership']
    mongo.server_info()

# Creating Mongodb Collections
    cars = db['cars']
    customers = db['customers']
    purchases = db['purchases']
    trade_in = db['trade_in']

# Welcome Message and Employee's Information
if __name__ == '__main__':
    print("Welcome to Famye's Dealership!!!\n'WE OFFER COMFORT AND CHOICES")
    name = input("\nEmployees_ID: ")
    message = "Hi Nick"
    print(message)

# Employee's CRUD OPERATION
if __name__ == '__main__':
    print()
    x = datetime.datetime.now()
    print("EMPLOYEE'S CRUD OPERATION FOR TODAY", x.strftime('%b'), x.strftime('%d'), x.year)
    print([1],'Create Trade_In Cars In Collection')
    print([2], 'Car Sales Appointment And Read Customers Record In Collection', x.strftime('%I'),
          x.strftime('%M'), x.strftime('%p'))
    print([3], 'Update Discrepancy In Customers Information In Collection')
    print([4], 'Delete Cars From Year 2000 and Lower In Collection')
    print([5], 'Thanks for your Patronage!!!')

# Iterating Using While Loop
if __name__ == '__main__':
    option = int(input("\nWhat Will You Like To Accomplish Today: "))
    print()
    while option != 5:
        if option == 1:
            print(str(input("Would You Like to View Trade_In Collections \nBefore Creating New Inventories: ")))
            print('\nList Of Trade_In Cars In Collection....')
            results = trade_in.find({})
            for result in results:
                pprint(result)

# Trade_in Cars List
            print("\nList Of Trade_In Cars To Be Created!!")
            print([1], 'Nissan Rouge')
            print([2], 'Toyota Highlander')
            print([3], 'Honda Accord')
            print([4], 'BMW 3 Series')
            print([5], 'Mazda Cx60')
            print(str(input("\nWould You Like to Create Trade_in Cars: ")))

# Creating trade_in cars
            def add_tradeIn():
                x = datetime.datetime.now()
                Make = ("Nissan", "Toyota", "Honda", "BMW", "Mazda")
                Model = ("Rouge", "Highlander", "Accord", "3 Series", "Cx30")
                Year = (2020, 2020, 2017, 2015, 2019)
                Engine_HP = (205, 230, 202, 235, 195)
                MSRP = (37400, 43680, 26500, 30330, 27200)
                Date = (x.strftime('%x'), x.strftime('%x'), x.strftime('%x'), x.strftime('%x'), x.strftime('%x'))

                docs = []

                for Make, Model, Year, Engine_HP, MSRP, Date in zip(Make, Model, Year, Engine_HP, MSRP, Date):
                    doc = {'Make': Make, 'Model': Model,
                           'Year': Year, 'Engine_HP': Engine_HP,
                           'MSRP': MSRP, 'Date': Date}
                    docs.append(doc)

                trade_in.insert_many(docs)
                for results in docs:
                    pprint(results)
            add_tradeIn()

# Extracting customers Information For Query and Update purposes
        print()
        if option == 2:
            print("Car sales in progress.....")
            import Customer_module
            print()

# Checking for index
            index_list = sorted(list(customers.index_information()))
            print("Filtering And Optimising Search Using index")
            print(index_list)
            print(str(input("How Would you Like To Optimize Your Search : ")))
            print()

# Optimizing Search using email
            results = customers.find({'Email': 'deal2@gmail.com'})
            for result in results:
                pprint(result)
                print()
            import cars_module
            print()

#Audi Inventory ( Filtering query)
            query ={'Make': {'$eq':'Audi'}, 'Year': '2017', 'Model': {'$eq': 'A3'},
                    'Driven_Wheels': {'$eq': 'all wheel drive'}}
            selection = db.cars.find(query).limit(3)
            for results in selection:
                pprint(results)
                print()

            pprint('_id ObjectId(626c4bb717bfecef77265b33) Make: Audi, Model A3, Year, 2017')
            print("SOLD", (x.strftime('%x')))
            print()
            print("Read Customer's Information and \nCar sales Accomplished....")

            print()
        elif option == 3:
            print('Update Discrepancy In Customers Information')
            print('\nPhone_Number In Record : 333-445-4433')
            print('New Phone_Number : 333-555-6655')
            print(str(input("Would You Like to Update Customers Phone_Number : ")))
            my_query = {"Phone_Number": "333-445-4433"}
            new_update = {"$set": {"Phone_Number": "333-555-6655"}}
            db.customers.update_one(my_query, new_update)
            results = customers.find({'Email': 'deal2@gmail.com'})
            for result in results:
                pprint(result)
            print('\nUpdate Discrepancy In Customers Information Accomplished....')

#Delete_Many
        elif option == 4:
            print('Delete Cars From Year 2000 and Lower In Collection')
            print(str(input("This Is A Max Deletion Are Sure You Want To Delete: ")))
            print(str(input("To Delete, Please Login Your Employee_ID: ")))
            sold_cars = {'Year': {'$lt': '1995'}}
            x = cars.delete_many(sold_cars)
            print(x.deleted_count, " documents deleted.")
            print()

            sold_cars = {'Year': {'$lt': '1995'}}
            x = cars.find(sold_cars).limit(4)
            for result in x:
                pprint(result)
# Draw 4 bars
            import matplotlib.pyplot as plt
            import numpy as np
            d = datetime.datetime.now()

            x = np.array(["CREATE", "READ", "UPDATE", "DELETE"])
            y = np.array([4, 8, 12, 16])

            plt.title("FAMYE'S DEALERSHIP CRUD OPERATION MAY 6TH, 2022")
            plt.xlabel("EXPECTATIONS")
            plt.ylabel("ACCOMPLISHMENT")
            plt.bar(x,y)
            plt.show()

        elif option == 5:

            print('\nThanks for your Patronage!!!')

        else:
            print("Create Trade_In Cars In Collection Accomplished.....")
        option = int(input("What Will You Like To Accomplish: "))


# CRUD OPERATION ACCOMPLISHED
    print("\nFamye's Dealership!!!\n'WE OFFER COMFORT AND CHOICES!!!")
    print("\nIf You can Predict!!!\n'YOU CAN MITIGATE...")
    print("\nTHANK YOU FOR YOUR TIME...")



