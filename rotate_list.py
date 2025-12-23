nums=[3, 10, 4, 5, 6]
k=1

n=len(nums)
k=k%n

rotated_lst = nums[-k:] + nums[:n-k]
print(rotated_lst)
