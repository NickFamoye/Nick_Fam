# Imoporting Modules
import printer as printer
import pymongo
import datetime
import pandas as pd
import json
import csv
import pprint
import pandas as pd
from pprint import pprint


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

if __name__ == '__main__':
    db = mongo.Famye['dealership']
    mongo.server_info()

    cars = db['cars']
    customers = db['customers']
    purchases = db['purchases']


    #result = cars.find({'MSRP': {'$eq': 'BMW'}})
    #for result in result:
        #pprint(list(result))
    #result = carscount({'Make': {'$eq':'BMW'}})
    #print(result)query ={'Make': {'$eq':'BMW'}}
    #query ={'Make': {'$eq':'BMW'},'Model': {'$eq':'A3'}}
    #selection = db.cars.find(query).limit(5)
    #for results in selection:
        #pprint(results)

results = cars.find({['Make', 'Model', 'Year', 'Engine HP', 'Vehicle Size', 'Vehicle Style', 'MSRP']})
for result in results:
    pprint(list(result))



#query ={'Make': {'$eq':'BMW'}},{'Model': {'$seq': '3 series'}}
#selection = db.cars.find(query).limit(5)
#for results in selection:
    #print(results)

# Welcome Message and Employee's Information
if __name__ == '__main__':
    print("Welcome to Famye's Dealership!!!\n'WE OFFER COMFORT AND CHOICES")
    print()
    name = input("Employees ID: ")
    message = "Hi Eng.Nick"
    print(message)

# Employees Task Manager
if __name__ == '__main__':
    print()
    x = datetime.datetime.now()
    print('EMPLOYEES', 'TASK', 'MANAGER', 'FOR', x.strftime('%b'), x.strftime('%d'),x.year)
    print([1], 'Car Sales Appointment', x.strftime('%I'), x.strftime('%M'), x.strftime('%p'), x.strftime('%a'), x.strftime('%b'), x.year)
    print([2], 'Create Customers Purchase Record In Collection', x.strftime('%a'), x.strftime('%b'), x.year)
    print([3], 'Read Customers Purchase Collection', x.strftime('%a'), x.strftime('%b'), x.year)
    print([4], 'Update Trade In Cars In Collection', x.strftime('%a'), x.strftime('%b'), x.year)
    print([5], 'Delete Sold Cars In Collection', x.strftime('%a'), x.strftime('%b'), x.year)

# Customer's Purchase Process
# Customer's Personal Information
if __name__ == '__main__':
    print()
    print('Customers information \n Please input your information and preferences')
    First_Name = input("First Name: ")
    Last_Name = input("Last Name: ")
    Return_Customer = input("Are You a Return Customer (Yes / No): ")
    Trade_In = input("Trade In (Yes / No): ")

    print()
    print("Welcome Back " + First_Name + Last_Name + "\n What Are You Looking To Buy?")

    # Cars Inventory
    print()
    print([1], 'Mercedes-Benz')
    print([2], 'Audi')
    print([3], 'BMW')
    print([4], 'FIAT')
    print([5], 'Volvo')
    print([6], 'Mazda')
    print([7], 'Nissan')

    # Customer's Car Preference
    print()
    print("To optimize your search from over 11 thousand inventories \n Please, give more details")
    Make = input("Make: ")
    Year = input("Year: ")
    Model = input("Model: ")
    Drive_Wheel = input("Drive_Wheel: ")


    # Customer's Financial Information
    print()
    Payment_Method = input("Finance or Cash: ")
    Social_Security = input("Please Enter The Last Four Digit Of Your Social Security: ")
    print("Checking Your Eligibility \n Congratulation You Are Approved!!")

# Searching the entire cars inventory
    #results = cars.find({}).pretty()
    #for result in results:
        #print(result)

# QUERIES
# Volvo Inventory ( Filtering query)
    query ={'Make': {'$eq':'Volvo'}}
    selection = db.cars.find(query).limit(4)
    for results in selection:
        print(results)

# BMW Inventory ( Filtering query)
    #query ={'Make': {'$eq':'BMW'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# Mercedes-Benz Inventory ( Filtering query)
    #query ={'Make': {'$eq':'Mercedes-Benz'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# Audi Inventory ( Filtering query)
    #query ={'Make': {'$eq':'Audi'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# FIAT Inventory ( Filtering query)
    #query ={'Make': {'$eq':'FIAT'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# Chrysler Inventory ( Filtering query)
    #query ={'Make': {'$eq':'Chrysler'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# Nissan Inventory ( Filtering query)
    #query ={'Make': {'$eq':'Nissan'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# Mazda Inventory ( Filtering query)
    #query ={'Make': {'$eq':'Mazda'}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

# Mazda Inventory ( Filtering query)
    #query ={'Make': {'Year': 2018}}
    #selection = db.cars.find(query)
    #for results in selection:
        #print(results)

    query = {"Make":'Mazda',
              'Year': 2018,
              'Drive_Wheels': ('all wheel drive', 'rear wheel drive', 'front wheel'),
              'Vehicle size': ('Midsize', 'Compact', 'Convertible')
              }
    selection = db.cars.find(query)
    for results in selection:
        print(results)




# Before Creating index
    #index_list = sorted(list(cars.index_information()))
    #print("Before Creating index")
    #print(index_list)

# Creating customers index
#customers.create_index("Email", unique = True)

# Creating cars index
#cars.create_index("Make", unique = True)

# Defining functions for customer

#results = customers.find({})
#for result in results:
    #print(result)

# db.programmers.remove( { name: "James Gosling" } )
# db.programmers.remove( { name: "James Gosling" } )
# db.programmers.deleteMany( { name: { $in: [ "Dennis Ritchie", "Bjarne Stroustrup" ] } } )
# db.programmers.aggregate([{$group : {_id: "$type", TotalRecords: {$sum : 1}}}])
# db.techSubjects.find({}, {"topic":1, _id:0}).sort({"topic":1})

# { count: { $meta: "textCount" } }
# Here this specified metadata will determine the sort order.
#
# Here is the syntax:
#
# db.collection_name.find(
# <MongoDB query statement>,
# { value: { $meta: <metadataKeyword> } }
# )
# db.techWriter.find({},
# { count: { $meta: "textCount" } }
# ).sort( { count: { $meta: "textCount" } } )


#x = str(input('please the customers payment methods'))
#V = str(input('Volvo'
# Employees login
# Employees presenting a menu with options
# option1- create a new car (add a car to the database, effect change in the car collections)
# option2- Update existing document in a collection
# option3- Option/ Delete