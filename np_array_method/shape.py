import numpy as np

def main():
    a = np.array([1, 2, 3, 4])
    print(a.shape)

    gene0 = [100, 200]
    gene1 = [50, 0]
    gene2 = [350, 100]
    a = np.array([gene0, gene1, gene2])
    print(a.shape)

if __name__ == "__main__":
    main()