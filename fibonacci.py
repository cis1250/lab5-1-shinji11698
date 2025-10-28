def getNumterms():
    while True:
        try:
            numOfitems = int(input("Enter how many terms of the Fibonacci sequence: "))
            if numOfitems > 0:
                return numOfitems
            else:
                print("Please enter a positive integer bigger  than 0.")
        except ValueError:
            print("Invalid input.")

# Function 2: Generate Fibonacci sequence
def genFibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def print_fibonacci(seq):
    print("Fibonacci sequence:")
    print(",".join(str(numOfitems) for numOfitems in seq))

def main():
    numOfterms = getNumterms()
    fib_seq = genFibonacci(numOfterms)
    print_fibonacci(fib_seq)

if __name__ == "__main__":
    main()
