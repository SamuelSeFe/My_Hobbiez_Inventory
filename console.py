import pdb
from models.hobby import Hobby
from models.location import Location

import repositories.hobby_repository as hobby_repository
import repositories.location_repository as location_repository

location1 = Location("home", "inside", 0, "The best location! Suitable for all weathers. Recommended during winter")
location_repository.save(location1)

hobby1 = Hobby("Napping", location1, 30, 0, 25, "Best Hobby EVER!")
hobby_repository.save(hobby1)
hobby2 = Hobby("Listening to music", location1, 30, 0, 10, "Great for relaxing or using alongside other hobbies")
hobby_repository.save(hobby2)







pdb.set_trace()