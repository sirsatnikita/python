class Rectangle:
	def __init__(self,length,width):
	
		self.length=length
		
		self.width=width
		
	def calculate_area(self):
	
		return self.length*self.width
		
	def calculate_parimeter(self):
	
		return 2*(self.length + self.width)
		
my_Rectangle= Rectangle(5,10)

print("Area of rectrangle:",My_Rectangle.calculate_area())

print("parimeter of rectrangle:",my_rectangle.calculate_parimeter())	
	
