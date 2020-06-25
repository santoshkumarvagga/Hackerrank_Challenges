import re
def count_substring(string, sub_string):
    count = 0
    n = len(string)
    m = len(sub_string)
    for i in range(n - m + 1):
        for j in range(m):
            if string[i + j] != sub_string[j]:
                break
        if j == m - 1:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input('enter string').strip()
    sub_string = input('enter substring').strip()
    count = count_substring(string, sub_string)
    print(count)