import pathlib
import os

curr_dir = pathlib.Path(__file__).parent.resolve()

def get_largest_joltage(joltage_str):
  # should be greedy
  tens_digit = int(joltage_str[0])
  ones_digit = 0

  joltage_len = len(joltage_str)
  
  for i in range(1, joltage_len):
    curr_jolt = int(joltage_str[i])
    if curr_jolt > tens_digit and i < joltage_len - 1:
      tens_digit = curr_jolt
      ones_digit = 0
    else:
      # last element
      if ones_digit < curr_jolt:
        ones_digit = curr_jolt
  print(tens_digit, ones_digit)

  return tens_digit * 10 + ones_digit

def get_joltage_sum():
  joltage = 0
  # with open(os.path.join(curr_dir, 'd3_example.in'),'r') as file:
  with open(os.path.join(curr_dir, 'd3.in'),'r') as file:
    for line in file:
      joltage += get_largest_joltage(line.strip())
      # print('\tupdated joltage to', joltage)

  print('p1 joltage', joltage)
  return joltage

def get_largest_joltage_p2(joltage_str):
  return 0

def get_joltage_sum_p2():
  joltage = 0
  with open(os.path.join(curr_dir, 'd3_example.in'),'r') as file:
  # with open(os.path.join(curr_dir, 'd3.in'),'r') as file:
    for line in file:
      joltage += get_largest_joltage(line.strip())
      # print('\tupdated joltage to', joltage)

  print('p1 joltage', joltage)
  return joltage

get_joltage_sum(2)