class Customer(object):
    cust=0
    cust_list=[]
    def __init__(self,day,name,cid):
            self.day=day
            self.name=name
            self.cid=cid
            Customer.cust+=1
    """
    def __str__(self):
            return "Name:"+"\t"  +self.name+"\t"+"Day"  +   self.day
    """
    @staticmethod
    def addCustomer():
        day=raw_input("Enter the Day")
        name=raw_input("Enter the name")
        cid=input("Enter the Customer ID")
        Customer.cust_list.append(Customer(day,name,cid))
        print ("Customer Added Succesfully")
        
        
    @staticmethod
    def display():
        print "Name of Customer"+"\t"+"Day"+"\t"+"Customer Id"
        for i in Customer.cust_list:
            print "\t",i.name,"\t""\t",i.day,"\t",i.cid
    
    @staticmethod
    def particularDay():
            choice=raw_input("Enter the day")
            print "Showing All the Customer list of "+choice

            for k in Customer.cust_list:
                    if choice==k.day:
                    
                        print (k.name)
                    else :
                        print "Not Found"
    @staticmethod
    def search():
        
        arr=[]
        arr=Customer.cust_list
        n=Customer.cust
        x=input("enter the id to be search")
        def binary_search(arr, 0, n, x):
                if (low<=high): # we can break the array further
                    # the middle element
                    middle = (low+high)//2

                    # the element to be found is at the middle
                    if (arr[middle] == x):
                        return middle

                    '''
                    element to be found is greater than the element
                    at the middle.
                    The element to be found should be in the right side
                    '''
                    if (ar[middle]>x):
                        return binary_search(ar, low, middle-1, x)

                    '''
                    the element is neither at the midddle nor int the
                    right side of middle, so it should be in the left
                    side
                    '''
                    return binary_search(ar, middle+1, high, x)
                #element is not found in the array
                return -1

"""if __name__ == "__main__":
  #sorted array
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  found_index = binary_search(a, 0, 9, 2)
  print("Found at index:",found_index)
"""


def main():
    while True :
        print "*"*50
        print "WELCOME TO RESTAURANT" 
        print "*"*50
        print "1.Add Customer"
        print "2.Display Customer"
        print "3.Delete Customer"
        print "4.visited Customers"
        print "5.show customer visited @ particular day"
        print "6.Search into the Database by"
        print "*"*50
        print "*"*50
        choice=input("Enter the Choice ")
        if choice==1:
                    Customer.addCustomer()
        elif choice==2:
                    Customer.display()
        elif choice==3:
                    print "Delete the Numer"
        elif choice==4:
                    print (Customer.cust)
        elif choice==5:
                Customer.particularDay()

        elif choice==6:  
                Customer.search()      
        else:
                    print("Enter the Correct Choice Code")
                

if __name__=="__main__":
    main()