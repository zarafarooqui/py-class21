def sum(n):
    return n*(n+1)/2
print(sum(4))
#space complewxity =0(1)
#space will remasin constant

def arraysum(a):
    sum = 0
    for i in a :
        sum += i
    return sum
a=[12,3,4,15]
result= arraysum(a)
print(result) #this wiil output:34

#space complexity= 0(n)
#auxillary space will increase due to array data structure