import achievementMovement
import achievementUtilities

def pumpkin(x,y):
	if achievementUtilities.checkGroundType(Grounds.Grassland):
		till()
	if not achievementUtilities.checkEntityType(Entities.Pumpkin):
		plant(Entities.Pumpkin)
		return
	if x == 0 and y == 0 and can_harvest():
		tryHarvestGiant()

def tryHarvestGiant():
	last = get_world_size() - 1
	first_id = measure()
	achievementMovement.move_to(last, last)
	if achievementUtilities.checkEntityType(Entities.Pumpkin) and can_harvest() and measure() == first_id:
		harvest()
	achievementMovement.move_to(0, 0)