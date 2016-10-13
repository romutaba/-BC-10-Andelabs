class ListComprehension:
    a = 0
    b = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b

   
    def getList(self,a,b):
        alist = []
        #length = len(alist)
        
        for x in range(b ,(a+1)*b)[::b]:
            alist.append(x)
        return alist



class BinarySearch(ListComprehension) :

    #length = a*b

    def __init__(self,a,b):
        #super().__init__(a,b)
        super(BinarySearch,self).__init__(a,b)
        self.length = None
    def search(self,item):
        alist = self.getList(self.a,self.length)
        #b == len(alist)
        first = 0
        last = len(alist)-1
        found = False
        count = 0
        dict_new = {}
        while first <= last and not found:
            midpoint = (first + last)//2  #//
            if alist[midpoint] == item:
                found=True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
            count = count +1
        dict_new["count"] = count
        dict_new["index"] = alist.index(item)
        return dict_new


Binary = BinarySearch(100,10)
print(Binary.search(1000))

#print (Binary.length)

#print(binarySearch(range(0,1000000000),90))