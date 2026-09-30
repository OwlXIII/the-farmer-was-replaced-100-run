def wood(x,y):
	if get_entity_type() == Entities.Grass:
		plantWood(x,y)
	if can_harvest():
		harvest()
		plantWood(x,y)
		
def plantWood(x,y):
	if (x + y) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)