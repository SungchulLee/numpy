import numpy as np; np.random.seed(0)

def main():
    x = np.array([[0,1],[2,3]])
    print(x)
    print()

    print(np.max(x))
    print(x.max())
    print()

    print(np.max(x, axis=0))
    print(x.max(axis=0))
    print()

    print(np.max(x, axis=1))
    print(x.max(axis=1))
    print()

if __name__ == "__main__":
    main()