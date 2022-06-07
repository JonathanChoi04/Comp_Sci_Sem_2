people_list = ["Mom", "Dad", "Brother", "Kanye West", "Sister"]
comp_list = ["is cool", "is chill", "is beautiful", "is amazing", "is smart"]

import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])