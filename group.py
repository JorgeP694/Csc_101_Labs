#Name:
# Section: 09
#Professor: Dr. S. Einnakain
# Task 1
'''
design recipe
input: list of int
output: list of list of int
purpose: to
'''
def group_of_3(nums:list[int]) ->list[list[int]]:
    new_list=[]
    for i in range (0,len(nums),3):
        together = nums[i:i+3]
        new_list.append(together)
    return new_list