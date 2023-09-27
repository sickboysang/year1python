#Sangeethan Thevathasan 100867103
class information():
    def __init__(self,name="",age=0,address="",phone=0):
        self.__name=name
        self.__age=age
        self.__address=address
        self.__phone=phone
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def getaddress(self):
        return self.__address
    def getphone(self):
        return self.__phone
    def setname(self,name):
        self.__name=name
    def setage(self,age):
        self.__age=age
    def setaddress(self,adress):
        self.__adress=adress
    def setphone(self,phone):
        self.__phone=phone
    def __str__(self):
        return 'Name : {} - age: {} - address: {} '.format(self.__name,self.__age,self.__address,self.__phone)
def display_info(data):
    name = data.getname()
    age = data.getage()
    address = data.getaddress()
    phone = data.getphone()
    print( 'Name: {}\nAge: {}\nAddress: {}\nPhone:{}'.format(name,age,address,phone))

if __name__== '__main__':
    data = information('sarah jones', 21,'2000 Simcoe North', '+1 9123405999')
    print(data)
    display_info(data)