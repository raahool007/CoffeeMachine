# put your python code here
bucket = 0
while True:
    bucket = int(input())
    if bucket < 10:
        continue
    elif bucket > 100:
        break
    else:
        print(bucket)