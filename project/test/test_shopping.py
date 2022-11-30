from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCar(TestCase):

    def setUp(self):
        self.shop_1 = ShoppingCart("Fantastiko", 2000.00)
        self.shop_2 = ShoppingCart("Kaufland", 4000.00)

    def test_initializing(self):
        self.assertEqual("Fantastiko", self.shop_1.shop_name)
        self.assertEqual(2000, self.shop_1.budget)
        self.assertEqual({}, self.shop_1.products)

    def test_if_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop_1.shop_name = "fantastiko"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_if_add_to_cart_func_with_wrong_input(self):
        with self.assertRaises(ValueError) as ve:
            self.shop_1.add_to_cart("sirene", 100.50)

        self.assertEqual("Product sirene cost too much!", str(ve.exception))

    def test_if_add_to_cart_func_adds_to_the_cart_and_returns_correct_info(self):
        return_result = self.shop_1.add_to_cart("sirene", 99.00)
        expected_return_result = "sirene product was successfully added to the cart!"

        expected_result_in_dict = {"sirene": 99.00}
        actual_result_in_dict = self.shop_1.products

        self.assertEqual(expected_result_in_dict, actual_result_in_dict)
        self.assertEqual(expected_return_result, return_result)

    def test_if_remove_from_dict_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop_1.remove_from_cart("sirene")

        self.assertEqual("No product with name sirene in the cart!", str(ve.exception))

    def test_if_remove_func_removes_from_the_dict_and_returns_correct_value(self):
        self.shop_1.add_to_cart("sirene", 99)
        return_result = self.shop_1.remove_from_cart("sirene")
        expected_return_result = "Product sirene was successfully removed from the cart!"

        expected_result_in_dict = {}
        actual_result_in_dict = self.shop_1.products

        self.assertEqual(expected_result_in_dict, actual_result_in_dict)
        self.assertEqual(expected_return_result, return_result)

    def test_if_add_func_adds_two_instances_correctly(self):
        self.shop_1.products = {"sirene": 50.00}
        self.shop_2.products = {"banica": 40.00}
        new_shop = self.shop_1 + self.shop_2

        expected_name = "FantastikoKaufland"
        actual_name = new_shop.shop_name

        expected_budget = 6000.00
        actual_budget = new_shop.budget

        expected_products = {"sirene": 50.00, "banica": 40.00}
        actual_products = new_shop.products

        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_budget, actual_budget)
        self.assertEqual(expected_products, actual_products)

    def test_buy_products_with_correct_values(self):
        self.shop_1.products = {"sirene": 50.00, "banica": 40.00}

        expected_result = "Products were successfully bought! Total cost: 90.00lv."
        actual_result = self.shop_1.buy_products()

        self.assertEqual(expected_result, actual_result)

    def test_buy_products_with_wrong_values(self):
        self.shop_1.products = {"sirene": 5000.00, "banica": 4000.00}

        with self.assertRaises(ValueError) as ve:
            self.shop_1.buy_products()

        expected_result = "Not enough money to buy the products! Over budget with 7000.00lv!"
        actual_result = str(ve.exception)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
