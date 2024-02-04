import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

def main():
    x = np.linspace(-3, 3, 100)
    y = 1 + x + x**2 + np.random.normal(size=x.shape)*0.2

    plt.plot(x, y)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()