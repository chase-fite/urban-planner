from building import Building
from city import City

megalopolis = City()

# Awesome code here
Saloon = Building("10 Plus Park Blvd", 5)
Stable = Building("28 Plus Park Blvd", 2)

megalopolis.add_building(Saloon)
megalopolis.add_building(Stable)

for building in megalopolis.buildings:
    print(building.__dict__)