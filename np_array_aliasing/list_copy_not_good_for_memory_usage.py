def main():
    # Create a list x
    x = [1, 2, 3]
    print(x)

    # Create a "slice" of x
    y = x[:2]
    print(y)

    # Set the first element of y to be 6
    y[0] = 6
    print(y)

    # However, the first element in x stays as 1!
    print(x)

if __name__ == "__main__":
    main()