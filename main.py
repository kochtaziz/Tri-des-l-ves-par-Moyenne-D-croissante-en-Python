def get_size():
    n = int(input("Enter the number of students: "))
    while n < 2:
        n = int(input("Enter a valid number (>= 2): "))
    return n

def fill(students, n):
    for i in range(n):
        student = {"name": "", "class": "", "avg": 0.0}
        student["name"] = input("Enter the name of student " + str(i) + ": ")
        student["class"] = input("Enter the class of student " + str(i) + ": ")
        student["avg"] = float(input("Enter the average of student " + str(i) + ": "))
        students.append(student)

def display(students):
    for s in students:
        print(f"{s['name']} {s['class']} {s['avg']}", end=" | ")

def max_index(students, n, i):
    max_avg = students[i]["avg"]
    max_idx = i
    for j in range(i + 1, n):
        if students[j]["avg"] > max_avg:
            max_avg = students[j]["avg"]
            max_idx = j
    return max_idx

def selection_sort(students, n):
    for i in range(n - 1):
        pos = max_index(students, n, i)
        if pos != i:
            students[i], students[pos] = students[pos], students[i]

n = get_size()
students = []
fill(students, n)

print('--------------------- List of students before sorting ---------------------------')
display(students)

selection_sort(students, n)

print('\n')
print('************ List of students sorted by descending averages ************')
display(students)
