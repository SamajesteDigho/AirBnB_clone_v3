#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.city import City

# data = {
#     "Alabama": ['Akron', 'Douglas', 'San Francisco'],
#     "Arizona": ['Denver', 'Miami', 'Honolulu'],
#     "Colorado": ['Chicago', 'New Orleans', 'Saint Paul'],
#     "Florida": ['Jackson', 'Portland', 'Babbie'],
#     "Georgia": ['Kearny', 'San Jose', 'Orlando'],
#     "Hawaii": ['Kailua', 'Peoria', 'Baton rouge'],
#     "Illinois": ['Tupelo', 'Eugene', 'Calera'],
#     "Indiana": ['Tempe', 'Fremont', 'Pearl city'],
#     "Loiusiana": ['Naperville', 'Lafayette', 'Meridian'],
#     "Mennesota": ['Fairfield', 'Napa', 'Urbana'],
#     "Mississippi": ['Sonoma'],
#     "Oregon": ['Joliet'],
# }

# for st, cts in data.items():
#     state = State(name=st)
#     state.save()
#     for ct in cts:
#         city = City(name=ct, state_id=state.id)
#         city.save()

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
