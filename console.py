import pdb
from models.hobby import Hobby
from models.location import Location

import repositories.hobby_repository as hobby_repository
import repositories.location_repository as location_repository

location_repository.delete_all()
hobby_repository.delete_all()

location1 = Location("home", "inside", 0, "The best location! Suitable for all weathers. Recommended especially during winter")
location_repository.save(location1)
location2 = Location("meadows", "outside", 10, "Great location for outdoor hobbies. Suitabale year round (except for winter, please don't go outside in the winter)")
location_repository.save(location2)

hobby1 = Hobby("Napping", location1, 30, 0, 25, "Best Hobby EVER!")
hobby_repository.save(hobby1)
hobby2 = Hobby("Listening to music", location1, 30, 0, 10, "Great for relaxing or using alongside other hobbies")
hobby_repository.save(hobby2)





pdb.set_trace()