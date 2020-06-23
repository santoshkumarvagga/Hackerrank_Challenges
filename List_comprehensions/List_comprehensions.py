arr = []
if __name__ == '__main__':
    x = int(input('enter x'))
    y = int(input('enter y'))
    z = int(input('enter z'))
    n = int(input('enter n'))
    [ arr.append([i,j,k]) for i in range( x + 1) for j in range( y + 1) for k in range( z + 1)if ( ( i + j+ k ) != n )]
    print(arr)
    
