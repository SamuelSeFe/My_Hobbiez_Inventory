class Hobby:
    
    def __init__(self, _name, _location, _duration, _cost, _energy_expenditure, _reminder, _completed = False, _id = None):
        self.name = _name
        self.location = _location
        self.duration = _duration
        self.cost = _cost
        self.energy_expenditure = _energy_expenditure
        self.reminder = _reminder
        self.completed = _completed
        self.id = _id