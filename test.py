import numpy as np

def householder(A):
    m, n = A.shape
    print(m)
    R = A.copy()
    print(R)
    Q = np.eye(m)


    for k in range(n):
        # Take the k-th column of R from k-th element to the end
        x = R[k:, k]
        e = np.zeros_like(x)
        e[0] = 1

        # Compute the Householder matrix
        v = np.sign(x[0]) * np.linalg.norm(x) * e + x
        print(v)
        v = v / np.linalg.norm(v)

        # Apply Householder transformation to R
        R[k:, :] -= 2 * np.outer(v, np.dot(v, R[k:, :]))
        print("Here", R)

        # Apply Householder transformation to Q
        Q[k:, :] -= 2 * np.outer(v, np.dot(v, Q[k:, :]))

        print(f"Transformation for column {k + 1}:\n{Q @ A}\n")

    return Q

# Given matrix A
A = np.array([[1, -1, 4],
              [1, 4, -2],
              [1, 1, 4],
              [-1, 2, 0]])
#[1, -1, 4],
#[1, 4, -2],
#[1, 4, 2],
#[1, -1, 0]

#[1, 0, 0],
#[0, 1, 0],
#[0, 0, 1],
#[-1, 1, 0],
#[-1, 0, 1],
#[0, -1, 1]
# Convert matrix A to float64
A = A.astype(np.float64)

# Apply Householder transformation
Q = householder(A)

# Display the orthogonal matrix Q
print("Orthogonal Matrix Q:\n", Q)

#
