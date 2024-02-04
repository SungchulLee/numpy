import numpy as np

def main():
    x = np.array([[0,1],[2,3]])
    print(x)
    print()

    print(np.cumsum(x))
    print(x.cumsum())
    print()

    print(np.cumsum(x, axis=0))
    print(x.cumsum(axis=0))
    print()

    print(np.cumsum(x, axis=1))
    print(x.cumsum(axis=1))
    print()

if __name__ == "__main__":
    main()