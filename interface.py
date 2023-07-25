from library import *

library1 = Library("Radcliffe Camera", "Oxford")
user1 = User("Hayden Ramm", 21, 1000)

library1.addUser(user1)

ID_searched = 1001
found_user = library1.find_user(ID_searched)

if found_user:
    print(f"User with ID {found_user.getId()}: {found_user.getName()}")
else:
    print(f"User with ID {ID_searched} not found.")