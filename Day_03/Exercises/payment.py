class Payment:
    def __init__(self, amount):
        self.amount = amount
    def valid(self):
        return self.amount > 0

class Coupon(Payment):
    def __init__(self, amount, expired):
        super().__init__(amount)
        self.expired = expired
    def valid(self):
        return super().valid() and not self.expired

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = str(card_number)
    def valid(self):
        return len(self.card_number) == 16 and super().valid()

class Online(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = str(email)
    def valid(self):
        # return super().valid() and self.email[-10:] == "@gmail.com"
        return super().valid() and self.email.endswith("@gmail.com")



