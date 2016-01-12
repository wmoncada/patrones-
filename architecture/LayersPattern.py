class PresentationLayer:
	def __init__(self):
		self.name = "PresentationLayer"

	def setLowerLayer(self,lowerLayer):
		self.lowerLayer = lowerLayer

	def s3(self,param):
		print("Entramos al %s" % self.name)
		self.lowerLayer.s2(param)
		print("Terminamos %s" % self.name)

class LogicLayer:
	def __init__(self):
		self.name = "LogicLayer"

	def setLowerLayer(self, lowerLayer):
		self.lowerLayer = lowerLayer

	def s2(self,param):
		print("Entramos al %s" % self.name)
		self.lowerLayer.s1(param)
		print("Terminamos %s" % self.name)

class DataLayer:
	def __init__(self):
		self.name = "DataLayer"

	def setLowerLayer(self, lowerLayer):
		self.lowerLayer = lowerLayer

	def s1(self,param):
		print("Dentro de %s" % self.name)
		print("ejecutamos s1 con %s" % param)
		
if __name__ == "__main__":
	ui  = PresentationLayer()
	logic = LogicLayer()
	data = DataLayer()

	ui.setLowerLayer(logic)
	logic.setLowerLayer(data)

	ui.s3("exampleParam")
