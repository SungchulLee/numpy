def main(n=5, p=0.5):
    """
    input n     : number of coin clips 
    input p     : prob of head
    output coin : numpy array of shape (n,) 
                  heads are represented by 1.
                  tails are represented by 0.
    """
    import numpy as np
    uniform = np.random.uniform(size=(n,))
    coin = np.zeros_like(uniform)
    coin[x>1-p] = 1.
    return coin


if __name__ == '__main__':
    n = 5   # number of coin clips 
    p = 0.5 # prob of head
    coin = main(n, p)
    print(coin)