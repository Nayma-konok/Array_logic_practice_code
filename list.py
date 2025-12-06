numbers=[3,10, 4, 5, 6]

largest=numbers[0]
smallest=numbers[0]

#largest number
for num in numbers:
    print(num)
    if num>largest:
        largest=num

#smallest number
for num in numbers:
    if num<smallest:
        smallest = num
        
print(largest)
print(smallest)