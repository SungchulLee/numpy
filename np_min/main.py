import numpy as np; np.random.seed(0)

def main():
    x = np.array([[0,1],[2,3]])
    print(x)
    print()

    print(np.min(x))
    print(x.min())
    print()

    print(np.min(x, axis=0))
    print(x.min(axis=0))
    print()

    print(np.min(x, axis=1))
    print(x.min(axis=1))
    print()

if __name__ == "__main__":
    main()