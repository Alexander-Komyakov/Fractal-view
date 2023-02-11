if __name__ == "__main__":
	exit()


class Fractal:
	def __init__(self):
		self.symbol = dict()
		self.expression = ""
		self.rules = dict()
	
	#example rule = "F++F++F+F-F--F"
	def add_rule(self, name_rule: str, rule: str):
		self.rules[name_rule] = rule
		if self.expression == "":
			self.expression = rule

	def add_symbol(self, symbol, func):
		self.symbol[symbol] = func
	
	def call_rule(self):
		for i in self.expression:
			self.symbol[i]()
	
	def del_rule(self, name_rule):
		del self.rules[name_rule]

	def del_symbol(self, symbol):
		del self.symbol[symbol]
	
	def smash_expression(self):
		new_expression = ""
		for i in self.expression:
			if i in self.rules.keys():
				new_expression += self.rules[i]
			else:
				new_expression += i
		self.expression = new_expression
