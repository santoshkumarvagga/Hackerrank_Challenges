def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        decimals = str(i)
        octals = str(oct(i)[2:])
        hexs = str(hex(i)[2:])
        bins = str(bin(i)[2:])
        binlen = len(bin(number)[2:])
        print(decimals.rjust(binlen),octals.rjust(binlen),hexs.rjust(binlen),bins.rjust(binlen))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)