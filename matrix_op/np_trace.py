import numpy as np; np.random.seed(0)

def main():
    A = np.random.uniform(0., 1., (2,2))
    print(A)
    print()

    det_A = np.linalg.det(A) # determinant
    print(det_A)

if __name__ == "__main__":
    main()