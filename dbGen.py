# Python script that gives an sql data base of item names, price, and image url
# name and price are chosen from a list of names and a range of integers
# image url is a placeholder for now
import random
import sqlite3
import os
import requests
import json
# List of item names
names = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# List of prices
prices = []
for price in range(0,5):
    prices.append(random.randint(1,100))
# List of image urls 
img_urls = ["placeholder"] 
# Connect to the database
con = sqlite3.connect('items.db')
#check response of db connection
if con:
    print("Connected to database")
else:
    print("Failed to connect to database")
    # Create a cursor object
    cur = con.cursor()
    # Create table
    cur.execute("CREATE TABLE items(id, name, price, image_url)")
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
    res.fetchone() is None
    print(res.fetchone())
    



