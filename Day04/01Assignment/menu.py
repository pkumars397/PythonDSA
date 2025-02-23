menu_items={}
def add_item(itemName,price):
 menu_items[itemName]=price

def remove_item(iname):
 if iname in menu_items:
   del menu_items[iname]
 else:
   print(f"Item '{iname}' not found in menu.")
   
def show_menu():
 return menu_items
