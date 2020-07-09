def matchingStrings(strings, queries):
    s = {}
    for i in queries:
        print("queries :",i)
        if i in strings:
            print("strings: ",i)
            if i not in s:
                print(i, "not in s")
                s[i] = strings.count(i)
                print("count of {} made to {}".format(i,s[i]))
            else:
                print(i,"in s")
                pass
        else:
            print(i,"not found in strings[]")
            s[i] = 0
            print("So, entry for {} is made to {}".format(i,s[i]))
    v = list(s.values())
    print(v)
    return(v)

strings = ['def','de','fgh']
queries = ['de','lmn','fgh']

matchingStrings(strings, queries)