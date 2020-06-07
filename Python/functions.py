def square(x):
    return x * x

def main():
    for i in range(1,11):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()
