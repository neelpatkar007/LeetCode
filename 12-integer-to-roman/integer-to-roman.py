class Solution(object):
    def intToRoman(self, num):
        valueslist = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        
        result = ""
        
        for symbol, value in reversed(valueslist):
            if num // value:
                count = num // value
                result += (symbol * count)
                num = num % value
        return result