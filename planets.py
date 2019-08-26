
# nstructions
# Use append() to add Jupiter and Saturn at the end of the list.
# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# Use insert() to add Earth, and Venus in the correct order.
# Use append() again to add Pluto to the end of the list.
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.


planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Earth", "Uranus"])
planet_list.insert(6, "Venus")
planet_list.insert(7, "Pluto")
planet_list.append("Neptune")
del planet_list[7]
print(planet_list)

rocky_list = planet_list[0:4]
print(rocky_list)


