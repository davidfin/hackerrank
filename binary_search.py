def binary_search(array, x, left, right):

	if (left > right): 
		return False 
	
	mid = (left + right) / 2

	if (array[mid] == x): 
		return True 
	elif (x < array[mid]): 
		return binary_search(array, x, left, mid-1)
	else: 
		return binary_search(array, x, mid+1, right)
		
