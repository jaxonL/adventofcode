# secret entrance

import pathlib
import os
from helpers.read_file import read_to_list
import math

curr_dir = pathlib.Path(__file__).parent.resolve()
# print(curr_dir)

def parse_instructions(instr):
  """
  given the instruction `instr`, returns a numeric value to
  indicate the rotation directive

  :param instr: string instruction following `(L|R)[0-9]+`
  """
  direction = instr[0]
  value = int(instr[1:])
  instruction = value if direction == 'R' else value * -1
  # print(direction, value, instruction)
  return instruction


def count_zeroes(land_on_zero=True):
  start = 50
  zero_count = 0
  with open(os.path.join(curr_dir,'d1.in'), 'r') as file:
    for line in file:
      directive = parse_instructions(line.strip())
      if not land_on_zero:
        # find distance to zero
        # -start or 100 - start
        abs_directive = abs(directive)
        if directive < 0 and abs_directive >= start and start != 0:
          # turning left -- bring back to 0 then determine additional 0 clicks
          abs_directive -= start
          zero_count += 1
        elif directive > 0 and abs_directive >= 100 - start and start != 0:
          abs_directive -= (100 - start)
          zero_count += 1
        # print('start', start, 'dir', directive, 'absolute', abs_directive, 'passed zero', zero_count)
        pass_zero_count = math.floor(abs_directive / 100)
        zero_count += pass_zero_count

      start += directive
      start %= 100
      if land_on_zero and start == 0:
        zero_count += 1
  return zero_count

print('part 1 answer', count_zeroes())
print('part 2 answer', count_zeroes(False))
