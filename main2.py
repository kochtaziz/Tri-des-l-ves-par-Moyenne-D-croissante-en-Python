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
        students[i] = student

def display(students, n):
    for i in range(n):
        print(students[i]["name"], students[i]["class"], students[i]["avg"], end=' | ')

def bubble_sort(students, n):
    while True:
        swapped = False
        for i in range(n - 1):
            if students[i]["avg"] < students[i + 1]["avg"]:
                students[i], students[i + 1] = students[i + 1], students[i]
                swapped = True
        n -= 1
        if not swapped or n == 1:
            break
    return students

from numpy import array

n = get_size()
students = array([dict()] * n)
fill(students, n)

print('--------------------- List of students before sorting ---------------------------')
display(students, n)
print('\n')
print('************ List of students sorted by descending average ************')
sorted_students = bubble_sort(students, n)
display(sorted_students, n)
