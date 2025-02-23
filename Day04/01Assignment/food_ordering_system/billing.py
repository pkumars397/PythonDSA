from orders import calculate_bill
def generate_bill():
 total=calculate_bill()
 return f"Total Bill: ${total}"

def apply_discount(discount_percentage):
 total=calculate_bill()
 discount_price=total-(total*discount_percentage/100)
 return f"Discounted Bill: ${discount_price}"

