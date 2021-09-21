"""
Script to solve the snail problem - unwrapping a square matrix in a clockwise
spiral starting at top left corner.
"""
import timeit

import numpy as np

FORWARD_SLICE = slice(None, None)
BACKWARD_SLICE = slice(None, None, -1)

def pop_row(idx, arr):
	"""
	Return row from array and array without the row.
	First row is returned forward, last row backward.

	Args:
		idx (int) - 0 or -1, row to pop
		arr (2D np.ndarray)

	Returns:
		row (np.ndarray), arr (np.ndarray)

	Raises:
		ValuelError if idx not 0 or -1
	"""
	if idx == 0:
		return arr[0, FORWARD_SLICE], arr[1:,:]
	if idx == -1:
		return arr[-1, BACKWARD_SLICE], arr[:-1,:]
	raise ValueError("idx must be 0 or 1")


def pop_col(idx, arr):
	"""
	Return column from array and array without the column.
	First column is returned backward, last column forward.

	Args:
		idx (int) - 0 or -1, column to pop
		arr (2D np.ndarray)

	Returns:
		column (np.ndarray), arr (np.ndarray)

	Raises:
		ValuelError if idx not 0 or -1
	"""
	if idx == 0:
		return arr[BACKWARD_SLICE, 0], arr[:,1:]
	if idx == -1:
		return arr[FORWARD_SLICE, -1], arr[:,:-1]
	raise ValueError("idx must be 0 or 1")

def return_snail(arr):
	"""
	Return snail array for square matrix arr.

	Args:
		arr (np.ndarray 2D square)

	Returns:
		np.ndarra
	"""
	ar = arr.copy()
	snail = np.array([])
	try:
		while ar.size:
			nxt, ar = pop_row(0, ar)
			snail = np.append(snail, nxt)
			nxt, ar = pop_col(-1, ar)
			snail = np.append(snail, nxt)
			nxt, ar = pop_row(-1, ar)
			snail = np.append(snail, nxt)
			nxt, ar = pop_col(0, ar)
			snail = np.append(snail, nxt)
	except IndexError:
		pass
	return snail

def main():
	"""
	Test it.
	"""
	print("\nrunning 5x5")
	ar = np.random.randint(0, 10, size=(5,5))
	print("Matrix:")
	print(ar)
	print("unwound:")
	print(return_snail(ar))

	print("\nrunning 6x6")
	ar = np.random.randint(0, 10, size=(6,6))
	print("Matrix:")
	print(ar)
	print("unwound:")
	print(return_snail(ar))

	print("\nrunning 500 x 500")
	ar = np.random.randint(0, 10, size=(500,500))
	ts0 = timeit.default_timer()
	sn = return_snail(ar)
	ts1 = timeit.default_timer()
   
	print("time:", ts1-ts0)

if __name__=="__main__":
	main()
