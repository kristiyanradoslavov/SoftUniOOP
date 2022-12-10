from OOP.exam.class_project.project_christmass_pastry_shop.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    def __init__(self, booth_number, capacity):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people):
        reservation_price = PrivateBooth.PRICE_PER_PERSON * number_of_people

        self.price_for_reservation = reservation_price
        self.is_reserved = True
