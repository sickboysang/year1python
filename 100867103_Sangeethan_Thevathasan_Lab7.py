#sangeethan Thevathasan 100867103 # Lab7
class BasicCalculator():  
     
    def add(self,x,y):
        sum = x + y
        return (sum)
    
    def multi(self,x,y):
        sum = x*y
        return(sum)
    
    def divd(self,x,y):
        sum = x/y
        return(sum)
    
    def sub(self,x,y):
        sum = int(x-y)
        return(sum)

class AdvancedCalculator(BasicCalculator):
    def add(self,x,y):
        try:
            result=""
            result+=(str(x)+"+"+str(y)+"=")
            sum=super().add(x,y)
            result+=str(sum)
            print(result)
        except:
            print("ERROR")
            
    def multi(self, x, y):
        try:
            result=""
            result+=(str(x)+"*"+str(y)+"=")
            sum = super().multi(x,y)
            result+=str(sum)
            print(result)
        except:
            print("ERROR")
            
    def sub(self,x,y):
        try:
            result=""
            result+=(str(x)+"-"+str(y)+"=")
            sum=super().sub(x,y)
            result+=str(sum)
            print(result)
        except:
            print("ERROR")            
    def divd(self,x,y):
        try:
            result=""
            result+=(str(x)+"/"+str(y)+"=")
            sum=super().divd(x,y)
            result+=str(sum)
            print(result)
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except:
            print("ERROR")

def main():       
    calc=AdvancedCalculator()
    cond=True
    while cond==True:
        try:
            ARI=input("Enter operation: ")
            print("---------------")
            x=float(input("What is your first number: "))
            print("---------------")
            y=float(input("What is your second number: "))
            print("---------------")
            if ARI=="+":
                calc.add(x,y)
            elif ARI=="addition":
                calc.add(x,y)
            if ARI=="*":
                calc.multi(x,y)
            elif ARI=="multiplication":
                calc.multi(x,y)
            if ARI=="-":
                calc.sub(x,y)
            elif ARI=="subtraction":
                calc.sub(x,y)
            if ARI=="/":
                calc.divd(x,y)
            elif ARI=="division":
                calc.divd(x,y)
            if ARI=="stop":
                break
        except:
            print("ERROR")
main()
