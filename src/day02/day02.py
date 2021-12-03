# Advent of Code 2021
# --- Day 2: Dive! ---
# https://adventofcode.com/2021/day/2
#
# Author: NoNonsenseTekkie


def part_1(commands):
    """
    Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?
    :param commands: the list of commands
    :return: product of final horizontal position and depth
    """
    horizontal_pos = 0
    depth = 0
    for command in commands:
        details = command.split()
        value = int(details[1].strip())
        if details[0] == "forward":
            horizontal_pos += value
        elif details[0] == "up":
            depth -= value
        elif details[0] == "down":
            depth += value
    print(f"Horizontal position: {horizontal_pos} and depth: {depth}")
    return horizontal_pos * depth


def part_2(commands):
    """
    https://adventofcode.com/2021/day/2#part2
    :param commands: the list of commands
    :return: product of final horizontal position and depth
    """
    aim = 0
    h_pos = 0
    depth = 0
    for command in commands:
        details = command.split()
        value = int(details[1].strip())
        if details[0] == "forward":
            h_pos += value
            depth += value * aim
        elif details[0] == "up":
            aim -= value
        elif details[0] == "down":
            aim += value
    print(f"Horizontal position: {h_pos} and depth: {depth}")
    return h_pos * depth


# MAIN STARTS HERE
INPUT = "input.txt"
with open(INPUT) as file:
    lines = file.readlines()

    solution_1 = part_1(lines)
    print(f"Part 1 answer: {solution_1}")

    solution_2 = part_2(lines)
    print(f"Part 2 answer: {solution_2}")
