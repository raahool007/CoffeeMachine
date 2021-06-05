years = 0
initial_sum = int(input())
while initial_sum < 700_000:
    initial_sum *= 1.071
    years += 1
print(years)
