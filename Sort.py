# coding:utf-8
import numpy as np

def bubble_sort(nums):
    for i in range(1,len(nums)):
        for j in range(len(nums)-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    print nums


# Insertion sort is used when number of elements is small.
# It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]<nums[j]:
                key = nums[i]
                nums[j+1:i+1]=nums[j:i]
                nums[j]=key
                break
    print nums

def merge_sort(nums):
    k = len(nums) / 2
    if k!=0:
        left = merge_sort(nums[0:k])
        right = merge_sort(nums[k:len(nums)])
        mergedNum = merge(left,right)
    else:
        mergedNum=nums
    return mergedNum


def merge(left,right):
    temp = []
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        elif left[i]>=right[j]:
            temp.append(right[j])
            j+=1
    if i==len(left):
        temp=temp+right[j:]
    elif j==len(right):
        temp=temp+left[i:]
    return temp


def quick_sort(nums):
    if len(nums)>1:
        l,nums0 = partition(nums)
        nums_left = quick_sort(nums0[0:l])
        nums_right = quick_sort(nums0[l+1:])
        return nums_left+[nums0[l]]+nums_right
    else:
        return nums

def partition(temp):
    pivot = temp[-1]
    low = -1
    for i in range(len(temp)-1):
        if temp[i]<pivot:
            low+=1
            temp[low],temp[i] = temp[i],temp[low]
    temp[low+1],temp[-1] = temp[-1],temp[low+1]
    return low+1,temp

def heapsort(nums):
    ## build the max heap
    for i in range(len(nums)/2-1,-1,-1):
        nums = Max_Heapify(nums,i)
    ## one by one extract elements
    for i in range(len(nums)-1,0,-1):
        nums[0],nums[i] = nums[i],nums[0]
        nums[0:i]=Max_Heapify(nums[0:i],0)
    return nums

def Max_Heapify(A,i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if right <=len(A)-1 and A[right]>A[largest]:
        largest = right

    if left <=len(A)-1 and A[left]>A[largest]:
        largest = left

    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        A = Max_Heapify(A,largest)

    return A

def counting_sort(nums,high):

    ## to store the ordered output
    orderednums = [0 for i in range(len(nums))]

    count = [0 for i in range(high+1)]
    for num in nums:
        count[num]+=1
    for i in range(len(count)-1):
        count[i+1]=count[i]+count[i+1]
    for i in range(len(nums)):
        orderednums[count[nums[i]]-1]=nums[i]
        count[nums[i]]-=1

    print orderednums



if __name__ == "__main__":
    nums = [19,0,2, 6, 8, 12,7,8, 1, 4, 9, 3, 7, 2, 7]
    print nums
    # bubble_sort(nums)
    # insert_sort(nums)
    # result = merge_sort(nums)
    # result = quick_sort(nums)
    # result = heapsort(nums)
    # counting_sort(nums,np.max(nums))
    # radix_sort(nums)
    # print result










