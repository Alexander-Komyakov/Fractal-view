import math


if __name__ == "__main__":
	exit()


class Turtle:
	def __init__(self, x = 0, y = 0, angel = 0):
		self.x = x
		self.y = y
		self.angel = angel
		self.coords = []
		self.coords.append([x, y])
		self.coords.append([x, y])
	
	def left(self, degree=-45):
		self.angel += degree * (math.pi/180)
	
	def right(self, degree=45):
		self.angel += degree * (math.pi/180)
	
	def direct(self, distance=2):
		old_x = self.x; old_y = self.y
		self.x = distance * math.cos(self.angel) + old_x
		self.y = distance * math.sin(self.angel) + old_y
		self.coords.append([self.x, self.y])
	
	def get_coords(self):
		return self.coords
