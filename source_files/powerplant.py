class PowerPlant():
    print("produces energy")


class NonRenewable(PowerPlant):

    print("produces a lot of pollution")

class Renewable(PowerPlant):

    print("Less pollution but much more maintenance cost")

# NONRENEWABLES
class CoalPlant(NonRenewable):

    print("Works on coal")

class NaturalGasPlant(NonRenewable):

    print("works on natural gas")

class NuclearPlant(NonRenewable):

    print("works on Urenium")

# RENEWABLES
class SolarPlant(Renewable):

    print("works on solar energy")

class WindPlant(Renewable):

    print("works on wind energy")

class HydroElectricPlant(Renewable):

    print("works on water")

class GeoThermalPlant(Renewable):

    print("works on internal energy of earth")
