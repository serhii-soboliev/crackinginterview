class ArrayOfProducts:

    def __init__(self, input_array):
        self.input_array = input_array

    def build_products(self):
        previous_products = []
        current_product = 1
        for i in self.input_array:
            previous_products.append(current_product)
            current_product *= i

        following_products = []
        current_product = 1
        for i in reversed(self.input_array):
            following_products.append(current_product)
            current_product *= i

        products = []

        l = len(self.input_array)
        for i in range(l):
            products.append(previous_products[i] * following_products[l - i - 1])

        return products