# Advent of Code 2021
# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3
#
# Author: NoNonsenseTekkie

import pandas as pd
import numpy as np


def to_binary_matrix(report):
    """
    Convert the diagnostic report as list of lines into a list of arrays.
    :param report: The input report as a list of lines.
    :return: A list of column headers and a list of arrays of binaries.
    """
    arrays = list(map(lambda n: list(n.strip()), report))
    headers = ["c" + str(i+1) for i in range(len(arrays[0]))]
    return headers, arrays


def to_decimal(binary_array):
    binary_str = "".join(binary_array)
    return int(binary_str, 2)


def part_1(report):
    """
    Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them
    together. What is the power consumption of the submarine?
    (Be sure to represent your answer in decimal, not binary.)

    :param report: The list of binary numbers in the diagnostic report
    :return: The power consumption of the submarine (gamma rate x epsilon rate)
    """
    headers, binary_arrays = to_binary_matrix(report)
    df = pd.DataFrame(np.array(binary_arrays), columns=headers)
    # Get the top most values from mode for gamma rate
    gamma_array = df.mode().to_numpy()[0]
    gamma = to_decimal(gamma_array)
    # Flip 0 and 1 for epsilon from gamma
    epsilon_array = list(map(lambda d: '1' if d == '0' else '0', gamma_array))
    epsilon = to_decimal(epsilon_array)
    return gamma * epsilon


# MAIN STARTS HERE
INPUT = "input.txt"
with open(INPUT) as file:
    lines = file.readlines()

solution_1 = part_1(report=lines)
print(f"The power consumption of the submarine is {solution_1}.")
