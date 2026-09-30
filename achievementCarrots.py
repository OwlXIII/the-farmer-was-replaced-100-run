import achievementMovement
import achievementUtilities

def carrot():
	if achievementUtilities.checkGroundType(Grounds.Soil):
		plant(Entities.Carrot)
	else:
		till()
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
	