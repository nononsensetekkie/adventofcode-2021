# Advent of Code 2021
# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3
#
# Author: NoNonsenseTekkie

import pandas as pd
import numpy as np


def make_headers(n):
    return ["c" + str(i+1) for i in range(n)]


def to_binary_matrix(report):
    """
    Convert the diagnostic report as list of lines into a list of arrays.
    :param report: The input report as a list of lines.
    :return: A Numpy 2-D array of a list of arrays of binaries.
    """
    arrays = list(map(lambda n: list(n.strip()), report))
    return np.array(arrays)


def to_decimal(binary_array):
    """
    Join the list of ['1', '0', '1', '1', '0'] into a binary string
    and convert into decimal integer.
    :param binary_array: The list of binary strings.
    :return: The decimal value of the joined binary string.
    """
    binary_str = "".join(binary_array)
    return int(binary_str, 2)


def get_gamma_array(df: pd.DataFrame):
    """
    Get the top most values from the data frame mode as gamma rate.
    :param df: The data frame to extract gamma rate.
    :return: The gamma rate array.
    """
    top = df.mode().to_numpy()
    if top.shape[0] > 1:
        gamma_list = [top[1][i] if top[1][i] == '1' else top[0][i] for i in range(top.shape[1])]
        array = np.array(gamma_list)
    else:
        array = top[0]
    return array


def part_1(df: pd.DataFrame):
    """
    Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them
    together. What is the power consumption of the submarine?
    (Be sure to represent your answer in decimal, not binary.)

    :param df: The data frame of the diagnostic report.
    :return: The power consumption of the submarine (gamma rate x epsilon rate)
    """
    print("\n===== Part 1 =====")
    gamma_array, epsilon_array = get_gamma_epsilon(df)
    gamma = to_decimal(gamma_array)
    epsilon = to_decimal(epsilon_array)
    print(f"Gamma = {gamma} | Epsilon = {epsilon}")
    return gamma * epsilon


def get_epsilon_array(gamma_array):
    """Flip 0 and 1 for epsilon from gamma"""
    return list(map(lambda d: '1' if d == '0' else '0', gamma_array))


def get_gamma_epsilon(df: pd.DataFrame):
    gamma_array = get_gamma_array(df)
    return gamma_array, get_epsilon_array(gamma_array)


def query_on(df, column, value):
    query = f"c{column} == ['{value}']"
    return df.query(query)


def part_2(df: pd.DataFrame):
    print("\n===== Part 2 =====")
    df_oxygen = query_oxygen(df_report, 0)
    oxygen = to_decimal(df_oxygen.to_numpy()[0])
    print(f"Oxygen scrubber rating:", oxygen)

    df_co2 = query_co2(df_report, 0)
    co2 = to_decimal(df_co2.to_numpy()[0])
    print(f"CO2 scrubber rating:", co2)
    return oxygen * co2


def query_oxygen(df: pd.DataFrame, index: int):
    if index >= df.shape[1]:
        return df

    gamma_array = get_gamma_array(df)
    query_o = query_on(df, index+1, gamma_array[index])
    # print(f"DEBUG: Query on {index}:\n{query_o}")
    # print(f"DEBUG: shape = {query_o.shape}")
    if query_o.shape[0] == 1:
        return query_o
    else:
        return query_oxygen(query_o, index+1)


def query_co2(df: pd.DataFrame, index: int):
    if index >= df.shape[1]:
        return df

    gamma_array, epsilon_array = get_gamma_epsilon(df)
    query = query_on(df, index+1, epsilon_array[index])
    # print(f"DEBUG: Query on {index}:\n{query}")
    # print(f"DEBUG: shape = {query.shape}")
    if query.shape[0] == 1:
        return query
    else:
        return query_co2(query, index+1)


# MAIN STARTS HERE
INPUT = "input.txt"
with open(INPUT) as file:
    lines = file.readlines()

binary_arrays = to_binary_matrix(lines)
headers = make_headers(binary_arrays.shape[1])
df_report = pd.DataFrame(binary_arrays, columns=headers)

solution_1 = part_1(df_report)
print(f"The power consumption of the submarine is {solution_1}.")

# Part 2
solution_2 = part_2(df_report)
print(f"The life support rating of the submarine = {solution_2}")
