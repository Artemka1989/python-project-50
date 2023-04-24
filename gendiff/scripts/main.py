import argparse
import json


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
#  Positional arguments
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

# Otional arguments
parser.add_argument('-f', '--format', type=str, help='set format of output',
                    default='gen')
args = parser.parse_args()


def generate_diff(first_file, second_file):
    result = ['{']
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    for key, value in sorted(file1.items()):
        if key in file2.keys() and value in file2.values():
            result.append(f'   {key}: {value}')
        else:
            result.append(f'  -{key}: {value}')
    for key2, value2 in sorted(file2.items()):
        if key2 in file1.keys() and value2 in file1.values():
            pass
        else:
            result.append(f'  +{key2}: {value2}')
    result.append('}')
    res_str = '\n'.join(result)
    return res_str


if args.format == 'gen':
    generate_diff(args.first_file, args.second_file)
