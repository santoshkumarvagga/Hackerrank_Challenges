import textwrap

def wrap(string, max_width):
    res = []
    s = ''
    for i in range(len(string)):
        if (i+1)%max_width==0:
            res.append(string[i])
            res.append('\n')
            #print(string[i],end='\n')
        else:
            res.append(string[i])
            #print(string[i],end='')
    return s.join(res)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)