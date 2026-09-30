import achievementMovement
import achievementWood
import achievementHay
import achievementTarget

def drone_task():
	achievementTarget.whatToFarm(resource, columns_per_drone, get_pos_x())

clear()
drones_spawned = 0
available_drones = 32
world_size = 32
set_world_size(world_size)
achievementMovement.move_to(0,0)
resource = Entities.Sunflower

columns_per_drone = world_size / available_drones
while True:
	if available_drones - 2 < drones_spawned:
		while True:
			drone_task()
	elif (get_pos_x() % columns_per_drone) == 0:
		if spawn_drone(drone_task):
			for i in range(columns_per_drone):
				move(East)
		drones_spawned += 1
	else:
		move(East)