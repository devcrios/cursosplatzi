from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, typecarAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted    = typecarAccepted
        self.seatsMaterial      = seatsMaterial