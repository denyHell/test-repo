import sys
import os

import random
import math



def quickSort(l, r, nums):
	if l<r:
		p = partition(l, r, nums)
		quickSort(l, p-1, nums)
		quickSort(p+1, r, nums)
	return 

def partition(l, r, nums):
	pivot = nums[r]
	i , j =l, r-1
	while(i<=j):
		if nums[i] < pivot:
			i += 1
		elif nums[j] > pivot:
			j -= 1
		else:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j -= 1
	nums[i], nums[r] = nums[r], nums[i]
	return i

a= [2,8,7,1,3,5,6,4]
quickSort(0,len(a)-1,a)
print(a)


def mergeSort(nums, l, r):
	if l == r:
		return [nums[l]]
	mid = (l + r) >> 1
	left = mergeSort(nums, l, mid)
	right = mergeSort(nums, mid+1,r)
	return combine(left, right)

def combine(nums1, nums2):
	n, m = len(nums1), len(nums2)
	i, j = 0, 0
	res = []
	while(i < n or j < m):
		if i == n:
			res = res + nums2[j:]
			return res
		elif j == m:
			res = res + nums1[i:]
			return res
		else:
			if nums1[i] <= nums2[j]:
				res.append(nums1[i])
				i += 1
			else:
				res.append(nums2[j])
				j += 1
	return res

print(mergeSort(a, 0, len(a)-1))

