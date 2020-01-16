import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, purchaser_name):
        self.owner = purchaser_name

building_1 = Building("202 Plus Park Blvd", 10)
building_2 = Building("205 Plus Park Blvd", 2)
building_3 = Building("3500 Shadow Lane", 2)
building_4 = Building("1200 Shadow Lane", 1)
building_5 = Building("382 Laiken Drive", 2)

building_1.purchase("Ken")
building_2.purchase("Ryan")
building_3.purchase("John")
building_4.purchase("Trey")
building_5.purchase("Jeremiah")

building_1.construct()
building_2.construct()
building_3.construct()
building_4.construct()
building_5.construct()

buildings = [building_1, building_2, building_3, building_4, building_5]

for building in buildings:
    print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories')
