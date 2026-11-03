"""num = int(input("Enter a number: "))

for i in range(0, num + 1, 2):
    print(i, end = "\t")

sum = 0
for i in range(1, num + 1):
    sum += i
print(f"\nSum: {sum}")"""

l = [1, 2, 3, 4]

largest = l[0]
second = l[0]

for s in l:
    if s > largest:
        second = largest
        largest = s

    elif s > second and l != largest:
        second = s

print(second)

