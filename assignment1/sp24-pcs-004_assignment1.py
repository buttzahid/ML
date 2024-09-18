# %%
import numpy as np
import pandas as pd

# %%
nums = [3, 5, 7, 8, 12]
cubes = []

# Appending the cubes of elements in nums to the cubes list
for num in nums:
    cubes.append(num ** 3)

# Print the cubes list
print(cubes)


# %%
# Creating an empty dictionary
dict = {}

# Adding the key-value pairs
dict['parrot'] = 2
dict['goat'] = 4
dict['spider'] = 8
dict['crab'] = 10

# Print the dictionary
print(dict)


# %%
# Initialize a variable for the total number of legs
total_legs = 0

# Looping through the dictionary items
for animal, legs in dict.items():
    print(f"{animal}: {legs} legs")
    total_legs += legs

# Print the total number of legs
print(f"Total legs: {total_legs}")


# %%
# Creating a tuple with a list inside
A = (3, 9, 4, [5, 6])

# Changing the value 5 to 8 in the list inside the tuple
A[3][0] = 8

# Print the modified tuple
print(A)


# %%
# Deleting the tuple A
del A


# %%
# Creating the tuple
B = ('a', 'p', 'p', 'l', 'e')

# Counting the number of occurrences of 'p'
count_p = B.count('p')

# Print the count of 'p'
print(f"Occurrences of 'p': {count_p}")


# %%
# Finding the index of 'l' in tuple B
index_l = B.index('l')

# Print the index of 'l'
print(f"Index of 'l': {index_l}")


# %%
# Define matrix A
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# Define vector z
z = np.array([1, 0, 1])
# 2.1 Convert matrix A into numpy array (already defined as a numpy array)
print("Matrix A as a NumPy array:\n", A)


# %%
# 2.2 Use slicing to pull out the subarray consisting of the first 2 rows and columns 1 and 2.
b = A[:2, :2]
print("Subarray b (first 2 rows and columns 1 and 2):\n", b)


# %%
# 2.3 Create an empty matrix 'C' with the same shape as 'A'
C = np.empty_like(A)
print("Empty matrix C with the same shape as A:\n", C)


# %%
# Define matrix A
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
# 2.4 Add the vector z to each column of the matrix 'A' with an explicit loop and store it in 'C'
for i in range(A.shape[1]):
    C[:, i] = A[:, i] + z
print("Matrix C after adding vector z to each column of A:\n", C)

# Define X, Y, and v
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])

# %%
# 2.5 Add and print the matrices X and Y
sum_XY = np.add(X, Y)  # Or X + Y
print("Sum of matrices X and Y:\n", sum_XY)


# %%
# 2.6 Multiply and print the matrices X and Y (element-wise multiplication)
product_XY = np.multiply(X, Y)  # Or X * Y
print("Element-wise multiplication of X and Y:\n", product_XY)


# %%
# 2.7 Compute and print the element-wise square root of matrix Y
sqrt_Y = np.sqrt(Y)
print("Element-wise square root of matrix Y:\n", sqrt_Y)


# %%
# 2.8 Compute and print the dot product of the matrix X and vector v
dot_product = np.dot(X, v)
print("Dot product of matrix X and vector v:\n", dot_product)


# %%
# 2.9 Compute and print the sum of each column of X
column_sum = np.sum(X, axis=0)
print("Sum of each column of matrix X:\n", column_sum)


# %%
# 3.1 Define the function Compute
def Compute(distance, time):
    if time == 0:
        return "Time cannot be zero!"
    else:
        velocity = distance / time
        return velocity

# Example usage
distance = 100  # meters
time = 10  # seconds
velocity = Compute(distance, time)
print(f"Velocity = {velocity} m/s")


# %%
# 3.2 Create the list of even numbers up to 12
even_num = [2, 4, 6, 8, 10, 12]

# Define the function mult
def mult(even_num):
    product = 1  # Start with 1 as the identity element for multiplication
    for num in even_num:
        product *= num
    return product

# Example usage
result = mult(even_num)
print(f"The product of all even numbers is: {result}")


# %%
# 4. Create the DataFrame 'pd'
data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}

# Create DataFrame
df = pd.DataFrame(data)
print("DataFrame 'pd':\n", df)

# 4.1 Print only the first two rows of the dataframe
print("\n4.1 First two rows:\n", df.head(2))

# %%
# 4.2 Print the second column
print("\n4.2 Second column:\n", df['C2'])

# %%
# 4.3 Change the name of the third column from ‘C3’ to ‘B3’
df.rename(columns={'C3': 'B3'}, inplace=True)
print("\n4.3 DataFrame after renaming column 'C3' to 'B3':\n", df)

# %%
# 4.4 Add a new column to the dataframe and name it ‘Sum’
df['Sum'] = 0
print("\n4.4 DataFrame after adding column 'Sum':\n", df)

# %%
# 4.5 Sum the entries of each row and add the result in the column ‘Sum’
df['Sum'] = df.sum(axis=1)
print("\n4.5 DataFrame after summing rows and adding to 'Sum':\n", df)

# %%
# 4.6 Read CSV file 'hello_sample.csv' into a Pandas dataframe
# Assuming 'hello_sample.csv' is located in the same directory or provided path
# For example purposes, I'll simulate this part:
df_csv = pd.read_csv('datasets/hello_sample.csv')
# For now, skipping this due to the lack of actual file in the current environment

# %%
# 4.7 Print complete dataframe (assuming the csv is loaded)
print("\n4.7 Complete DataFrame:\n", df_csv)

# %%
# 4.8 Print only the bottom 2 records of the dataframe
print("\n4.8 Bottom 2 records:\n", df_csv.tail(2))

# %%
# 4.9 Print information about the dataframe
print("\n4.9 Information about the DataFrame:\n")
df_csv.info()

# %%
# 4.10 Print shape (rows x columns) of the dataframe
print("\n4.10 Shape of the DataFrame:\n", df_csv.shape)

# %%
# 4.11 Sort the data of the dataframe using column ‘Weight’
# Assuming 'Weight' column exists in the CSV file
df_sorted = df_csv.sort_values(by='Weight')
print("\n4.11 DataFrame sorted by 'Weight':\n", df_sorted)

# %%
# 4.12 Use isnull() and dropna() methods and see if they produce changes
# Checking for missing values
print("\n4.12 Checking for missing values (isnull):\n", df_csv.isnull())

# %%
# Dropping rows with missing values (if any)
df_dropped_na = df_csv.dropna()
print("\n4.12 DataFrame after using dropna:\n", df_dropped_na)


