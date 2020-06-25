def swap_case(s):
    s=list(s)
    m = ''
    for i in range(len(s)):
        if s[i].islower():
            s[i]=s[i].upper()
        else:
            s[i]=s[i].lower()
    m=m.join(s)
    return m

if __name__ == '__main__':
    s = input('enter string')
    result = swap_case(s)
    print(result)