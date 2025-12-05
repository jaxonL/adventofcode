import pathlib
import os
from helpers.read_file import read_to_list

curr_dir = pathlib.Path(__file__).parent.resolve()

def make_rolls_row(rolls_string):
  return [x for x in rolls_string]

def make_rolls_map(filename):
  input_map = read_to_list(filename, make_rolls_row)
  # print(input_map)
  return input_map

def has_roll(r, c, rollmap):
  max_r = len(rollmap)
  max_c = len(rollmap[0])
  if r >= max_r or r < 0 or c >= max_c or c < 0:
    # invalid coordinates => assume empty
    return False
  
  return rollmap[r][c] == '@'
  

def can_remove_roll(r, c, rollmap):
  # check top left -> top right, left, right, bottom left -> bottom right
  adjacent_rolls_count = 0
  # (r-1, c-1)
  # (r-1, c)
  # (r-1, c+1)
  # (r, c-1)
  # (r+1, c-1)
  # (r+1, c)
  # (r+1, c+1)
  for r_check in range(r-1, r+2):
    for c_check in range(c-1, c+2):
      if r_check == r and c_check == c:
        # skip checking itself
        continue
      if has_roll(r_check, c_check, rollmap):
        adjacent_rolls_count += 1
      if adjacent_rolls_count >= 4:
        return False
  return True

def count_rolls(input_map):
  rolls = 0

  # brute force
  for r in range(0, len(input_map)):
    for c in range(0, len(input_map[0])):
      if input_map[r][c] == '.':
        # no roll to remove
        continue
      if can_remove_roll(r, c, input_map):
        rolls += 1
        # mark as removed
        input_map[r][c] = '.'
  return rolls

def count_rolls_p1():
  parsed_map = make_rolls_map('d4_example.in')
  # parsed_map = make_rolls_map('d4.in')

  print('p1 rolls count', count_rolls(parsed_map))

count_rolls_p1()

def count_rolls_p2():
  removed_rolls = 0
  # parsed_map = make_rolls_map('d4_example.in')
  parsed_map = make_rolls_map('d4.in')
  # print(parsed_map)
  while True:
    current_removal = count_rolls(parsed_map)
    if current_removal == 0:
      break
    # print('updated map', parsed_map)
    # print(type(parsed_map), type(parsed_map[0]))
    removed_rolls += current_removal
  print('p2 rolls count', removed_rolls)
  return removed_rolls

count_rolls_p2()