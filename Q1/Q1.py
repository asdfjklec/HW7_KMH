import numpy as np

def main():

    arr = np.array ([[1, 2],[3, 4]])

    elg_val, elg_vec = np.linalg.eig(arr)
    deter = int(np.linalg.det(arr))

    print("eigenvalues :" , elg_val)
    print("eigenvectors :  \n ", elg_vec)
    print("determinant : ", deter)

    
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])

    vec3_1 = np.matmul(vec1, vec2.T)

    print("cross product : ", vec3_1)

    
    A = np.array([[1, 2, -2],[2, 1 , -5],[1, -4, 1]])
    b = np.array([-15, -21, 18])
    x = np.linalg.solve(A,b)

    print("Solution : " , x)

if __name__ == '__main__':
    main()
