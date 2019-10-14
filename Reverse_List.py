#program to reverse a list using reverse() builtin method

def Reverse(l):
    l.reverse()
    return l

print("Enter the number of elements in the list: ")
n=int(input())
l=[]
for i in range(n):
    print("Enter element to append in the list: ")
    j=int(input())
    l.append(j)
print(Reverse(l))
