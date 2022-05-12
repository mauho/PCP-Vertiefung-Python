class Casino:
    def lose_money(self):
        print("next time I win!")


class StockMarked:
    def lose_money(self):
        print("in ten years it will be up again!")


class CryptoMarket:
    def lose_money(self):
        print("nooo i lost all my money :(")


class Internet:
    def lose_money_in_scam(self):
        print("it was too good to be true!")


class TryBecomeRich:
    def __init__(self, methode):
        methode.lose_money()


def main():
    TryBecomeRich(Casino())
    TryBecomeRich(StockMarked())
    TryBecomeRich(CryptoMarket())
    # AttributeError: 'Internet' object has no attribute 'lose_money'
    # BecomeRich(Internet())


if __name__ == '__main__':
    main()
