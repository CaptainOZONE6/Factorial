#finds the factorial of a number
def fact():

    n = int(input("Enter a non-negative number: "))
    if n<0:
        print("Baka, NON NEGATIVE INTEGER")
        fact()
    else:
        f = n+1
        for i in range(0,n):
            f=f*(n-i)
        f=f/(n+1)
        print(f"Factorial of {n} is {f}")

fact()

