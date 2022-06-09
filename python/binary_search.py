import math
 
def binary_search(trgt,lst):
    lst.sort()
    middle=math.floor(len(lst)/2)
    # print(middle)
    # print(lst[middle])
    # print(lst)
    if trgt not in lst:
        return -1
    else:
        if lst[middle] == trgt:
            return middle
        #
        elif lst[middle]<trgt:
            # print('upper')
            lst= lst[middle:]
            return binary_search(trgt,lst)+middle
        #
        elif lst[middle]>trgt:
            # print('lower')
            lst=lst[:middle]
            return binary_search(trgt, lst)
    



values=[1,5,7,2,3,8,4,9]
answer=binary_search(6,values)
print(answer)
