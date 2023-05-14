import numpy as np
import time

MATRIX_SIZE = 1000

matrix1 = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
matrix2 = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)

start_time = time.time()

while True:
    np.dot(matrix1, matrix2)

    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        break
