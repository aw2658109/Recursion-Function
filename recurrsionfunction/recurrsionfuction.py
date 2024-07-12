# Recursion Function:
def show(n):
    if(n==0): #Base case:
        return
    print(n)
    show(n-1)

show(5)

#second example:
print("new example Recursion functions:")
def display(x):
    if(x==2):
        return
    print(x)
    display(x-1)

display(10)

#Q1: write to find factorial using recursion functions:

def fact(y):
    if(y==0 or y==1):
        return 1
    return y*fact(y-1)
print("factorial is:",fact(5))

#Q2: write a recursive function to calculate sum of first natural number:

def cal_sum(z):
    if(z==0):
        return 0

    return cal_sum(z-1)+z

sum=cal_sum(100)
print("Sum of natural number is:",sum)

#Q3: write a recursive function to print all element in list.(hint: use list and index as paramter)

def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)
value=[12,43,4.4]
print_list(value )


#Q2: wri

