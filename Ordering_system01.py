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


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        # two ways of payment method using credit & debit
        print("Processing Debit payment type")
        print(f"Verifying security code : {security_code}")
        self.status = "paid"

    def pay_credit(self, order, security_code):
        # two ways of payment method using credit & debit
        print("Processing Credit payment type")
        print(f"Verifying security code : {security_code}")
        self.status = "paid"

    def pay_paypal(self, order, security_code):
        print("Processing Paypal payment type")
        print(f"Verifying security code : {security_code}")
        self.status = "paid"


order = Order()
# adding order item list to cart
order.add_item("flashdrive", 1, 40)
order.add_item("drone", 2, 100)
order.add_item("tv", 1, 20)

# viewing total price
print(order.total_price())
# payment_type and security code
processor = PaymentProcessor()
processor.pay_paypal(order, "02155236654")
