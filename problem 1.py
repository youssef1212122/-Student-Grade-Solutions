steps = list(map(int, input("Enter the number of steps taken each day in the month: ").split()))

max_steps = max(steps)
min_steps = min(steps)

average_steps = sum(steps) / len(steps) # 30

sorted_steps = sorted(steps, reverse=True)

print(f"Highest step count: {max_steps}")
print(f"Lowest step count: {min_steps}")
print(f"Average daily step count: {average_steps:.2f}")
print("Step counts in descending order:", *sorted_steps)
