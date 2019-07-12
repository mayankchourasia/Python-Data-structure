class Customer(object):
	custo=0
	customer_list=[]
	def __init__(self,day,name):
		self.day=day
		self.name=name
		Customer.custo+=1
		
	@staticmethod
	def addcustomer():
		day=raw_input("Enter the Day")
		name=raw_input("Enter the name Of Custome")
		Customer.customer_list.append(Customer(day,name)
