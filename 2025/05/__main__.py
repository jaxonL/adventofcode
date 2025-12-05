import pathlib
import os

curr_dir = pathlib.Path(__file__).parent.resolve()

def parse_ranges(range_str):
  [min, max] = range_str.split('-')
  return [int(min), int(max)]

def parse_input_file():
  parsing_ingredients = False
  ranges = []
  ingredients = []
  # with open(os.path.join(curr_dir, 'd5_example.in'),'r') as file:
  with open(os.path.join(curr_dir, 'd5.in'),'r') as file:
    for line in file:
      stripped_line = line.strip()
      if len(stripped_line) == 0:
        # print('parsing ingredients now')
        parsing_ingredients = True
        continue
      if parsing_ingredients:
        ingredients.append(int(stripped_line))
      else:
        ranges.append(parse_ranges(stripped_line))
  ranges.sort(key=lambda range_pair: range_pair[0])
  ingredients.sort()
  return [ranges, ingredients]

def make_distinct_ranges(ranges):
  merged_ranges = []
  range_min, range_max = ranges[0]
  for id_range in ranges[1:]:
    min_id, max_id = id_range
    if min_id > range_max:
      # non-overlapping; reset checks
      merged_ranges.append([range_min, range_max])
      range_min = min_id
      range_max = max_id
    else:
      # overlapping -- check if we're extending end
      if max_id > range_max:
        range_max = max_id

  merged_ranges.append([range_min, range_max])
  # print('merged to become', merged_ranges)
  return merged_ranges

def verify_ingredient_freshness(ingredient_list, distinct_ranges):
  ingredient_index = 0
  ingredient_count = len(ingredient_list)
  fresh_count = 0

  for id_range in distinct_ranges:
    min_id, max_id = id_range
    print('checking range', id_range)
    while ingredient_index < ingredient_count:
      ingredient_id = ingredient_list[ingredient_index]
      print('\t is', ingredient_id, 'not in range?', ingredient_id < min_id)
      if ingredient_id < min_id:
        ingredient_index += 1
      else:
        break
    
    if ingredient_index >= ingredient_count:
      print('\t no more ingredients')
      break

    # min_id < ingredient_id right now
    while min_id <= ingredient_id <= max_id:
      print('\tcounting', ingredient_id, 'as fresh')
      fresh_count += 1
      ingredient_index += 1
      if ingredient_index >= ingredient_count:
        break
      ingredient_id = ingredient_list[ingredient_index]
    
    if ingredient_index >= ingredient_count:
      print('\t no more ingredients')
      break
    print('\t ingredient id', ingredient_id, '>', id_range[1], ', going to next window to check')
    # id > max_id right now -> go to next window
  return fresh_count
    # while ingredient_index < ingredient_count and 

  # for ingredient_id in ingredient_list:
  #   print('checking for', ingredient_id, 'in range', distinct_ranges[range_index])
  #   if range_min <= ingredient_id <= range_max:
  #     # in the window
  #     fresh_count += 1
  #   # not in the window -- check if it falls before or after
  #   if ingredient_id < range_min:
  #     # falls before -- don't shift window, go to next ingredient
  #     continue
  #   # falls after -- shift window and check again 
  #   if ingredient_id > range_max:
  #     # shift the window up and check
  #     range_index += 1
  #     # while range_index < len(distinct_ranges) and ingredient_id < range_min
  #     if range_index >= len(distinct_ranges):
  #       break
  #     range_min, range_max = distinct_ranges[range_index]
  #     # check if in window now
  #     if range_min <= ingredient_id <= range_max:
  #       fresh_count += 1
  #     continue
  #   fresh_count += 1
  # return fresh_count

def get_fresh_count():
  [sorted_ranges, ingredients] = parse_input_file()
  # print(len(sorted_ranges), len(ingredients))
  distinct_ranges = make_distinct_ranges(sorted_ranges)

  # fresh_count = verify_ingredient_freshness(ingredients, distinct_ranges)
  # print('p1 fresh count', fresh_count)

  total_fresh_ids = 0
  for min_id, max_id in distinct_ranges:
    total_fresh_ids += (max_id - min_id + 1)

  print('p2 fresh ids count', total_fresh_ids)

get_fresh_count()
