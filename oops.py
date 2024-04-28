class CRUD:
	def __init__(self):
		self.Name=None
		self.number=None
		self.email=None
		self.password=None
	def create(self):
		self.name=input("enter the name:")
		self.number=int(input("enter your number: "))
		slef.email=self.name+"@email.com"
		print("your new email is ",self.email)
		slef.password=input("enter your password:")
	def read(self):
		if self.name==None:
			print("please enter an account first")
			self.create()
		else:
			print("name:",self.name)
			print("number:",self.number)
			print("email:",self.self.email)
			print("password:",self.password)
object=CRUD()
while True:
	inp=int(input("enter your choise:"))
	if inp==0:
		object.create()
	elif inp==1:
		object.read()
	
