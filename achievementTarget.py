import achievementFarm
import achievementWood
import achievementHay
import achievementCarrots
import achievementPumpkin
import achievementSunflower



def whatToFarm(resource, columns_per_drone, drone_x):
	if resource == Entities.Bush or resource == Entities.Tree:
		return achievementFarm.farm(columns_per_drone, drone_x, achievementWood.wood)
	if resource == Entities.Grass:
		return achievementFarm.farm(columns_per_drone, drone_x, achievementHay.hay)
	if resource == Entities.Carrot:
		return achievementFarm.farm(columns_per_drone, drone_x, achievementCarrots.carrot)
	if resource == Entities.Cactus:
		return
	if resource == Entities.Pumpkin:
		return achievementFarm.farm(columns_per_drone, drone_x, achievementPumpkin.pumpkin)
	if resource == Entities.Treasure:
		return
	if resource == Entities.Sunflower:
		return achievementFarm.farm(columns_per_drone, drone_x, achievementSunflower.sunflower)