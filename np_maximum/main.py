import numpy as np; np.random.seed(0)

def main():
    x = np.array([[0,1],[2,-3]])
    y = np.array([[0,-1],[2,3]])
    z = np.maximum(x, y)
    print(z)
    print()

    a = np.array([3,2,5])
    print(np.maximum(a,4))

if __name__ == "__main__":
    main()