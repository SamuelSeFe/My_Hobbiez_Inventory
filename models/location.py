class Location:

    def __init__(self, _name, _description, _distance_to_location, _reminder, _id = None):
        self.name = _name
        self.description = _description
        self.distance_to_location = _distance_to_location
        self.reminder = _reminder
        self.id = _id