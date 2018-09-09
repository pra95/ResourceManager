class NonRenewable():


    def info(self):
        print("They can get depleted")
class Coal(NonRenewable):

    amount_left = 1000
    def info(self):
        print("It is back in color")

class NaturalGas(NonRenewable):

    amount_left = 500
    def info(self):
        print("Its a liquid")

