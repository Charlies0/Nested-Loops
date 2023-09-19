def sum_proper_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def classify_numbers(upper_bound):
    deficient_count = 0
    perfect_count = 0
    abundant_count = 0

    for num in range(1, upper_bound + 1):
        divisors_sum = sum_proper_divisors(num)

        if divisors_sum < num:
            deficient_count += 1
        elif divisors_sum == num:
            perfect_count += 1
        else:
            abundant_count += 1

    return deficient_count, perfect_count, abundant_count

# Get the upper bound from the user
upper_bound = int(input("Enter an upper bound: "))

# Calculate the counts
deficient_count, perfect_count, abundant_count = classify_numbers(upper_bound)

# Output the results
print(f"Deficient numbers: {deficient_count}")
print(f"Perfect numbers: {perfect_count}")
print(f"Abundant numbers: {abundant_count}")