numbers=[3, 4, 5, 6]

#metod:1In-place reversal (Two Pointers)
left=0
right=len(numbers)-1

while right>left:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left+=1
    right-=1
print(numbers)       

#method2:Using a new list (Extra space)

rev_nums=[]

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])
    rev_nums.append(numbers[i])

print(rev_nums)