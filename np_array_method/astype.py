import numpy as np

def main():
    a = np.array([1., 2., 3., 4.])
    print(a.dtype)

    a = a.astype(np.uint8)
    print(a.dtype)

if __name__ == "__main__":
    main()