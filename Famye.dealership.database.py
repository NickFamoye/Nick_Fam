# Imoporting Modules

import printer as printer
import pymongo
import datetime
import pandas
import json
import csv
import pprint
import pandas as pd
# Establsihing Network connection
if __name__ == '__main__':
    try:
        mongo = pymongo.MongoClient(
            host="localhost",
            port=27017,
            serverSelectionTimeoutMS=1000
        )
    except:
        print("Error - Cannot connect to db")

# Creating Mongodb database
    db = mongo.Famye['dealership']
    mongo.server_info()

    # Creating Mongodb Collections
    cars = db['cars']
    customers = db['customers']
    purchases = db['purchases']
    trade_in = db['trade_in']





#query ={'Make': {'$eq':'BMW'}}
#selection = db.cars.find(query).limit(2)
#for results in selection:
    #print(results)

# Welcome Message
if __name__ == '__main__':
    print("Welcome to Famye's Dealership!!!\n'WE OFFER COMFORT AND CHOICES'\n    !!!Thanks!!!")



# QUERIES
# Volvo Inventory ( Filtering query)
    #query ={{'$and':
                 #[{'Make': {'$exists': 'true'}},
                  #{'Model': {'$exists': 'true'}},
                  #{'Drive_Wheel': {'$exists': 'true'}}]}}
    #selection = db.cars.find(query).limit(4)
    #for results in selection:
        #print(results)

        #query ={'Make': {'$eq':'Volvo'}}
        #selection = db.cars.find(query).limit(4)
        #for results in selection:
            #print(results)

# Before Creating index
index_list = sorted(list(cars.index_information()))
print("Before Creating index")
print(index_list)

# Creating customers index
#customers.create_index("Email", unique = True)

# Creating cars index
#cars.create_index("Make", unique = True)

# Defining functions for customer
def add_customers(first_name, last_name, date_of_birth, phone_number, email):
    document = {
        'Fist_Name': first_name,
        'Last_Name': last_name,
        'Date_Of_Birth': date_of_birth,
        'Phone_Number': phone_number,
        'Email': email,
        'Date Added': datetime.datetime.now()
    }
    return customers.insert_one(document)

# Defining functions for customer
def add_customers(first_name, last_name, date_of_birth, phone_number, email):
    document = {
        'Fist_Name': first_name,
        'Last_Name': last_name,
        'Date_Of_Birth': date_of_birth,
        'Phone_Number': phone_number,
        'Email': email,
        'Date Added': datetime.datetime.now()
    }
    return customers.insert_one(document)

# Creating Mongodb Database
# And Collections
def add_tradeIn():
    x = datetime.datetime.now()
    Make = ("Nissan", "Toyota", "Honda", "BMW", "Mazda")
    Model = ("Rouge", "Highlander", "Accord", "3 Series", "Cx60")
    Year = (2018, 2020, 2017, 2015, 2019)
    Engine_HP = (180, 230, 202, 235, 195)
    MSRP = (37400, 49680, 38500, 39330, 34200)
    Date = (x.strftime('%x'), x.strftime('%x'), x.strftime('%x'), x.strftime('%x'), x.strftime('%x'))

    docs = []

    for Make, Model, Year, Engine_HP, MSRP, Date in zip(Make, Model, Year, Engine_HP, MSRP, Date):
        doc = {'Make': Make, 'Model': Model,
               'Year': Year, 'Engine_HP': Engine_HP,
               'MSRP': MSRP, 'Date': Date}
        docs.append(doc)

    trade_in.insert_many(docs)

add_tradeIn()


# Defining functions for purchases
def add_purchases(cars_id, customers_id, payment_method, trade_in, customers_email):
    document = {
        'Cars_Id': cars_id,
        'Customers_Id': customers_id,
        'Payment_Method': payment_method,
        'Trade_in': trade_in,
        'customers_email': customers_email,
        'Date': datetime.datetime.now()
    }
    return purchases.insert_one(document)
#if __name__ == '__main__':
#purchases = add_purchases('cars.inserted_id', 'Financed', 'No', 'customers_email')
#customers = add_customers('Zhel', 'Nichol', 'Oct 11', '339-225-816', 'deal9@gmail.com')
#purchases = add_purchases('cars.inserted_id', 'customers.inserted_id', 'Financed', 'No', 'customers_email')


#Query Ideas
# All cars with price less than 30000
# The count of each brand in inventory
# How many cars are older than 2000
# Average price of all car brands
# car with max price
# Average price of Hondas newer than 2000 by model
# Most expensive car
#document.append(document)
    # QUERIES


# columns = file.readline().split(',')
# file = csv.reader(file)
#columns_needed = ['Make', 'Model', 'Year', 'Engine HP', 'Vehicle Size', 'Vehicle Style', 'MSRP']
#indexs = list(filter(lambda x: columns[x].strip() in columns_needed, [i for i in range(len(columns))]))
#number_columns = {"MSRP", "Year", "Engine HP"}







