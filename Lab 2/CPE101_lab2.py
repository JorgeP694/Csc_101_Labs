def modify(first:list[ int ], second:list[ int ]) -> int:
     res = first[ 2 ] * second[ 1 ]
     return res

theList = [1,2,3]
result = modify(theList, theList)