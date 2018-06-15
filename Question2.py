class Element:
    ID = 0
    Value = 0
    Row = 0
    Column = 0 

    def __init__(self,id, value, row, column):
        self.ID = id
        self.Value = value
        self.Row = row
        self.Column = column

    @classmethod
    def Empty(self):
        self.Value=0
        self.Row=0
        self.Column=0
        self.ID=0

ListElements = []

#Read File then each value was added into List as an object from Element Class.
def ReadFile():
    fileRow = 0
    fileColumn = 0
    id=0
    pyramid = open("pyramid.txt", "r")

    numbers = pyramid.split()

    for number in numbers:
        print(number)    

    for line in f:    
        print(line)
        for value in line:
      
            if(value!=' ' and value != '\n'):                         
                element = Element(id,value,fileRow,fileColumn)
                fileColumn +=1
                id+=1
                ListElements.append(element)
        fileColumn = 0
        fileRow += 1

def split_line(text):

    # split the text
    words = text.split()

    # for each word in the line:
    for word in words:

        # print the word
        print(word)
# Find Next Element
def FindNextElement(element):
    return  ListElements[ListElements.index(element) + 1]


#Each number are checked whether prime number.
def isPrimeNumber(value):
    isPrime = True

    if(value == '1'):
        return False
    if(value == '2'):
        return True

    for number in range(2, int(value)):
       if int(value) % number == 0:
           isPrime = False


    if(isPrime == True):
        return True
    else:
        return False

#Numbers are summed.
def SumTriangle():

    beforeElement = Element.Empty()
    continueElement = Element.Empty()
    afterElement = Element.Empty()

    isRowFinished = False
    totalsum = 0

    listLen = len(ListElements)
    for element in ListElements:
        if(element.ID >= listLen-1):
            return totalsum

       

        afterElement = FindNextElement(element)
        if(element.Row == afterElement.Row and isRowFinished ==False):
            if((element.Column == beforeElement.Column or element.Column == beforeElement.Column + 1)):
                number1 = element.Value
                number2 = afterElement.Value

                if((number1>number2 and isPrimeNumber(number1) == False) or (isPrimeNumber(number2) == True and isPrimeNumber(number1) == False )):
                    totalsum += int(number1)
                    isRowFinished = True     
                    beforeElement  = element
                elif((number2>=number1 and isPrimeNumber(number2) == False) or (isPrimeNumber(number1) == True and isPrimeNumber(number2)==False) ):
                    totalsum += int(number2)
                    isRowFinished = True   
                    beforeElement  = afterElement
                else:
                    return totalsum     
             
        elif(element.Row == 0 and element.Column == 0):
            totalsum += int(element.Value)
            beforeElement = element
        elif(afterElement.Row > element.Row) :
            isRowFinished=False           
        
       
    return totalsum




if __name__ == "__main__":
    
   

    ReadFile()
    TotalSum = int(SumTriangle())
    print("Sum of Triangle: " + str(TotalSum))





