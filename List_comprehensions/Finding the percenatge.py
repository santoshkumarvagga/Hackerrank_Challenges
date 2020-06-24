if __name__ == '__main__':
    n = int(input('enter n'))
    student_marks = {}
    for _ in range(n):
        name, *line = input('enter name with marks').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('enter query name')
    avg = 0
    sum = 0
    for key,values in student_marks.items():
        if key == query_name:
            for i in values:
                sum = sum + i
            avg = float(sum / len(values))
    print(avg)
    print(type(avg))
    print("{:.2f}".format(avg))