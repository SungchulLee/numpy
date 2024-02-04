import numpy as np; np.random.seed(0)

def main():
    A = np.random.uniform(0., 1., (2,2))
    print(A)
    print()

    inv_A = np.linalg.inv(A) # inverse
    print(inv_A)

if __name__ == "__main__":
    main()