def prints(n):
    if (n<=0):
     return n
    print("codingal")
    prints(n/2)#recursion
    prints(n/2)#recursion
prints(4)
#time complexity=O(nlogn) with base 2