import random

def assign_delivery_executive():
 executives=["Amit","Priya","Rohan","Sneha"]
 return random.choice(executives)

def estimate_delivery_time(distance):
 return f"Estimated Delivery tiem : {distance*5}"
 
