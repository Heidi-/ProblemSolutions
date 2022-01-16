"""
Module to count the longest sequence of 1's in a matrix of 0's and 1's.
"""
import argparse

import numpy as np

def find_longest_sequence(matrix):
    """
    Return longest sequence of 1's in matrix in either row or column direction.

    Args:
        matrix (np.ndarray)

    Returns:
        int
    """
    # need to make border of zeros to start and end counts that span whole row or column
    colzeros = np.full((matrix.shape[1], 1), 0)
    rowzeros = np.full((1, matrix.shape[0] + 2), 0)
    
    appmatrix = np.concatenate([colzeros, matrix, colzeros], axis=1)
    appmatrix = np.concatenate([rowzeros, appmatrix, rowzeros])
    
    
    rowdiff = appmatrix[:,1:] - appmatrix[:,:-1]
    coldiff = appmatrix[1:,:] - appmatrix[:-1,:]
    
    # count row sequences
    startseq = np.argwhere(rowdiff==1)
    endseq = np.argwhere(rowdiff==-1)
    rowseq = [eni[1] - sti[1] for sti, eni in zip(startseq, endseq)]
    
    # count col sequences
    startseq = np.argwhere(coldiff==1)
    endseq = np.argwhere(coldiff==-1)
    colseq = [eni[0] - sti[0] for sti, eni in zip(startseq, endseq)]
    
    return max(rowseq + colseq)


def main():
    """
    Proof of concept.
    """
    parser = argparse.ArgumentParser(description='Input matrix size')
    parser.add_argument('size', type=int, help='size of square matrix')
    args = parser.parse_args()
    
    matrix = np.random.randint(0, 2, (args.size, args.size))

    print("MATRIX")
    print(matrix)
    print("Longest sequence", find_longest_sequence(matrix))


if __name__ == "__main__":
    main()
