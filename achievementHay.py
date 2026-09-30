def hay(x,y):
	if can_harvest():
		harvest()
	else:
		plant(Entities.Grass)