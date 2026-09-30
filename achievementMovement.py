def move_to(x_or_position_tuple, y = None):
	if y == None:
		x = x_or_position_tuple[0]
		y = x_or_position_tuple[1]
	else:
		x = x_or_position_tuple
	
	move_on_axis(x, get_pos_x, East, West)
	move_on_axis(y, get_pos_y, North, South)

def move_on_axis(target, position_function, increase_direction, decrese_direction):
	current_position = position_function()
	increase_steps = (target - current_position) % get_world_size()
	decrease_steps = (current_position - target) % get_world_size()
	
	direction = increase_direction
	if decrease_steps < increase_steps:
		direction = decrese_direction
		
	while position_function() != target:
		move(direction)

def traverseFarm(columns_per_drone, drone_x, action):
	for i in range(drone_x, columns_per_drone + drone_x):
			for j in range(get_world_size()):
				move_to(i, j)
				action(i,j)
	