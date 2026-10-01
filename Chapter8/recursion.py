'''
factorial(n)=n*(n-1)...2*1
'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n *factorial(n-1)

n=int(input("enter number" ))
print(f"factorial of no {factorial(n)}")