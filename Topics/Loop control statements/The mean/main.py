total = 0
counter = 0
while True:
    bucket = input()
    if bucket == '.':
        break
    total += int(bucket)
    counter += 1
print(total / counter)