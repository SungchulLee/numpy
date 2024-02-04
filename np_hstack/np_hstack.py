import numpy as np; np.random.seed(0)

def main():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5], [6]])
    c = np.hstack([a, b])
    print(a.shape)
    print(b.shape)
    print(c.shape)
    print()

    a = np.array([[1, 2], [3, 4]])
    b1 = np.array([[5], [6]])
    b2 = np.array([[5], [6]])
    b3 = np.array([[5], [6]])
    c = np.hstack([a, b1, b2, b3])
    print(a.shape)
    print(b1.shape)
    print(b2.shape)
    print(b3.shape)
    print(c.shape)

if __name__ == "__main__":
    main()