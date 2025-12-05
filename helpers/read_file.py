from inspect import stack
from os import path

def read_to_list(filename, cast_fn=str):
    """
    assumes filename is relative to the calling file and a simple file with values per line
    and reads it into a list. casts the elements according to cast_fn. ignores empty lines.
    """
    caller_frame = stack()[1]
    caller_file = caller_frame.filename
    caller_dir = path.dirname(path.realpath(caller_file))

    input_file = open(path.join(caller_dir, filename), 'r')
    input_list = [cast_fn(line.strip()) for line in input_file if line.strip()]
    input_file.close()
    return input_list
