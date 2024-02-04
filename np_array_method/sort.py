import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

def main():
    _, (ax0, ax1) = plt.subplots(1,2,figsize=(12,3))

    x = np.random.uniform(-2., 2., (100,))
    y0 = x ** 2
    ax0.plot(x,y0)

    x.sort()
    y1 = x ** 2
    ax1.plot(x,y1)
    
    plt.show()

if __name__ == "__main__":
    main()