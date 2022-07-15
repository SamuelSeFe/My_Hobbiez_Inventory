class Hobby:
    
    def __init__(self, _name, _description, _time_taken, _cost_of_hobby, _energy_expenditure, _reminder, _completed = False, _id = None):
        self.name = _name
        self.description = _description
        self.time_taken = _time_taken
        self.cost_of_hobby = _cost_of_hobby
        self.energy_expenditure = _energy_expenditure
        self.reminder = _reminder
        self.completed = _completed
        self.id = _id