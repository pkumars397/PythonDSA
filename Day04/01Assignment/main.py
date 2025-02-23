from menu import add_item,remove_item,show_menu
from orders import place_order,calculate_bill

from food_ordering_system.billing import generate_bill,apply_discount
from food_ordering_system.delivery import assign_delivery_executive,estimate_delivery_time

#add items
add_item("Burger",120)
add_item("Pizza",300)
add_item("Pasta",180)
add_item("Sandwich",100)

print("\n Menu: ")
print(show_menu())

#take orders
place_order("Burger")
place_order("Pizza")
place_order("Pasta")

#Calculate and display bills
print("\n Bill details:")
print(generate_bill())
print(apply_discount(10))

#Assign a delivery boy
print("\n Delivery Details: ")
print(f"Assigned Delivery Executive: {assign_delivery_executive()}")
print(estimate_delivery_time(7))
