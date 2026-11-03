n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")

else:
    Prime = True

    for i in range(2, n):
        if n % i == 0:
            Prime = False
            break

    if Prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

