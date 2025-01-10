import numpy as np

vector = np.arange(10)


m1 = np.arange(1, 17).reshape(4,4)


m2 = np.random.randint(0, 101,(5,5))  



mean = np.mean(m2)
median = np.median(m2)



identity = np.identity(3)



m3 = np.arange(1, 37).reshape(6,6).reshape(3,12)




vector2 = np.random.rand(15)




count = np.sum(vector2 > 0.5)



matrix_4x4 = np.random.rand(4, 4)
determinant = np.linalg.det(matrix_4x4)



matrix_3x3 = np.arange(9).reshape(3, 3)
transposed_matrix = matrix_3x3.T



random_vector = np.random.rand(10)
max_index = np.argmax(random_vector)



matrix_even = np.random.randint(0, 10, (4, 4))
matrix_even[matrix_even % 2 == 0] = -1



row_values = (np.arange(1, 6)).reshape(5,1)
col_values = (np.arange(6, 11)).reshape(1,5)
matrix_5x5 = row_values + col_values



matrix_3x3_mult = np.arange(9).reshape(3, 3)
matrix_3x2 = np.random.rand(3, 2)  
product = np.dot(matrix_3x3_mult, matrix_3x2)



matrix_inverse = np.random.randint(1,16,(4, 4))
inverse_matrix = np.linalg.inv(matrix_inverse)




print("Random 4x4 Matrix:\n", matrix_4x4)
print("Determinant:", determinant)

print("3x3 Matrix:\n", matrix_3x3)
print("Transposed:\n", transposed_matrix)

print("Random Vector:\n", random_vector)
print("Index of Maximum Value:", max_index)

print("4x4 Matrix with Even Numbers Replaced by -1:\n", matrix_even)

print("5x5 Matrix with Row and Column Values:\n", matrix_5x5)

print("Product of 3x3 Matrix and Random 3x2 Matrix:\n", product)

print("Inverse of Random 4x4 Matrix:\n", inverse_matrix)
