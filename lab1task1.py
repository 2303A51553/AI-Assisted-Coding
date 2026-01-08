#write a program to check given number is prime or not without user defined function directly in main code
num = int(input("Enter a number: "))
is_prime = True

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number") 


# optimise theabove code for better performance

num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")    
else:       
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")     

        

                                                                 