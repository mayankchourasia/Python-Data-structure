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

def main():
	while True:
		print "-"*50
                print "Welcome to APP"
                print "-"*50
                print "1.Add Customer"
		    choice=input("Enter ur choice") #Choice provided for user to perform various operations using menu
                         if choice==1:
                                Customer.addcustomer()
			else :
				Customer.Display()
					      

if __name__ == '__main__':
        main()


		

		

