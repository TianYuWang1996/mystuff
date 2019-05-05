class Scene(object):
	
	def enter(self):
		pass


class Engine(object):
	
	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass

class Death(Scene):
	pass

class Central_Corridor(Scene):
	pass

class Laser_Weapon_Armory(Scene):
	pass

class The_Bridge(Scene):
	pass

class Escape_Pod(Scene):
	pass

class Map(object):
	
	def __init__(self, start_scene):
		pass
	
	def next_scence(self, scene_name):
		pass
	
	def opening_scence(self):
		pass


# 测试模块
a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()