class Product:
    def __init__(self, name, price, stock):
        self.__name = name  
        self.__price = price  
        self.__stock = stock  

    def update_stock(self, quantity):
        if quantity >= 0:
            self.__stock = quantity
            print(f"Stock updated to {self.__stock} for {self.__name}.")
        else:
            print("Stock quantity cannot be negative.")

    def sell(self, quantity):
        if 0 < quantity <= self.__stock:
            self.__stock -= quantity
            print(f"Sold {quantity} of {self.__name}. Remaining stock: {self.__stock}.")
        else:
            print("Invalid quantity to sell.")

    def get_info(self):
        return f"Product: {self.__name}, Price: ${self.__price:.2f}, Stock: {self.__stock}"


product = Product("Laptop", 2000, 20)
print(product.get_info())
product.sell(5)
product.update_stock(20)
print(product.get_info())