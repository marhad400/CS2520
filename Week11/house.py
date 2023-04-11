def main():
	x, y = 100, 100
	width, height = 100, 400

	draw_house(x, y, width, height)

def draw_house(x, y, width, height):
	"""
	function draws house with width and height from the reference point

	param x: x coorindate of the midpoint of the foundation
	param y: y coordinate of the bottom side of the foundation
	param width: total width of the house
	param height: total heght of the house
	
	"""
	print("Drawing house", x, y, width, height)

	foundation_height = 0.05 * height
	walls_width = 0.9 * width
	walls_height = 0.5 * height
	roof_height = height - foundation_height- walls_height

	draw_house_foundation(x, y, width, foundation_height)
	draw_house_walls(x, y - foundation_height, walls_width, walls_height)
	draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)

def draw_house_foundation(x, y, width, height):
	"""
	function draws house with width and height from the reference point

	param x: x coorindate of the midpoint of the foundation
	param y: y coordinate of the bottom side of the foundation
	param width: total width of the foundation
	param height: total heght of the foundation
	
	"""
	print("Drawing foundation", x, y, width, height)

	pass

def draw_house_walls(x, y, width, height):
	"""
	function draws house with width and height from the reference point

	param x: x coorindate of the midpoint of the foundation
	param y: y coordinate of the bottom side of the foundation
	param width: total width of the walls
	param height: total heght of the walls
	
	"""
	print("Drawing walls", x, y, width, height)

	pass

def draw_house_roof(x, y, width, height):
	"""
	function draws house with width and height from the reference point

	param x: x coorindate of the midpoint of the foundation
	param y: y coordinate of the bottom side of the foundation
	param width: total width of the roof
	param height: total heght of the roof
	
	"""
	print("Drawing roof", x, y, width, height)

	pass

main()