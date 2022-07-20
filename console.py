import pdb

from models.hobby import Hobby
from models.location import Location

import repositories.hobby_repository as hobby_repository
import repositories.location_repository as location_repository
import repositories.user_repository as user_repository

location_repository.delete_all()
hobby_repository.delete_all()
user_repository.delete_all()

location1 = Location("Home", "inside", 0, "The best location! Suitable for all weathers. Recommended especially during winter")
location_repository.save(location1)
location2 = Location("Meadows", "outside", 10, "Great location! Suitabale year round (except for winter, please don't go outside in the winter)")
location_repository.save(location2)
location3 = Location("Holyrood Park", "outside", 15, "Less busy than the meadows and with more space")
location_repository.save(location3)
location4 = Location("Omni Centre", "insde", 20, "Better to go with friends")
location_repository.save(location4)

hobby1 = Hobby("Napping", location1, 30, 0, -20, "Best Hobby EVER!")
hobby_repository.save(hobby1)
hobby2 = Hobby("Listening to music", location2, 30, 0, -5, "For relaxing or to enjoy alongside other hobbies!")
hobby_repository.save(hobby2)
hobby3 = Hobby("Painting", location1, 60, 0, 10, "Good for the mind")
hobby_repository.save(hobby3)
hobby4 = Hobby("Watch a film", location4, 150, 10, 15, "Once every week or two")
hobby_repository.save(hobby4)
hobby5 = Hobby("Go for a run", location3, 45, 0, 40, "Good for the body")
hobby_repository.save(hobby5)



pdb.set_trace()