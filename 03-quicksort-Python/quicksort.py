"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(arr, low, high):
	i = low-1
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return i+1

def sort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		sort(arr,low,pi-1)
		sort(arr,pi+1,high)

def quicksort(array):
	# Your code goes here
	n = len(array)
	low = 0
	high = n-1
	sort(array, low, high)
	l = []
	for i in range(n):
		l.append(array[i])
	return l
