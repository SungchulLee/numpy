import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

def main():
    # https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html
    # shuffle(x) modify a sequence in-place by shuffling its contents.
    x = [1,2,3,4,5,6] 
    np.random.shuffle(x)
    print(x)

if __name__ == "__main__":
    main()