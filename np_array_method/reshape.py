import numpy as np

def main():
    gene0 = [100, 200]
    gene1 = [50, 0]
    gene2 = [350, 100]
    a = np.array([gene0, gene1, gene2])
    print(a.shape)

    a = a.reshape((1,3,2))
    print(a.shape)

    a = a.reshape((-1,))
    print(a.shape)

if __name__ == "__main__":
    main()