# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n=int(input('enter n'))
    a = []
    for i in range(n):
        a.append(input('enter 2 va;ues').split(' '))
    #print(a)

    for i in a:
        #print(i)
        a=(i[0])
        b=(i[1])
        try:
            print(int(int(a)//int(b)))
        except ValueError as e:
            print("Error Code:", e)
            continue
        except ZeroDivisionError as e:
            print("Error Code:", e)
            continue