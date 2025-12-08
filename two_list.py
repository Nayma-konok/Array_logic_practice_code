from collections import Counter

nums1=[1,2,3,4,4,5]
nums2= [2,1,3,3,4,5]

# if sorted(nums1)==sorted(nums2):
if Counter(nums1)==Counter(nums2): #handle the duplicates
    print("Same elements..")
else:
    print("Different elements")
