class Hobby:
    
    def __init__(self, _name, _activity_area, _duration, _cost, _energy_expenditure, _reminder, _completed = False, _id = None):
        self.name = _name
        self.activity_area = _activity_area
        self.duration = _duration
        self.cost = _cost
        self.energy_expenditure = _energy_expenditure
        self.reminder = _reminder
        self.completed = _completed
        self.id = _id