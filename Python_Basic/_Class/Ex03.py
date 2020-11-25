class Unit:
    def __init__(self):
        print("unit constructor")

class Airborne:
    def __init__(self):
        print("airborne constructor")

class AirborneUnit(Airborne, Unit):
    def __init__(self):
        super().__init__() 
        # super().__init__() can be used to initialize
        # the parent class constructor
        # however, when multiple inherited, only
        # calls the constructor of the first inherited
        # in this case, Airborne
        # thus to initialize both, you should call their
        # constructors instead of using super().__init__()

dropship = AirborneUnit()