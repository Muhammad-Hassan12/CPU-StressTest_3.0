import numpy as np
import time

# Define the size of the matrix to multiply
MATRIX_SIZE = 1000

# Create two random matrices of the same size
matrix1 = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
matrix2 = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)

start_time = time.time()

# Perform matrix multiplication repeatedly in a loop
while True:
    np.dot(matrix1, matrix2)

    # Check if the desired time has elapsed
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:  # Change the time limit as needed
        break
