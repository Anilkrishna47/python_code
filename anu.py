'''n=5
for i in range(1,n+1):

    for j in range(1,i+1):
        print("*",end=' ')
    print()
for i in range(n,1,-1):
    for j in range(i,1,-1):
        print("*",end=' ')
    print()
def largestNumber(* numbers):

    largestNumber(1,2,3,4)
largestNumber(8,9,3,4,2,5)
class Car():
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def get_speed(self):
        print("Top speed of " + self.name + " is 150")

Honda_city=Car("Honda city","Red")

Honda_city.get_speed()
print(Honda_city.color)

Honda_civic=Car("Honda civic","White")
Honda_civic.get_speed()
class Car:
    def setenginemodel(self,engine):
        self.engine = engine
    def getenginemodel(self):
        print(self.engine)
class Honda(Car):
    def setcarmodel(self,model):
        self.model = model
    def getcarmodel(self):
        print(self.model)
mycar = Honda()
mycar.setenginemodel('Ek-1')
mycar.setcarmodel('V6')
print('Car Details:')
mycar.getenginemodel()
mycar.getcarmodel()'''



'''fr=open('sample.txt','r')

print(fr.read())
fr.seek(0)
fw=open('sample2.txt','w')
fw.write(fr.read())
fr.close()
fw.close()
print(fr.read(1))
print(fr.tell())'''
class Anil():
    def setDetails(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def getDetails(self):
        print(self.name,self.age,self.mark)
mycar=Anil()
mycar.setDetails('Anull',12,10000000)
mycar.getDetails()
        























