import math


if __name__ == "__main__":
	exit()


class Turtle:
	def __init__(self, x = 0, y = 0, angel = 0):
		self.x = x
		self.y = y
		self.angel = angel
		self.angel_degree = angel
		self.angel_radian = angel * (math.pi/180)
		self.coords = []
		self.coords.append([x, y])
		self.coords.append([x, y])
		self.distance = 20
		self.stack = []

	def set_angel(self, angel):
		self.angel = angel	
		self.angel_degree = angel

	def left(self):
		self.angel -= self.angel_degree
	
	def right(self):
		self.angel += self.angel_degree
	
	def direct(self, distance=None):
		if distance != None:
			self.distance = distance
		self.angel_radian = self.angel * (math.pi/180)
		old_x = self.x; old_y = self.y
		self.x = self.distance * math.cos(self.angel_radian) + old_x
		self.y = self.distance * math.sin(self.angel_radian) + old_y
		self.coords.append([self.x, self.y])
	
	def set_distance(self, distance: int):
		self.distance = distance
	
	def get_coords(self):
		return self.coords
	
	def add_stack(self):
		self.stack.append((self.x, self.y))
	
	def pop_stack(self):
		self.x, self.y = self.stack.pop()
		self.coords.append([self.x, self.y])
