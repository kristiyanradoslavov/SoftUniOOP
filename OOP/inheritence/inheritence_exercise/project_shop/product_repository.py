from OOP.inheritence.inheritence_exercise.project_shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product_name == product.name:
                return product

    def remove(self, product_name):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        result = [i.__dict__ for i in self.products]
        final_result = []
        for i in result:
            final_result.append(f"{i['name']}: {i['quantity']}")

        return "\n".join(final_result)