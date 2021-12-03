# Advent of Code 2021
# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1
#
# Author: NoNonsenseTekkie

# Read in the input file
INPUT = "input.txt"

# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
with open(INPUT) as file:
    lines = file.readlines()
    # https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    measurements = list(map(int, lines))

    # Problem 1
    count = 0
    previous = None
    for value in measurements:
        if previous is not None and value > previous:
            # print(f"{previous} --> {value}")
            count += 1
        previous = value
    print(f"Number of measurements larger than previous measurement: {count}")

    # Problem 2
    # References:
    # + https://www.geeksforgeeks.org/window-sliding-technique/
    # + https://blog.finxter.com/how-to-loop-through-a-python-list-in-batches/
    count = 0
    n = len(measurements)
    k = 3  # sliding window
    # Sum of first window of size k
    previous_sum = sum(measurements[:k])

    # Find remaining sums of windows by removing first element of previous window and add last element of current window.
    for i in range(n - k):
        window_sum = previous_sum - measurements[i] + measurements[i + k]
        if window_sum > previous_sum:
            # print(f"{previous_sum} --> {window_sum}")
            count += 1
        previous_sum = window_sum
    print(f"Number of sums larger than previous sum: {count}")
