
import numpy as np

def householder(A):
    n = len(A)
    a_Tra = np.transpose(A)
    Q = np.eye(A)
    print(Q)



    for i in range(len(a_Tra)):
        print("Now number ", i+1)
        al = np.sum(a_Tra[0]**2)
        #print(al)
        al = -(np.sqrt(al))
        print("This is the square: ",al)
        aT = np.zeros(n)
        aT[0] = 1
        v = np.dot(al,aT)
        #print(v)
        v = np.subtract(a_Tra[0],v)
        #print(v)
        ha = np.subtract(a_Tra[i],2*(np.matmul(v,a_Tra[i]))/(np.matmul(v,v))*v)
        print(ha)





        #al[i] = -np.sqrt(A[i][i])






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = np.array([
        [1, -1, 4],
        [1, 4, -2],
        [1, 1, 4],
        [-1, 2, 0]
    ])
    A = A.astype(np.float64)
    householder(A)


