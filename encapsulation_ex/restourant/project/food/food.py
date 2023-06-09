from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        self.__grams = grams
        super().__init__(name, price)

    @property
    def grams(self):
        return self.__grams
    


