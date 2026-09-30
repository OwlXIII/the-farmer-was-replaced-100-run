import achievementMovement
import achievementUtilities

def sunflower(x, y):
	if achievementUtilities.checkGroundType(Grounds.Grassland):
		till()
	if can_harvest():
		harvest()
	if not achievementUtilities.checkEntityType(Entities.Sunflower):
		plant(Entities.Sunflower)

	
	