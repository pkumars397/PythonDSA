from menu import menu_items
orders=[] #for storing ordered items

def place_order(item):
  if item in menu_items:
   orders.append(item)
   print(f"done '{item}' added to the order")
  else:
   print(f"X '{item}' is not availabe in menu")

def calculate_bill():
  total=sum(menu_items[item] for item in orders)
  return total

