class City:
    def __init__(self):
        self.name = ""
        self.mayor = ""
        self.year_est = 0
        self.buildings = list()
    
    def add_building(self, building):
        self.buildings.append(building)