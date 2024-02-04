import numpy as np; np.random.seed(0)

def main():
    A = np.random.uniform(0., 1., (2,2))
    print(A)
    print()

    A_T = np.transpose(A) # transpose
    print(A_T)
    print()

    A_T = A.T # transpose
    print(A_T)
    

if __name__ == "__main__":
    main()