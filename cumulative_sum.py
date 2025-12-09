#running sum 1D array

numbers=[1,2,3,4,5]

running_sum=[]
total=0

for num in numbers:
    total=total+num
    print(total)
    running_sum.append(total)

print(running_sum)