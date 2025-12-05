import pathlib
import csv
import os
import math

curr_dir = pathlib.Path(__file__).parent.resolve()

def parse_range(range):
  """
  given `range`, returns the min, max inclusive of the range

  :param range: string range following `[1-9]?[0-9]+\-[1-9]?[0-9]`
  """
  [min_id, max_id] = range.split('-')
  # print(min_id, max_id)
  return [min_id, max_id]

def check_invalid_ids(first_half, min_id, max_id):
  """
  Docstring for check_invalid_ids
  
  :param start_id: int that is the first half of a starting id. min: 1
  :param min_id: string representing the inclusive min id
  :param max_id: string representing the inclusive max id
  """
  # invalid_ids = []
  half_len = len(str(first_half))
  # print('first half', first_half, 'half len', half_len)
  start_id = int(first_half * pow(10, half_len) + first_half)
  # print('starting at', start_id, 'range', min_id, '->', max_id)
  invalid_id_sum = 0

  while start_id <= int(max_id):
    if start_id >= int(min_id):
      # print('invalid', int(start_id))
      # invalid_ids.append(start_id)
      invalid_id_sum += start_id

    first_half += 1
    half_len = len(str(first_half))
    start_id = first_half * pow(10, half_len) + first_half
  # print('invalid ids', invalid_ids)
  return invalid_id_sum

def check_is_id_invalid(id):
  # while
  return False


def get_invalid_id_sum():
  # with open(os.path.join(curr_dir, 'd2_example.in'),'r') as file:
  with open(os.path.join(curr_dir, 'd2.in'),'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
      ranges = [parse_range(range) for range in line]
    # print(ranges)
  
  range_sum = 0
  for [min_id, max_id] in ranges:
    if len(min_id) == len(max_id) and len(min_id) % 2 != 0:
      # cannot be a "repeated twice" number in here, as there are an odd number of digits
      continue
    # edge case: [0-9] min id -> start with 1 and check for increasing
    if int(min_id) < 10:
      range_sum += check_invalid_ids(1, min_id, max_id)
    else:
      number_length = len(min_id)
      half_length = int(math.floor(number_length / 2))
      first_half = int(min_id[0:half_length])
      range_sum += check_invalid_ids(first_half, min_id, max_id)
  return range_sum

def get_invalid_id_sum_p2():
  with open(os.path.join(curr_dir, 'd2_example.in'),'r') as file:
  # with open(os.path.join(curr_dir, 'd2.in'),'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
      ranges = [parse_range(range) for range in line]
    # print(ranges)
  
  range_sum = 0
  for [min_id, max_id] in ranges:
    start_id = int(min_id)
    while start_id <= int(max_id):
      if check_is_id_invalid(start_id):
        range_sum += start_id
      start_id += 1
  print('p2 -', range_sum)

print('p1', get_invalid_id_sum())
get_invalid_id_sum_p2()