import math as ms

def calculations():
    num=int(input("Enter a number : "))
    print(f"The square root of {num} is {ms.sqrt(num)}")
    print(f"The natural logarithm of {num} is {ms.log(num)}")
    print(f"The sine of {num} is {ms.sin(num)}")

if __name__ == "__main__":
    calculations()