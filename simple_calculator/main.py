import operator, bisect
from functools import reduce
class SimpleCalculator:

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b
    
    def mul(self, *args):
        if not all(args):
            raise ValueError
        
        return reduce(operator.mul, args)
    
    def div(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return float('inf')
        
    def avg(self, A, lt = None, ut = None):
        if len(A) == 0:
            return 0
        else: 
            A_sorted = sorted(A)
            if not ut:
                ut = max(A_sorted)
            if not lt:
                lt = min(A_sorted)
                      
            idut = bisect.bisect(A_sorted, ut)
            idlt = bisect.bisect(A_sorted, lt)
            if A_sorted[idlt-1] == lt:
                idlt = idlt - 1
             
            if len(A_sorted[idlt:idut]) == 0:
                return 0
            else:  
                return sum(A_sorted[idlt:idut]) / len(A_sorted[idlt:idut])