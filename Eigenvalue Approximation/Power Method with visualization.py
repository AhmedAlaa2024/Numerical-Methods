import numpy as np
from numpy.core.records import array

# Request the matrix from the user
A = [float(a) for a in input("Please, Enter the matrix row by row: ").split(" ")]
A_shape = [int(i) for i in input("Please, Enter the dimension of the previous matrix: ").split(" ")]
A = np.array(A).reshape(A_shape)

# Request the starting vector from the user
X = [float(a) for a in input("Please, Enter the starting vector: ").split(" ")]
X_shape = [int(i) for i in input("Please, Enter the dimension of the previous vector: ").split(" ")]
X = np.array(X).reshape(X_shape)

def PowerMethod(A, X, tolerance, ndigits, counter = np.inf):
    print('#' * 50, "The Power Method", '#' * 50)
    i = 1
    B = list()
    print("Iteration No.", 0)
    print(X.T, "---")
    print("Iteraion No.", 1)
    B.append(np.dot(A, X))
    print(B[0].T, "---")
    print("Iteration No.", 2)
    # min = np.amax([abs(b) for b in B[0]])
    # B[0] = np.array([b / min for b in B[0]])
    B.append(np.dot(A, B[0]))
    dominant_eigenvalue = round(np.amax([abs(b) for b in abs(B[1])]) / np.amax([abs(b) for b in abs(B[0])]), ndigits)
    print(B[1].T, dominant_eigenvalue)
    # min = np.amax([abs(b) for b in B[1]])
    # B[1] = np.array([b / min for b in B[1]])
    previous = -1
    while((abs(dominant_eigenvalue - previous) > tolerance or (dominant_eigenvalue == previous)) and i <= counter-2):
        B.append(np.dot(A, B[i]))
        previous = dominant_eigenvalue
        i += 1
        # min = np.amax([abs(b) for b in B[i]])
        # B[i] = np.array([b / min for b in B[i]])
        dominant_eigenvalue = round(np.amax([abs(b) for b in abs(B[i])]) / np.amax([abs(b) for b in abs(B[i - 1])]),ndigits)
        print("Iteration No.", i+1)
        print(B[i].T, dominant_eigenvalue)

    print('#' * 120)
    dominant_eignevector = np.round([(b / np.amin([abs(b) for b in abs(B[i])])) for b in B[i]],ndigits)
    
    return [dominant_eignevector, dominant_eigenvalue, i+1]

# Example 1: 2 1 1 1 2 1 1 1 2
# Example: 1 -1 0 -2 4 -2 0 -1 2
# PowerMethod(A, X, 0.0001, 5)
[dominant_eignevector, dominant_eigenvalue, i] = PowerMethod(A, X, 0.0001, 5)
print("The Dominant Eigenvalue =", dominant_eigenvalue)
print("The Dominant Eigenvector =", dominant_eignevector.T)
print("Total Number of iterations =", i)