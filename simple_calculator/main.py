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
        count = 0
        total = 0

        for number in A:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count
    
        ##################  
        ## Implementation option 2: works well with list but not for generators where the len funciton is not available
        ##################
        #if len(A) == 0:
        #    return 0
        #else: 
        #    A_sorted = sorted(A)
        #    idlt = 0
        #    idut = len(A_sorted)

        #    if ut is not None:
        #        idut = bisect.bisect(A_sorted, ut)
        #    if lt is not None:
        #        idlt = bisect.bisect(A_sorted, lt)
        #        if A_sorted[idlt-1] == lt:
        #            idlt = idlt - 1
        #     
        #    if len(A_sorted[idlt:idut]) == 0:
        #        return 0
        #    else:  
        #        return sum(A_sorted[idlt:idut]) / len(A_sorted[idlt:idut])

        ##################  
        ## Implementation option 3: works well with list but not for generators where the len funciton is not available
        ##################
        #_it = it[:]

        #if lt is not None:
        #    _it = [x for x in _it if x >= lt]

        #if ut is not None:
        #    _it = [x for x in _it if x <= ut]

        #if not len(_it):
        #    return 0

        #return sum(_it)/len(_it)        