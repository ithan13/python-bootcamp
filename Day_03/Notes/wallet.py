class Wallet:
    def __init__(self,initial_amount=50):
        self.amount = initial_amount

food_wallet = Wallet(250)
food_wallet.amount += 1_100

print("Food Budget:", food_wallet.amount)
