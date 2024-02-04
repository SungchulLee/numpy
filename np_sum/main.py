import numpy as np; np.random.seed(0)

def main():
    x = np.array([[0,1],[2,3]])
    print(x)
    print()

    print(np.sum(x))
    print(x.sum())
    print()

    print(np.sum(x, axis=0))
    print(x.sum(axis=0))
    print()

    print(np.sum(x, axis=1))
    print(x.sum(axis=1))
    print()

if __name__ == "__main__":
    main()