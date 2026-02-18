more=[x+1 for x in[1,2,3,4]]  #[2,3,4,5] the values of x takes a value from the list and adds one to that digit.
print()                       #it is the same value but the digits with in are larger.

def square(n:int) -> int:
    return n*n                          #n:1,2,3,4 return values: 1,4,9,16

squares=[square(x)for x in [1,2,3,4]]   #[1,4,9,16] they are related by just by being multiplied by themselves.
print()

def check(n:int) -> bool:
    return n>2                              #0,1,2,3,4
answer=[x for x in range(5) if check(x)]    #[3,4]
print()

def inc(m:int) -> int:
    return m+1              # 3,4
def check(n:int) -> bool:
    return n>2              # 0,1,2,3,4
answer = [inc(x) for x in range(5) if check(x)] # [4,5]
print()

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total= total + num      #total;4,13,15,16  number;4,9,2,1

    return total
result=tally([4,9,2,1])

def copy(nums:list[int]) -> list[int]:
    new_list=[]
    for idx in range(len(nums)):        #[] idx:0, [4] idx:1, [4,9] idx:9, [4,9,2] idx:3, [4,9,2,1] idx:3
        new_list.append(nums[idx])
                                        #this one is adding values to a list slowly after each run through
    return new_list                     #while the other one is adding the values together.
result=copy([4,9,2,1])

def increment_all(nums:list[int]) -> list[int]:
    new_list=[]
    for value in nums:
        new_list.append(value+1)    #values at end: 4 9 2 1
    return new_list                 #new_list [] [5] [5,10] [5,10,3] [5,10,3,2]
result=increment_all([4,9,2,1])






