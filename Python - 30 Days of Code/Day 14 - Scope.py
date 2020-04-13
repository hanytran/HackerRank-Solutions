class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        self.maximumDifference = abs(sorted(self.__elements)[0]-sorted(self.__elements)[-1])
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)