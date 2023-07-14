# Ordering System in Python
# by Dhanubalde
class Order():
    item = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        # creating an object
        self.item.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        # computing for total order
        # total = quantity * price
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def pay(self, payment_type, security_code):
        # two ways of payment method using credit & debit
        if payment_type == "debit":
            print("Processing Debit payment type")
            print(f"Verifying security code : {security_code}")
            self.status = "paid"

        elif payment_type == "credit":
            print("Processing Credit payment type")
            print(f"Verifying security code : {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()
# adding order item list to cart
order.add_item("flashdrive", 1, 40)
order.add_item("drone", 2, 100)
order.add_item("tv", 1, 20)

# viewing total price
print(order.total_price())
# payment_type and security code
order.pay("credit", "023554525")
