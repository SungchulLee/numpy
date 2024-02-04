import numpy as np

def main():
    # Create an ndarray x
    x = np.array([1, 2, 3])
    print(x)

    # Create a "slice" of x
    y = x[:2]
    print(y)

    # Set the first element of y to be 6
    y[0] = 6
    print(y)

    # Now the first element in x has changed to 6!
    print(x)

if __name__ == "__main__":
    main()