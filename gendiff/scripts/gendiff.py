import argparse
import json


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
#  Positional arguments
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

# OPtional arguments
parser.add_argument('-f', '--format', type=str, help='set format of output',
                    default='gen')
args = parser.parse_args()


def main():
    def generate_diff(first_file, second_file):
        file1 = json.load(open(first_file))
        print(file1)
        file2 = json.load(open(second_file))
        print(file2)
        merged_file = {**file1, **file2}
        sorted_merged_file = dict(sorted(merged_file.items()))
        for key, value in sorted_merged_file.items():
            print(key, ":", value)
    if args.format == 'gen':
        generate_diff(args.first_file, args.second_file)


if __name__ == main:
    main()
