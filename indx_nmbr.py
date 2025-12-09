#Return the index of a number in a list (or -1 if not found).

numbers=[1,2,3,5,7,9]

target=8
found=False

for i, num in enumerate(numbers):
    if target == num:
        print(i)
        found = True
        break

if not found:
    print(-1)   
