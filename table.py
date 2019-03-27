from elements import elements
import elements.elements as elements

class Table:
    def __init__(self):
        return
    @staticmethod
    def roun(num):
        if '(' in num:
            i1 = num.index('(')
            i2 = num.index(')')
            number = num[i1+1:i2]
            return float(number)
        num = [i for i in num]
        del num[len(num)-4:len(num)]
        num = ''.join(num)
        num = float(num)
        return num
    def get_table(self):
        data = elements.Elements
        data = sorted(data,key=lambda i:i.AtomicNumber)
        elems = {}
        for i in range(0,len(data)):
            elems[data[i].Symbol] = Table.roun(data[i].AtomicMass)
        return elems
