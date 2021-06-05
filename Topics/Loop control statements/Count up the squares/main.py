# put your python code here
int_array = []


def _sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


def sum_of_squares(arr):
    total = 0
    for i in arr:
        total += i ** 2
    return total


while True:
    next_int = int(input())
    int_array.append(next_int)
    if _sum(int_array) == 0:
        break

print(sum_of_squares(int_array))
